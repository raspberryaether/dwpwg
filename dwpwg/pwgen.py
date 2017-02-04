"""Password generator utility. Uses 3 d20 dice for entropy."""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from .wordlist import WordList
from .format import parse_format


def main():
    ap = ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        epilog="""

Patterns are constructed as follows:
- `{.}` is replaced by a lowercase word.
- `{+}` is replaced by a Capitalized word.
- `{@}` is replaced by an ALL-CAPS word.
- `{%}` is replaced by the numerical value of one dice roll.
- `{#42}` is replaced by a number no higher than 42.
- `{{` is replaced by `{` as soon as it is encountered.
- `}}` is replaced by `}` if there is no currently open brace.
- any other character is treated as a literal (kept unchanged).

For example, the pattern:
    {{octothorpe_{@}.{%}-{#1000}[{+}{.}]}}

may output the passphrase:
    {octothorpe_RAZOR.12-254[Applynougat]}

        """.lstrip())

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
