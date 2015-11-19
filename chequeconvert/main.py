import sys
import argparse
from .base import generate_word


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    subparser = parser.add_subparsers(dest='chequeconvert')
    args = parser.parse_args(sys.argv[1:])
    amt = getattr(args, args.chequeconvert)
    print generate_word(amt)
