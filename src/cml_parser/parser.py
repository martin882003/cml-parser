from dataclasses import dataclass, asdict
from pathlib import Path
from textx import metamodel_from_file
from textx.exceptions import TextXSyntaxError
from typing import List, Optional, Any, Union
import argparse
import json
import sys
import os


@dataclass
class Diagnostic:
    message: str
    line: Optional[int] = None
    col: Optional[int] = None
    filename: Optional[str] = None
    expected: Optional[List[str]] = None
    context: Optional[str] = None

    def pretty(self) -> str:
        location = ""
        if self.filename:
            location += f"{self.filename}"
        if self.line is not None:
            location += f":{self.line}"
            if self.col is not None:
                location += f":{self.col}"
        if location:
            location = f"[{location}] "
        expected = f" (expected: {', '.join(self.expected)})" if self.expected else ""
        return f"{location}{self.message}{expected}"


@dataclass
class ParseResult:
    model: Optional[Any]
    errors: List[Diagnostic]
    warnings: List[Diagnostic]
    source: Optional[str] = None
    filename: Optional[str] = None

    @property
    def ok(self) -> bool:
        return not self.errors

    @property
    def has_errors(self) -> bool:
        return bool(self.errors)

    @property
    def has_warnings(self) -> bool:
        return bool(self.warnings)

    @property
    def first_error(self) -> Optional[Diagnostic]:
        return self.errors[0] if self.errors else None

    def to_dict(self) -> dict:
        return {
            "ok": self.ok,
            "errors": [asdict(e) for e in self.errors],
            "warnings": [asdict(w) for w in self.warnings],
            "filename": self.filename,
        }

    def to_json(self, include_model: bool = False) -> str:
        data = self.to_dict()
        if include_model and self.model is not None:
            data["model"] = model_to_data(self.model)
        return json.dumps(data, ensure_ascii=False, indent=2)

    def errors_text(self) -> str:
        return "\n".join(e.pretty() for e in self.errors)

    def tree(self, max_depth: Optional[int] = None) -> str:
        if self.model is None:
            return "<no model>"
        return render_tree(self.model, max_depth=max_depth)

    def raise_on_error(self):
        if self.errors:
            raise CmlSyntaxError(self.errors[0])
        return self

    # Convenience accessors for common top-level elements.
    def contexts(self):
        if not self.model or not hasattr(self.model, "elements"):
            return []
        return [e for e in self.model.elements if e.__class__.__name__ == "BoundedContext"]

    def relationships(self):
        if not self.model or not hasattr(self.model, "elements"):
            return []
        rels = []
        for e in self.model.elements:
            if e.__class__.__name__ == "ContextMap":
                rels.extend(getattr(e, "relationships", []))
        return rels

    def use_cases(self):
        if not self.model or not hasattr(self.model, "elements"):
            return []
        return [e for e in self.model.elements if e.__class__.__name__ == "UseCase"]


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


def parse_file(file_path):
    """
    Strict parsing of a .cml file. Raises CmlSyntaxError on failure.
    """
    result = _parse_internal(path=file_path, text=None, strict=True)
    return result


def parse_file_safe(file_path):
    return _parse_internal(path=file_path, text=None, strict=False)


def parse_text(text: str, *, filename: Optional[str] = None, strict: bool = True):
    return _parse_internal(path=filename, text=text, strict=strict)


class DisplayStr(str):
    """
    A string that prints naturally in REPLs (repr == value).
    Useful for showing source text without escape sequences.
    """

    def __repr__(self) -> str:  # pragma: no cover - trivial
        return str(self)


def _parse_internal(path: Optional[str], text: Optional[str], strict: bool) -> ParseResult:
    filename = str(path) if path else None
    source = text
    if path and source is None:
        source = Path(path).read_text(encoding="utf-8")
    mm = get_metamodel()
    try:
        if text is None:
            model = mm.model_from_file(filename)
        else:
            model = mm.model_from_str(text, file_name=filename)
        result = ParseResult(
            model=model,
            errors=[],
            warnings=[],
            source=DisplayStr(source) if source is not None else None,
            filename=filename,
        )
        return result
    except Exception as exc:
        diagnostic = _diagnostic_from_exception(exc, filename, source)
        result = ParseResult(model=None, errors=[diagnostic], warnings=[], source=source, filename=filename)
        if strict:
            raise CmlSyntaxError(diagnostic) from exc
        return result


def model_to_data(obj: Any, visited=None) -> Union[dict, list, str, int, float, bool, None]:
    """
    Best-effort conversion of a textX model to plain data structures for JSON export.
    """
    if visited is None:
        visited = set()
    if id(obj) in visited:
        return "<recursion>"
    visited.add(id(obj))

    if isinstance(obj, (str, int, float, bool)) or obj is None:
        return obj
    if isinstance(obj, list):
        return [model_to_data(item, visited) for item in obj]
    if isinstance(obj, dict):
        return {k: model_to_data(v, visited) for k, v in obj.items()}
    # textX model objects behave like plain objects; walk their __dict__
    if hasattr(obj, "__dict__"):
        data = {}
        for k, v in vars(obj).items():
            if k.startswith("_"):
                continue
            data[k] = model_to_data(v, visited)
        data["__type__"] = obj.__class__.__name__
        return data
    return str(obj)


def render_tree(obj: Any, max_depth: Optional[int] = None) -> str:
    """
    Render a simple tree view of the model for quick inspection.
    """
    lines: List[str] = []
    visited = set()

    def label(x):
        name = getattr(x, "name", None)
        typ = x.__class__.__name__
        return f"{typ}({name})" if name is not None else typ

    def walk(node, depth):
        if max_depth is not None and depth > max_depth:
            return
        prefix = "  " * depth
        if isinstance(node, (str, int, float, bool)) or node is None:
            lines.append(f"{prefix}{repr(node)}")
            return
        if isinstance(node, list):
            lines.append(f"{prefix}list[{len(node)}]")
            for item in node:
                walk(item, depth + 1)
            return
        if id(node) in visited:
            lines.append(f"{prefix}<recursion {label(node)}>")
            return
        visited.add(id(node))
        if hasattr(node, "__dict__"):
            lines.append(f"{prefix}{label(node)}")
            for k, v in vars(node).items():
                if k.startswith("_"):
                    continue
                lines.append(f"{prefix}  {k}:")
                walk(v, depth + 2)
        else:
            lines.append(f"{prefix}{label(node)}")

    walk(obj, 0)
    return "\n".join(lines)


def main(argv=None) -> int:
    """
    Minimal CLI entrypoint to parse a single .cml file.
    """
    args = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(prog="cml-parse", add_help=True)
    parser.add_argument("file", nargs="?", help="Path to .cml file")
    parser.add_argument("--json", action="store_true", help="Emit parse result as JSON (model converted best-effort)")
    parser.add_argument("--tree", action="store_true", help="Print a tree view of the model")
    parser.add_argument("--summary", action="store_true", help="Print a short success summary")
    parsed = parser.parse_args(args)

    if not parsed.file:
        parser.print_usage(file=sys.stderr)
        return 1

    result = parse_file_safe(parsed.file)
    if not result.ok:
        print(f"Error parsing {parsed.file}:", file=sys.stderr)
        for err in result.errors:
            print(err.pretty(), file=sys.stderr)
        return 1

    if parsed.json:
        print(result.to_json(include_model=True))
        return 0
    if parsed.tree:
        print(render_tree(result.model))
        return 0
    if parsed.summary:
        print(result.summary())
        return 0

    print(f"Successfully parsed {parsed.file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
