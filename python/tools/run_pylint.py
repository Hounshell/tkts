import sys
from pylint.lint import Run

def main():
    if len(sys.argv) < 2:
        print("Usage: run_pylint.py <file1.py> [file2.py ...]", file=sys.stderr)
        sys.exit(1)

    files_to_lint = sys.argv[1:]

    # Pass files to Pylint without invoking exit() immediately
    results = Run(["--score=n"] + files_to_lint)

    # Pylint exit code bitmask:
    # 1 = Fatal, 2 = Error, 4 = Warning, 8 = Refactor, 16 = Convention, 32 = Usage
    exit_code = results.linter.msg_status
    if exit_code & (1 | 2 | 32):
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()

