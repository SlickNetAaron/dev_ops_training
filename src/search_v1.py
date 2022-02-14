import argparse
import sys

active_pipe=(True if not sys.stdin.isatty() else False )

parser = argparse.ArgumentParser(
    usage=f"Usage: search.py [SEARCH] [INPUT_FILENAME] ",
    description="Search for exact string in [FILENAME] or piped input"
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
    default=(sys.stdin if active_pipe else False),
    help="File name or default to STDIN"
)

args = parser.parse_args()

#print(args.input_file.name)
if args.input_file.name != '<stdin>' and active_pipe:
    print(f"Error: Too many inputs: Both piped input and file not allowed. File:{args.input_file.name}.")
    print("Use either a pipe or input filename - noth both.")
    parser.print_help()
    exit()

for line in args.input_file.readlines():
    if args.search in line:
        print(line)

