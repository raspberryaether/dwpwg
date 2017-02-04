"""Parses the format string."""

from __future__ import division
import pyparsing as pp


class FormatStringError(Exception):
    pass


class EntropyRequiredError(Exception):
    pass


class Element(object):
    def __str__(self):
        if self.requires_entropy():
            raise EntropyRequiredError
        try:
            return self.content
        except AttributeError:
            return ""

    def activate(self, wordlist):
        self.wordlist = wordlist
        self.calculate()

    def calculate(self):
        pass

    def requires_entropy(self):
        return False


class OpenBrace(Element):
    content = "{"


class CloseBrace(Element):
    content = "}"


class Literal(Element):
    def __init__(self, content):
        super(Literal, self).__init__()
        self.content = content


class Variable(Element):
    def __init__(self):
        self.entropy = []
        self.entropy_needed = Ellipsis
        self.wordlist = None

    def requires_entropy(self):
        return len(self.entropy) < self.entropy_needed 
        
    def process_entropy(self, entropy):
        self.entropy.append(entropy)
        if not self.requires_entropy():
            self.prepare()

    def prepare(self):
        raise NotImplementedError

    @classmethod
    def create(cls, content):
        if content.startswith("#"):
            try:
                limit = int(content[1:])
            except:
                raise FormatStringError
            element = Number(limit)
            return element
        else:
            try:
                return {
                    "@": AllCapsWord,
                    "+": CapitalWord,
                    ".": Word,
                    "%": Roll
                }[content]()
                return element
            except KeyError:
                raise FormatStringError


class Word(Variable):
    def __init__(self):
        super(Word, self).__init__()

    def calculate(self):
        self.entropy_needed = self.wordlist.throws

    def prepare(self):
        self.content = self.wordlist.get(self.entropy)


class CapitalWord(Word):
    def prepare(self):
        super(CapitalWord, self).prepare()
        self.content = self.content.capitalize()


class AllCapsWord(Word):
    def prepare(self):
        super(AllCapsWord, self).prepare()
        self.content = self.content.upper()


class Number(Variable):
    def __init__(self, limit):
        super(Number, self).__init__()
        self.limit = limit

    def calculate(self):
        self.entropy_needed = 0
        while self.wordlist.facets ** self.entropy_needed < self.limit:
            self.entropy_needed += 1
        self.roll_max = (self.wordlist.facets ** self.entropy_needed) - 1

    def prepare(self):
        #TODO: refactor into utility function
        offsets = []
        for throw in self.entropy:
            if 1 <= throw <= self.wordlist.facets:
                offsets.append(throw - 1)
            else:
                err = "throw value {} is out of range"
                raise ValueError(err.format(throw))

        index = 0
        while offsets:
            offset = offsets.pop(0)
            exponent = len(offsets)
            index += offset * (self.wordlist.facets**exponent)

        self.content = str(int(round((index / self.roll_max) * self.limit)))


class Roll(Number):
    def __init__(self):
        super(Roll, self).__init__(None)

    def calculate(self):
        super(Roll, self).calculate()
        self.entropy_needed = 1
        self.limit = self.wordlist.facets - 1
        self.roll_max = self.limit

    def prepare(self):
        super(Roll, self).prepare()
        self.content = str(int(self.content) + 1)


def parse_format(format):
    definition = []

    # define pattern grammar
    variable_ptn = pp.QuotedString("{", endQuoteChar="}")("variable")
    escape_open_ptn = pp.Literal("{{")("escape_open")
    escape_close_ptn = pp.Literal("}}")("escape_close")
    escape_ptn = escape_open_ptn | escape_close_ptn
    literal_ptn = pp.CharsNotIn("{}")("literal")
    element_ptn = escape_ptn | variable_ptn | literal_ptn

    for toks, start, end in element_ptn.leaveWhitespace().scanString(format):
        try:
            definition.append({
                "literal": lambda: Literal(toks[0]),
                "variable": lambda: Variable.create(toks[0]),
                "escape_open": lambda: OpenBrace(),
                "escape_close": lambda: CloseBrace(),
            }[toks.items()[0][0]]())
        except KeyError:
            raise FormatStringError
    return definition
