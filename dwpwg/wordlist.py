"""Provider for dwpwg word lists."""

import random
from pkg_resources import resource_filename

DIE_FACES = 20
NUM_DICE = 3

class WordList(object):
    def __init__(self, words):
        """Create a word list object from the given iterable of words."""
        self.words = words

    @classmethod
    def load_default(cls, filepath):
        return cls.load(resource_filename("dwpwg", "lists/" + filepath))

    @classmethod
    def load(cls, filepath):
        """Loads a word list from a simple flat file (newline-separated)."""
        words = []
        with open(filepath) as f:
            for line in f:
                line = line.strip()
                if 4 <= len(line) <= 6:
                    words.append(line)
        return cls(words)

    def save(self, filepath):
        with open(filepath, "w") as f:
            for word in self.words:
                f.write(word + "\n")

    def sort(self):
        self.words.sort()

    def shuffle(self):
        """Uses a CSPRNG to generate a new order for the word list."""
        rng = random.SystemRandom()
        rng.shuffle(self.words)

    def build(self, filepath):
        """Stub. Will eventually generate PDF of the wordlist to be printed."""

    def get(self, dice_list):
        """Use the given list of dice throws to generate a word.

        An insufficient amount of throws will cause a LookupError.
        Throws lower than 1 or higher than DIE_FACES will cause a ValueError.
        Extra throws will be ignored.
        """
        if len(dice_list) < NUM_DICE:
            raise LookupError("invalid number of die throws")

        offsets = []
        for throw in dice_list:
            if 1 <= throw <= DIE_FACES:
                offsets.append(throw - 1)
            else:
                err = "throw value {} is out of range"
                raise ValueError(err.format(throw))

        index = 0
        while offsets:
            offset = offsets.pop(0)
            exponent = len(offsets)
            index += offset * (DIE_FACES**exponent)

        if __name__ == "__main__":
            print "DEBUG: {}".format(index)

        return self.words[index]

def main(args):
    test = WordList.load(args[1])
    print len(test.words), "words loaded"
    try:
        print (test.get([1, 1, 1]) +
               "..." +
               test.get([20, 20, 20]))
        test.shuffle()
        test.sort()
        print "Tests passed."
    except:
        print "Tests failed."

    throws = [int(x) for x in args[2:5]]
    print test.get(throws)


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv));
