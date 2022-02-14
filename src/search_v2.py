import argparse
import sys

active_pipe=(True if not sys.stdin.isatty() else False )

def init_argparse():
    parser = argparse.ArgumentParser(
        usage=f"Usage: search.py [SEARCH] [INPUT_FILENAME] ",
        description="Search for an exact string in a file or piped input"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version 0.0.1"
    )
    parser.add_argument("search", help="exact search string")
    parser.add_argument(
        "input_file",
        nargs='?',
        type=argparse.FileType('r'),
        default=(sys.stdin if active_pipe else None),
        help="File name or default to STDIN",
    )
    return parser

def input_validate(parser, args):
    if not active_pipe and not args.input_file:
        print("\n   Error: No input file or piped data provided. \n")
        parser.print_help()
        exit()

    if args.input_file.name != '<stdin>' and active_pipe:
        print(f"\n   Error: Too many inputs: Both piped input and file not allowed. File:{args.input_file.name}. \n")
        print("Use either a pipe or input filename - noth both.")
        parser.print_help()
        exit()

def search_lines(args):
    for line in args.input_file.readlines():
        if args.search in line:
            print(line)

def main():
    parser = init_argparse()
    args = parser.parse_args()
    input_validate(parser, args)
    search_lines(args)

if __name__ == '__main__':
    main()