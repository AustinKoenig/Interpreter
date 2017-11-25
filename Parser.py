# Parser -- HW 5
# Austin Koenig
# Programming Languages

# The parser will recieve a list of tokens and then return an expression tree
# created by the given token list

from Scanner import *

class TreeType:
    ID_NODE, BOOL_NODE, NUM_NODE, OPER_NODE = ["ID", "BOOL", "NUM", "OPER"]

class ExprTreeNode:
    def __init__(self):
        self.layer = 1
        self.nodeType = None
        self.left = None
        self.right = None

class ExprTreeIDNode(ExprTreeNode):
    def __init__(self, _value, _left, _right):
        self.layer = 1
        self.oper = _value
        self.left = _left
        self.right = _right
        self.nodeType = TreeType.ID_NODE

class ExprTreeBoolNode:
    def __init__(self, _value, _left, _right):
        self.layer = 1
        self.value = _value
        self.left = _left
        self.right = _right
        self.nodeType = TreeType.BOOL_NODE

class ExprTreeNumNode:
    def __init__(self, _value, _left, _right):
        self.layer = 1
        self.value = _value
        self.left = _left
        self.right = _right
        self.nodeType = TreeType.NUM_NODE

class ExprTreeOperNode:
    def __init__(self, _value, _left, _right):
        self.layer = 1
        self.value = _value
        self.left = _left
        self.right = _right
        self.nodeType = TreeType.OPER_NODE

class Parser:
    def __init__(self):
        self.currToken = None
        self.currLine = []
        self.tokens = []
        self.cursor = 0;

    def parse(self, _tokens):
        self.tokens = _tokens
        for t in self.tokens: # each element in self.tokens is a list of tokens
            self.currLine = t
            self.currToken = self.currLine[cursor] # currToken is now the first token in the line
            # varTree = self.parseVars() # parse any variables
            # funTree = self.parseFuncs() # parse any functions
            cmdTree = self.parseCMDS() # parse any commands
            if self.currToken != None:
                raise Error("Unconsumed tokens at end of program")

    def parseVars(self):
        while self.currToken == KeywordToken("var"):
            self.parseVar()

    def parseVar(self):
        

    def parseFuncs(self):
        pass

    def parseFunc(self):
        pass

    def parseCMDS(self):
        while self.currToken.type == TokenType.ID:
            self.parseCMD()

    def parseCMD(self):
        L = ExprTreeIDNode(self.currToken.value, None, None)
        self.consumeToken()
        if self.currToken.value == ':=':
            N = ExprTreeOperNode(self.currToken, L, None)
            self.consumeToken()
            R = self.parseExpr()
            N.right = R

    def parseExpr(self):
        L = self.parseSimpleExpr()

    def parseSimpleExpr(self):
        if self.currToken.value == '+' or self.currToken.value == '-':
            temp = self.currToken.value
            self.consumeToken()
            self.parseTerm()
            
    def parseTerm(self):
        L = self.parseFactor()
        self.consumeToken()
        N = None
        if isMulOp(self.currToken):
            N = ExprTreeOperNode(self.currToken.value, L, None)
            self.consumeToken()
            R = parseFactor()

    def parseFactor(self):
        if self.currToken.type == TokenType.INT or self.currToken.type == TokenType.REAL:
            return ExprTreeNumNode(self.currToken.value, None, None)
        elif self.currToken.type == TokenType.BOOL:
            return ExprTreeBoolNode(self.currToken.value, None, None)
        elif self.currToken.type == TokenType.ID:
            return ExprTreeIDNode(self.currToken.value, None, None)
        elif self.currToken.value == 'not':
            pass
        elif self.currToken.value == '(':
            self.consumeToken()
            enode = self.parseExpr()
            self.consumeToken()
            if self.currToken.value != ')':
                raise Exception('Invalid factor -- bad paren use.')
        else:
            raise Exception('Invalid factor.')
            

    def isMulOp(self, token):
        return token.value == '*' or token.value == '/' or token.value == '%' or token.value == 'and'

    def consumeToken(self):
        if self.cursor < len(self.tokens):
            self.cursor += 1
        if self.cursor == len(self.tokens):
            self.currToken = None
        else:
            self.currToken = self.tokens[self.cursor]


if __name__ == '__main__':
    s = Scanner()
    p = Parser()
    prgm = []
    while True:
        try:
            userInput = input("PROMPT [[ ")
            if len(userInput) < 1:
                break
            print(userInput)
            TOKENS = s.scan(userInput)
            prgm.append(TOKENS)
        except(EOFError):
            break

    try:
        tree = p.parse(prgm)
    except(EOFError):
        break































    
