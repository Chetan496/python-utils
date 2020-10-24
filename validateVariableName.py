import sys


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return "Type: %s, Value: %s " % (self.type, self.value)


class Lexer:
    def __init__(self, text):
        self.text = text
        self.currIndex = 0

    def isEofReached(self):
        return self.currIndex >= len(self.text)

    def getCurrToken(self):
        token = None
        if self.isEofReached():
            token = Token("EOF", None)
            return token

        currTokenVal = self.text[self.currIndex]
        if currTokenVal.isalpha():
            token = Token("ALPHABET", currTokenVal)
            return token
        elif currTokenVal.isdigit():
            token = Token("DIGIT", currTokenVal)
            return token
        elif currTokenVal.__eq__("_"):
            token = Token("UNDERSCORE", currTokenVal)
            return token
        else:
            raise ValueError(
                "unexpected  char %c in variable name" % currTokenVal)

    def consumeCurrToken(self):
        currToken = self.getCurrToken()
        if not currToken.type.__eq__("EOF"):
            self.currIndex = self.currIndex + 1
        return currToken

    def consumeCurrTokenOnMatch(self, expectedTokenType):
        currToken = self.getCurrToken()
        if currToken.type.__eq__(expectedTokenType):
            return self.consumeCurrToken()
        else:
            return None


def main():
    if len(sys.argv) < 2:
        raise ValueError('please pass the variable name to validate')

    varNameToValidate = sys.argv[1]
    validateIfValidName(varNameToValidate)


def validateIfValidName(varNameToValidate):
    print("validating variable name: %s " % varNameToValidate)
    lexer = Lexer(varNameToValidate)
    consumedToken = lexer.consumeCurrTokenOnMatch("ALPHABET")
    if consumedToken is None:
        raise ValueError("Variable names should start with an alphabet")
    print("first token is %s " % consumedToken)
    try:
        while lexer.getCurrToken().type != "EOF":
            currToken = lexer.consumeCurrToken()
            print("curr token is %s " % currToken)
    except Exception as e:
        print(e)

    print("Variable name is valid")


if __name__ == "__main__":
    main()
