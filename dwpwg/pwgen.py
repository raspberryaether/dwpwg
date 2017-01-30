"""Password generator utility. Uses 3 d20 dice for entropy."""

from wordlist import WordList, NUM_DICE, DIE_FACES
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("num_words", metavar="number-of-words", type=int,
                    help="the number of words to generate")
    args = ap.parse_args()
    wordlist = WordList.load_default("en/full")
    wordlist.shuffle()

    num_throws = args.num_words * NUM_DICE
    throws = []
    while num_throws > len(throws):
        try:
            print "Input throws (%d): " % (num_throws - len(throws)),
            throw = int(raw_input())
            if 1 <= throw <= DIE_FACES:
                throws.append(throw)
            else:
                raise ValueError
        except:
            print "Try again (%d):   " % (num_throws - len(throws)),

    words = []
    while args.num_words > len(words):
        word = wordlist.get([throws.pop(0) for x in xrange(3)])
        words.append(word)

    password = "".join(words)
    print password

if __name__ == "__main__":
    import sys
    sys.exit(main());
