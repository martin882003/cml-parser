from textx import metamodel_from_file
from types import SimpleNamespace
import sys
import os


def get_metamodel():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    grammar_path = os.path.join(current_dir, 'cml.tx')
    mm = metamodel_from_file(grammar_path, debug=False, global_repository=True)
    return mm


def parse_file(file_path):
    mm = get_metamodel()
    model = mm.model_from_file(file_path)
    print(f"Successfully parsed {file_path}")
    return model


def parse_file_safe(file_path):
    try:
        return SimpleNamespace(model=parse_file(file_path), error=None, raw_text=None)
    except Exception as e:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return SimpleNamespace(model=None, error=e, raw_text=content)


def main(argv=None) -> int:
    """
    Minimal CLI entrypoint to parse a single .cml file.
    """
    args = sys.argv[1:] if argv is None else argv
    if args:
        try:
            parse_file(args[0])
            return 0
        except Exception as e:
            print(f"Error parsing {args[0]}: {e}", file=sys.stderr)
            return 1
    print("Usage: python parser.py <file.cml>", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
