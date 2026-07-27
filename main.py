"""Command-line program for Add2Num."""

from __future__ import annotations

import argparse
import logging

from my_big_number import MyBigNumber


def parse_args() -> argparse.Namespace:
    """Read command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Add two large non-negative integers represented as strings."
    )
    parser.add_argument("stn1", help="First number")
    parser.add_argument("stn2", help="Second number")
    parser.add_argument("--log", action="store_true", help="Show each addition step")
    return parser.parse_args()


def main() -> int:
    """Run the CLI."""
    args = parse_args()

    if args.log:
        logging.basicConfig(level=logging.INFO, format="%(message)s")

    print(MyBigNumber().sum(args.stn1, args.stn2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
