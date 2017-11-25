# Scanner -- HW 1
# Austin Koenig
# Programming Languages


# Tokens:

## IDENTIFIER = (a‐z|A‐Z)(a‐z|A‐Z|0‐9)*
## BOOLEAN = #t | #f
## INTEGER = (0‐9)+
## REAL = (0‐9)+\.(0‐9)* | (0‐9)*\.(0‐9)+
## PUNCTUATION = \( | \) | { | } | , | \+ | ‐ | \* | / | %
##            | := | != | < | > | <= | >= | ;
## KEYWORD = var | fun | if | else | return
##        | read | write | not | or | and


# pseudo enum with class for token types
class TokenType:
    ID, BOOL, INT, REAL, PUNCT, KW, ERR = ["ID", "BOOL", "INT", "REAL", "PUNCT", "KW", "ERR"]

# token class
class Token:
    def __init__(self):
        self.type = 'none'
        self.value = 'default'
        
    def tprint(self):
        print("Type: " + self.type)
        print("Value: " + str(self.value))
        print("\n")


class IdentifierToken(Token):
    def __init__(self, value):
        self.value = value
        self.type = TokenType.ID

class BooleanToken(Token):
    def __init__(self, value):
        self.value = value
        self.type = TokenType.BOOL

class IntegerToken(Token):
    def __init__(self, value):
        self.value = value
        self.type = TokenType.INT

class RealToken(Token):
    def __init__(self, value):
        self.value = value
        self.type = TokenType.REAL

class PunctuationToken(Token):
    def __init__(self, value):
        self.value = value
        self.type = TokenType.PUNCT

class KeywordToken(Token):
    def __init__(self, value):
        self.value = value
        self.type = TokenType.KW

class ErrorToken(Token):
    def __init__(self, value):
        self.value = value
        self.type = TokenType.ERR

class Error(Exception):
    pass

class BadNumber(Error):
    def __init__(self, message):
        self.message = message

class BadPunct(Error):
    def __init__(self, message):
        self.message = message

class BadBool(Error):
    def __init__(self, message):
        self.message = message
        
class Scanner:
    def __init__(self):
        self.cursor = 0
        self.eol = False # end of line
        self.next_char = ''
        self.line = ""
        self.tokens = []

    def isWhiteSpace(self, c):
        return ((c == ' ') or (c == '\t') or (c == '\n'))
        

    def isDigit(self, c):
        return ((c >= '0') and (c <= '9'))


    def isAlpha(self, c):
        return (((c >= 'a') and (c <= 'z')) or ((c >= 'A') and (c <= 'Z')))


    def isalpha(self, c):
        return ((c >= 'a') and (c <= 'z'))


    def isDecimal(self, c):
        return (c == '.')


    def isBoolHash(self, c):
        return (c == '#')


    def isBool(self, c):
        return ((c == 't') or (c == 'f'))


    def isPunct(self, c):
        return ((c == '(') or (c == ')') or (c == '{') or (c == '}') or (c == ',') or
                (c == '+') or (c == '-') or (c == '*') or (c == '/') or (c == '%') or
                (c == ':') or (c == '!') or (c == '<') or (c == '>'))


    def checkId(self):
        temp = ''
        temp += self.next_char
        self.safeAdvance()
        while (self.isalpha(self.next_char) or self.isAlpha(self.next_char) or self.isDigit(self.next_char)) and not self.eol:
            temp += self.next_char
            self.safeAdvance()
        return IdentifierToken(temp)


    def checkKeyword(self):
        if self.next_char == 'a':
            if self.line[self.cursor+1] == 'n' and self.line[self.cursor+2] == 'd':
                self.safeAdvance() # I know, but bear with me
                self.safeAdvance()
                self.safeAdvance()
                return KeywordToken('and')
        elif self.next_char == 'e':
            if self.line[self.cursor+1] == 'l' and self.line[self.cursor+2] == 's' and self.line[self.cursor+3] == 'e':
                self.safeAdvance()
                self.safeAdvance()
                self.safeAdvance()
                self.safeAdvance()
                return KeywordToken('else')
        elif self.next_char == 'f':
            if self.line[self.cursor+1] == 'u' and self.line[self.cursor+2] == 'n':
                self.safeAdvance()
                self.safeAdvance()
                self.safeAdvance()
                return KeywordToken('fun')
        elif self.next_char == 'i':
            if self.line[self.cursor+1] == 'f':
                self.safeAdvance()
                self.safeAdvance()
                return KeywordToken('if')
        elif self.next_char == 'n':
            if self.line[self.cursor+1] == 'o' and self.line[self.cursor+2] == 't':
                self.safeAdvance()
                self.safeAdvance()
                self.safeAdvance()
                return KeywordToken('not')
        elif self.next_char == 'o':
            if self.line[self.cursor+1] == 'r':
                self.safeAdvance()
                self.safeAdvance()
                return KeywordToken('or')
        elif self.next_char == 'r':
            if self.line[self.cursor+1] == 'e' and self.line[self.cursor+2] == 'a' and self.line[self.cursor+3] == 'd':
                self.safeAdvance()
                self.safeAdvance()
                self.safeAdvance()
                self.safeAdvance()
                return KeywordToken('read')
            elif self.line[self.cursor+1] == 'e' and self.line[self.cursor+2] == 't' and self.line[self.cursor+3] == 'u' and self.line[self.cursor+4] == 'r' and self.line[self.cursor+5] == 'n':
                self.safeAdvance()
                self.safeAdvance()
                self.safeAdvance()
                self.safeAdvance()
                self.safeAdvance()
                return KeywordToken('return')
        elif self.next_char == 'v':
            if self.line[self.cursor+1] == 'a' and self.line[self.cursor+2] == 'r':
                self.safeAdvance()
                self.safeAdvance()
                self.safeAdvance()
                return KeywordToken('var')
        elif self.next_char == 'w':
            if self.line[self.cursor+1] == 'r' and self.line[self.cursor+2] == 'i' and self.line[self.cursor+3] == 't' and self.line[self.cursor+4] == 'e':
                self.safeAdvance()
                self.safeAdvance()
                self.safeAdvance()
                self.safeAdvance()
                self.safeAdvance()
                return KeywordToken('write')
        return -1


    def checkNumber(self):
        foundDigit = False
        whole = 0.0
        frac = 0.0
        fracMult = 0.1
        pastDecimal = False
        
        while (not self.eol) and (self.isDigit(self.next_char) or self.isDecimal(self.next_char)):
            if self.isDecimal(self.next_char):
                if pastDecimal:
                    raise BadNumber('Poorly formed number -- multiple decimal points')
                    return ErrorToken('BadNumber')
                pastDecimal = True
            elif self.isDigit(self.next_char):
                foundDigit = True
                if not pastDecimal:
                    whole = whole*10 + (ord(self.next_char)-ord('0'))
                else:
                    frac = frac + (ord(self.next_char)-ord('0'))*fracMult
                    fracMult = fracMult/10.0
            self.safeAdvance()
            
        if not foundDigit:
            raise BadNumber('Poorly formed number -- decimal point with no digits')
            return ErrorToken('BadNumber')
        
        if not pastDecimal:
            return IntegerToken(int(whole))
        return RealToken(whole+frac)


    def checkPunct(self):
        if self.next_char == ':':
            if self.line[self.cursor+1] == '=':
                self.safeAdvance()
                return PunctuationToken(':=')
            else:
                raise BadPunct('Bad punctuation -- invalid character: :' + self.next_char)
                return ErrorToken('BadPunct')
        elif self.next_char == '!':
            if self.line[self.cursor+1] == '=':
                self.safeAdvance()
                return PunctuationToken('!=')
            else:
                raise BadPunct('Bad punctuation -- invalid character: !' + self.next_char)
                return ErrorToken('BadPunct')
        elif self.next_char == '<':
            if self.line[self.cursor+1] == '=':
                self.safeAdvance()
                return PunctuationToken('<=')
            return PunctuationToken('<')
        elif self.next_char == '>':
            if self.line[self.cursor+1] == '=':
                self.safeAdvance()
                return PunctuationToken('>=')
            return PunctuationToken('>')
        return PunctuationToken(self.next_char)


    def safeAdvance(self):
        self.cursor += 1
        if self.cursor >= len(self.line):
            self.eol = True
        else: self.next_char = self.line[self.cursor]


    def skipWhiteSpace(self):
        while (not self.eol) and self.isWhiteSpace(self.next_char):
            self.safeAdvance()


    def getNextToken(self):
        token = None
        self.skipWhiteSpace()
        if self.eol:
            token = None
        elif self.isalpha(self.next_char) or self.isAlpha(self.next_char):
            token = self.checkKeyword()
            if token == -1:
                token = self.checkId()
        elif self.isDecimal(self.next_char) or self.isDigit(self.next_char):
            token = self.checkNumber()
        elif self.isPunct(self.next_char):
            token = self.checkPunct()
            self.safeAdvance()
        elif self.isBoolHash(self.next_char):
            if self.isBool(self.line[self.cursor+1]):
                token = BooleanToken('#'+self.line[self.cursor+1])
                self.safeAdvance()
                self.safeAdvance()
            else:
                raise BadBool('Bad boolean value -- invalid boolean value: ' + self.next_char)
                return ErrorToken('BadBool')
        return token


    def scan(self, l):
        self.tokens = []
        
        self.line = l
        self.eol = False
        self.cursor = -1
        self.safeAdvance()
        token = Token()
        
        while token != None:
            token = self.getNextToken()
            if token != None:
                self.tokens.append(token)
                token.tprint()
        return self.tokens


if __name__ == "__main__":
    s = Scanner()
    while True:
        try:
            userInput = input("CODE: ")
            if len(userInput) < 1:
                break
            print(userInput+"\n")
            TOKEN_LIST = s.scan(userInput)
        except(EOFError):
            break
        except(BadBool):
            print('Bad boolean value')
        except(BadNumber):
            print('Bad number')
        except(BadPunct):
            print('Bad punctuation')








































            
