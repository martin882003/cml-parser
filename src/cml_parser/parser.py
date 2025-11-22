from dataclasses import dataclass, asdict
from pathlib import Path
from textx import metamodel_from_file
from textx.exceptions import TextXSyntaxError
from typing import List, Optional, Any
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

    def to_dict(self) -> dict:
        return {
            "ok": self.ok,
            "errors": [asdict(e) for e in self.errors],
            "warnings": [asdict(w) for w in self.warnings],
            "filename": self.filename,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def summary(self) -> str:
        if self.ok:
            return f"Parsed successfully: {self.filename or ''}".strip()
        return "\n".join(e.pretty() for e in self.errors)


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
        result = ParseResult(model=model, errors=[], warnings=[], source=source, filename=filename)
        return result
    except Exception as exc:
        diagnostic = _diagnostic_from_exception(exc, filename, source)
        result = ParseResult(model=None, errors=[diagnostic], warnings=[], source=source, filename=filename)
        if strict:
            raise CmlSyntaxError(diagnostic) from exc
        return result


def main(argv=None) -> int:
    """
    Minimal CLI entrypoint to parse a single .cml file.
    """
    args = sys.argv[1:] if argv is None else argv
    if args:
        result = parse_file_safe(args[0])
        if result.ok:
            print(f"Successfully parsed {args[0]}")
            return 0
        print(f"Error parsing {args[0]}:", file=sys.stderr)
        for err in result.errors:
            print(err.pretty(), file=sys.stderr)
        return 1
    print("Usage: python parser.py <file.cml>", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
