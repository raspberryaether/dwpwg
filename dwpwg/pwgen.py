"""Password generator utility. Uses 3 d20 dice for entropy."""

from argparse import ArgumentParser
from .wordlist import WordList
from .format import parse_format


def main():
    ap = ArgumentParser()
    ap.add_argument("pattern", type=str,
                    help="the pattern of the generated phrase")

    args = ap.parse_args()

    wordlist = WordList.load_default("en/full")
    wordlist.shuffle()

    elements = parse_format(args.pattern)
    
    for element in elements:
        element.activate(wordlist)
        while element.requires_entropy():
            element.process_entropy(int(raw_input("Input roll: ")))

    print "".join(str(element) for element in elements)


if __name__ == "__main__":
    import sys
    sys.exit(main())
