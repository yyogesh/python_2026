import argparse
from pathlib import Path

# Create the parser
parser = argparse.ArgumentParser(
    prog='mytool',
    description='A demonstration of argparse',
    epilog='For more info visit https://docs.python.org/3/library/argparse.html'
)
# Positional argument — REQUIRED, no -- prefix
parser.add_argument('filename',
    type=str,
    help='Path to the input file'
)
# Optional flag — starts with -
parser.add_argument('--output', '-o',
    type=str,
    default='output.txt',
    help='Output file path (default: output.txt)'
)
# Boolean flag — store_true means flag presence = True
parser.add_argument('--verbose', '-v',
    action='store_true',
    help='Enable verbose output'
)
# Type conversion — argparse converts for you
parser.add_argument('--count', '-n',
    type=int,
    default=10,
    help='Number of items to process (default: 10)'
)
# Choices — restrict to specific values
parser.add_argument('--format',
    choices=['json', 'csv', 'txt'],
    default='json',
    help='Output format'
)
# Version flag
parser.add_argument('--version',
    action='version',
    version='%(prog)s 1.0.0'
)
args = parser.parse_args()
print(args.filename)
print(args.verbose)
print(args.count)
# Running: python mytool.py data.csv --verbose --count 20 --format csv
# args.filename = 'data.csv'
# args.verbose  = True
# args.count    = 20  (already an int!)
# args.format   = 'csv