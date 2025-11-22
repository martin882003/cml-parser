from dataclasses import asdict
from pathlib import Path
from textx import metamodel_from_file
from textx.exceptions import TextXSyntaxError
from typing import List, Optional, Any, Union
import argparse
import json
import sys
import os

from .cml_objects import (
    CML,
    ParseResult,
    Diagnostic,
    Domain,
    Subdomain,
    SubdomainType,
    ContextMap,
    Context,
    Relationship,
    RelationshipType,
    UseCase,
    Entity,
    Aggregate,
    Service
)

class CmlSyntaxError(Exception):
    def __init__(self, diagnostic: Diagnostic):
        super().__init__(diagnostic.pretty())
        self.diagnostic = diagnostic

def get_metamodel():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    grammar_path = os.path.join(current_dir, 'cml.tx')
    mm = metamodel_from_file(grammar_path, debug=False, global_repository=True)
    return mm

def _diagnostic_from_exception(exc: Exception, filename: Optional[str], source: Optional[str]) -> Diagnostic:
    if isinstance(exc, TextXSyntaxError):
        return Diagnostic(
            message=exc.message,
            line=exc.line,
            col=exc.col,
            filename=filename or exc.filename,
            expected=[str(r) for r in getattr(exc, "expected_rules", [])] or None,
            context=getattr(exc, "context", None),
        )
    return Diagnostic(message=str(exc), filename=filename)

def parse_file(file_path) -> CML:
    """
    Strict parsing of a .cml file. Raises CmlSyntaxError on failure.
    """
    return _parse_internal(path=file_path, text=None, strict=True)

def parse_file_safe(file_path) -> CML:
    return _parse_internal(path=file_path, text=None, strict=False)

def parse_text(text: str, *, filename: Optional[str] = None, strict: bool = True) -> CML:
    return _parse_internal(path=filename, text=text, strict=strict)

def _parse_internal(path: Optional[str], text: Optional[str], strict: bool) -> CML:
    filename = str(path) if path else None
    source = text
    if path and source is None:
        source = Path(path).read_text(encoding="utf-8")
    
    mm = get_metamodel()
    model = None
    errors = []
    
    try:
        if text is None:
            model = mm.model_from_file(filename)
        else:
            model = mm.model_from_str(text, file_name=filename)
    except Exception as exc:
        errors.append(_diagnostic_from_exception(exc, filename, source))
        if strict:
            raise CmlSyntaxError(errors[0]) from exc

    parse_result = ParseResult(
        model=model,
        errors=errors,
        warnings=[],
        source=source,
        filename=filename
    )

    if model:
        return _build_cml_object(parse_result)
    else:
        return CML(parse_results=parse_result)

def _build_cml_object(parse_result: ParseResult) -> CML:
    model = parse_result.model
    cml = CML(parse_results=parse_result)

    # First pass: Create all objects (Domains, Subdomains, Contexts)
    # This is needed to resolve references in the second pass
    
    domain_map = {}
    subdomain_map = {}
    context_map_obj_map = {} # Map name -> Context object
    
    if hasattr(model, "elements"):
        for el in model.elements:
            el_type = el.__class__.__name__
            
            if el_type == "Domain":
                domain = Domain(
                    name=getattr(el, "name", ""),
                    vision=getattr(el, "vision", "")
                )
                
                # Check body for vision override
                if hasattr(el, "body") and el.body:
                    for entry in getattr(el.body, "entries", []) or []:
                        entry_type = entry.__class__.__name__
                        if entry_type == "SubdomainAttribute":
                            if hasattr(entry, "domainVisionStatement") and entry.domainVisionStatement:
                                domain.vision = entry.domainVisionStatement
                        elif entry_type == "BoundedContextAttribute":
                            if hasattr(entry, "domainVisionStatement") and entry.domainVisionStatement:
                                domain.vision = entry.domainVisionStatement

                cml.domains.append(domain)
                domain_map[domain.name] = domain
                
                # Process subdomains within domain
                _process_subdomains(el, domain, subdomain_map)

            elif el_type == "BoundedContext":
                # Contexts can be top level
                context = Context(
                    name=getattr(el, "name", ""),
                    type=getattr(el, "type", "FEATURE"), # Default?
                    state=getattr(el, "state", "UNDEFINED"), # Default?
                    vision=getattr(el, "vision", "")
                )
                
                # Check body for attributes
                if hasattr(el, "body") and el.body:
                    for entry in getattr(el.body, "entries", []) or []:
                        entry_type = entry.__class__.__name__
                        if entry_type == "BoundedContextAttribute":
                            if hasattr(entry, "type") and entry.type:
                                context.type = str(entry.type)
                            if hasattr(entry, "domainVisionStatement") and entry.domainVisionStatement:
                                context.vision = entry.domainVisionStatement
                            if hasattr(entry, "responsibilities") and entry.responsibilities:
                                context.responsibilities = entry.responsibilities
                            if hasattr(entry, "implementationTechnology") and entry.implementationTechnology:
                                context.implementation_technology = entry.implementationTechnology
                            if hasattr(entry, "knowledgeLevel") and entry.knowledgeLevel:
                                context.knowledge_level = str(entry.knowledgeLevel)

                # Process aggregates and services
                _process_context_children(el, context)
                
                context_map_obj_map[context.name] = context

            elif el_type == "ContextMap":
                cm = ContextMap(
                    name=getattr(el, "name", ""),
                    type=getattr(el, "type", "SYSTEM_LANDSCAPE"), # Default?
                    state=getattr(el, "state", "AS_IS") # Default?
                )
                
                # Extract type and state from settings
                settings = getattr(el, "contextMapSettings", []) or []
                for setting in settings:
                    if hasattr(setting, "type") and setting.type:
                        cm.type = str(setting.type)
                    if hasattr(setting, "state") and setting.state:
                        cm.state = str(setting.state)

                cml.context_maps.append(cm)

            elif el_type == "UseCase":
                uc = UseCase(name=getattr(el, "name", ""))
                
                # Extract attributes
                elements = getattr(el, "elements", []) or []
                for element in elements:
                    el_type_uc = element.__class__.__name__
                    if el_type_uc == "UseCaseActor":
                        uc.actor = getattr(element, "actor", "")
                    elif el_type_uc == "UseCaseBenefit":
                        uc.benefit = getattr(element, "benefit", "")
                    elif el_type_uc == "UseCaseScope":
                        uc.scope = getattr(element, "scope", "")
                    elif el_type_uc == "UseCaseLevel":
                        uc.level = getattr(element, "level", "")

                cml.use_cases.append(uc)

    # Second pass: Link everything
    if hasattr(model, "elements"):
        for el in model.elements:
            el_type = el.__class__.__name__
            
            if el_type == "BoundedContext":
                ctx = context_map_obj_map.get(getattr(el, "name", ""))
                if ctx:
                    # Link implements
                    implements = getattr(el, "implements", []) or []
                    for impl in implements:
                        # impl is a string (ID) from textX
                        sd_name = str(impl)
                        sd = subdomain_map.get(sd_name)
                        if sd:
                            ctx.implements.append(sd)
                            sd.implementations.append(ctx)

            elif el_type == "ContextMap":
                cm_obj = next((c for c in cml.context_maps if c.name == getattr(el, "name", "")), None)
                if cm_obj:
                    # Explicit 'contains' from settings
                    settings = getattr(el, "contextMapSettings", []) or []
                    for setting in settings:
                        if hasattr(setting, "contains"):
                            for ctx_name in getattr(setting, "contains", []) or []:
                                ctx = context_map_obj_map.get(str(ctx_name))
                                if ctx:
                                    if ctx not in cm_obj.contexts:
                                        cm_obj.contexts.append(ctx)
                                    ctx.context_map = cm_obj

                    # Relationships
                    relationships = getattr(el, "relationships", []) or []
                    for rel in relationships:
                        left_node = getattr(rel, "left", None)
                        right_node = getattr(rel, "right", None)
                        
                        left_name = getattr(left_node, "contextName", "")
                        right_name = getattr(right_node, "contextName", "")
                        
                        left_ctx = context_map_obj_map.get(left_name)
                        right_ctx = context_map_obj_map.get(right_name)
                        
                        if left_ctx and left_ctx not in cm_obj.contexts:
                            cm_obj.contexts.append(left_ctx)
                            left_ctx.context_map = cm_obj
                        if right_ctx and right_ctx not in cm_obj.contexts:
                            cm_obj.contexts.append(right_ctx)
                            right_ctx.context_map = cm_obj

                        if left_ctx and right_ctx:
                            rel_type, roles = _determine_relationship_type_and_roles(rel)
                            
                            relationship = Relationship(
                                left=left_ctx,
                                right=right_ctx,
                                type=rel_type,
                                roles=roles,
                                raw_model=rel
                            )
                            cm_obj.relationships.append(relationship)

    return cml

def _process_subdomains(domain_node, domain_obj, subdomain_map):
    # Recursive search for subdomains in the domain node
    def walk(container):
        for attr in ("items", "entries", "elements", "subdomains"):
            if hasattr(container, attr):
                for item in getattr(container, attr, []) or []:
                    if item.__class__.__name__ == "Subdomain":
                        sd_name = getattr(item, "name", "")
                        sd_type_str = getattr(item, "type", "GENERIC_SUBDOMAIN")
                        # Map string to Enum
                        try:
                            sd_type = SubdomainType(sd_type_str)
                        except ValueError:
                            sd_type = SubdomainType.GENERIC

                        sd = Subdomain(
                            name=sd_name,
                            type=sd_type,
                            vision=getattr(item, "vision", ""),
                            domain=domain_obj
                        )
                        
                        # Check body for type and vision overrides
                        if hasattr(item, "body") and item.body:
                            for entry in getattr(item.body, "entries", []) or []:
                                entry_type = entry.__class__.__name__
                                if entry_type == "SubdomainAttribute":
                                    if hasattr(entry, "type") and entry.type:
                                        try:
                                            sd.type = SubdomainType(str(entry.type))
                                        except ValueError:
                                            pass
                                    if hasattr(entry, "domainVisionStatement") and entry.domainVisionStatement:
                                        sd.vision = entry.domainVisionStatement
                                elif entry_type == "BoundedContextAttribute":
                                    if hasattr(entry, "domainVisionStatement") and entry.domainVisionStatement:
                                        sd.vision = entry.domainVisionStatement
                                elif entry_type == "DomainObject":
                                    # DomainObject wraps Entity, ValueObject, etc.
                                    inner = getattr(entry, "domainObject", None)
                                    if inner and inner.__class__.__name__ == "Entity":
                                        sd.entities.append(Entity(name=getattr(inner, "name", "")))
                                elif entry_type == "Entity":
                                    sd.entities.append(Entity(name=getattr(entry, "name", "")))

                        # Entities (legacy check, just in case)
                        if hasattr(item, "entities"):
                            for ent in item.entities:
                                sd.entities.append(Entity(name=getattr(ent, "name", "")))
                        
                        domain_obj.subdomains.append(sd)
                        subdomain_map[sd_name] = sd
                    
                    walk(item)
        
        if hasattr(container, "body"):
             walk(getattr(container, "body"))

    walk(domain_node)

def _process_context_children(context_node, context_obj):
    # Recursive search for Aggregates and Services in the context node
    def walk(container):
        for attr in ("items", "entries", "elements", "aggregates", "services"):
            if hasattr(container, attr):
                for item in getattr(container, attr, []) or []:
                    item_type = item.__class__.__name__
                    if item_type == "Aggregate":
                        agg = Aggregate(name=getattr(item, "name", ""))
                        context_obj.aggregates.append(agg)
                    elif item_type == "Service":
                        svc = Service(name=getattr(item, "name", ""))
                        context_obj.services.append(svc)
                    
                    walk(item)
        
        if hasattr(container, "body"):
             walk(getattr(container, "body"))

    walk(context_node)

def _determine_relationship_type_and_roles(rel_node) -> tuple[str, List[str]]:
    keyword = getattr(getattr(rel_node, "connection", None), "keyword", None)
    arrow = getattr(getattr(rel_node, "connection", None), "arrow", None)
    attrs = getattr(rel_node, "attributes", []) or []
    attr_type = next((getattr(a, "relType", None) for a in attrs if getattr(a, "relType", None)), None)
    
    roles = []
    left = getattr(rel_node, "left", None)
    right = getattr(rel_node, "right", None)
    for endpoint in (left, right):
        if endpoint:
            for roleset in (getattr(endpoint, "rolesBefore", None), getattr(endpoint, "rolesAfter", None)):
                if roleset:
                    roles.extend([str(x).upper() for x in getattr(roleset, "roles", [])])

    rel_type = "Unknown"
    if keyword:
        rel_type = str(keyword)
    elif attr_type:
        rel_type = str(attr_type)
    elif arrow:
        rel_type = str(arrow)
    elif "U" in roles and "D" in roles:
        rel_type = "Upstream-Downstream"
    
    return rel_type, roles

def main(argv=None) -> int:
    """
    Minimal CLI entrypoint to parse a single .cml file.
    """
    args = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(prog="cml-parse", add_help=True)
    parser.add_argument("file", nargs="?", help="Path to .cml file")
    parser.add_argument("--json", action="store_true", help="Emit parse result as JSON")
    parser.add_argument("--summary", action="store_true", help="Print a short success summary")
    parsed = parser.parse_args(args)

    if not parsed.file:
        parser.print_usage(file=sys.stderr)
        return 1

    cml = parse_file_safe(parsed.file)
    if not cml.parse_results.ok:
        print(f"Error parsing {parsed.file}:", file=sys.stderr)
        for err in cml.parse_results.errors:
            print(err.pretty(), file=sys.stderr)
        return 1

    if parsed.json:
        print(json.dumps(asdict(cml.parse_results), default=str, indent=2))
        return 0
        
    if parsed.summary:
        print(f"Successfully parsed {parsed.file}")
        print(f"Domains: {len(cml.domains)}")
        print(f"Context Maps: {len(cml.context_maps)}")
        return 0

    print(f"Successfully parsed {parsed.file}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
