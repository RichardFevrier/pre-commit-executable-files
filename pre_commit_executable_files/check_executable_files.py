import argparse
import os
import stat

from typing import Sequence


def check_executables(paths: list[str]) -> int:
    for path in paths:
        if not os.access(path, os.X_OK):
            print(f"{path} is not executable.")
            print("Trying to fix it...")
            st = os.stat(path)
            os.chmod(path, st.st_mode | stat.S_IEXEC)
            if os.access(path, os.X_OK):
                print(f"{path} is now executable.")
            else:
                print(f"Unable to make {path} executable.")
                return 1

    return 0


def main(argv: Sequence[str] | None = None) -> int:

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(argv)

    return check_executables(args.filenames)
