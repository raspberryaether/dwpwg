"""Package executable file for dwpwg."""

from .pwgen import main

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv));
