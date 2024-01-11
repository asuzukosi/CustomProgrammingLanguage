# parser utilities for lox
from enum import Enum, auto
from typing import List
from main import Lox

class TokenType(Enum):
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    COMMA = auto()
    DOT = auto()
    MINUS = auto()
    PLUS = auto()
    SEMICOLON = auto()
    SLASH = auto()
    STAR = auto()
    BANG = auto()
    BANG_EQUALS = auto()
    EQUAL = auto()
    EQUAL_EQUAL = auto()
    GREATER_EQUAL = auto()
    GREATER = auto()
    LESS = auto()
    LESS_EQUAL = auto()
    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()
    AND = auto()
    CLASS = auto()
    OR = auto()
    ELSE = auto()
    FUN = auto()
    FOR = auto()
    IF = auto()
    NIL = auto()
    PRINT = auto()
    RETURN = auto()
    SUPER = auto()
    THIS = auto()
    TRUE = auto()
    VAR = auto()
    WHILE = auto()
    FALSE = auto()
    EOF = auto()



keywordMap = {
    "and": TokenType.AND,
    "class":  TokenType.CLASS,
    "else":   TokenType.ELSE,
    "false":  TokenType.FALSE,
    "for":    TokenType.FOR,
    "fun":    TokenType.FUN,
    "if":     TokenType.IF,
    "nil":    TokenType.NIL,
    "or":     TokenType.OR,
    "print":  TokenType.PRINT,
    "return": TokenType.RETURN,
    "super":  TokenType.SUPER,
    "this":   TokenType.THIS,
    "true":   TokenType.TRUE,
    "var":    TokenType.VAR,
    "while":  TokenType.WHILE
}


class Token:
    def __init__(self, type: TokenType, lexeme: str, literal, line: int):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
    
    def __str__(self) -> str:
        return self.type + " " + self.lexeme + " " + self.literal
    
    
class Scanner:
    def __init__(self, source: str, lox):
        self.source = source
        self.tokens: List[Token] = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.lox = lox
        
    def scanTokens(self):
        while not self.isAtEnd():
            self.start = self.current
            self.scanToken()
        
        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens
    
    def isAtEnd(self):
        return self.current >= len(self.source)
    
    def scanToken(self):
        c = self.advance()
        
        match c:
            case '(':
                self.addToken(TokenType.LEFT_PAREN)
            case ')':
                self.addToken(TokenType.RIGHT_PAREN)
            case '{': 
                self.addToken(TokenType.LEFT_BRACE)
            case '}': 
                self.addToken(TokenType.RIGHT_BRACE)
            case ',': 
                self.addToken(TokenType.COMMA)
            case '.':
                self.addToken(TokenType.DOT)
            case '-': 
                self.addToken(TokenType.MINUS)
            case '+': 
                self.addToken(TokenType.PLUS)
            case ';': 
                self.addToken(TokenType.SEMICOLON)
            case '*': 
                self.addToken(TokenType.STAR)
            case '!':
                self.addToken(TokenType.BANG_EQUALS if self.match('=') else TokenType.BANG)
            case '=':
                self.addToken(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
            case '<':
                self.addToken(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
            case '>':
                self.addToken(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)
            case '/':
                if(self.match('/')):
                    while(self.peek() != '\n' and not self.isAtEnd()):
                        self.advance()
                elif(self.match('*')):
                    while not(self.peek() == '*' and self.peekNext() == '/') and not self.isAtEnd():
                        if(self.advance() == '\n'):
                            self.line += 1
                    
                    self.advance()
                    self.advance()
                else:
                    self.addToken(TokenType.SLASH)
            case ' ':
                pass
            case '\r':
                pass
            case '\t':
                pass
            case '\n':
                self.line += 1
            case '"':
                self.handleString()
            case _:
                if (self.isDigit(c)):
                    self.number()
                elif (self.isAlpha(c)):
                    self.identifier()
                else:
                    self.lox.error(self.line, "Unexpected character")
                
    def isAlpha(self, character):
        if ('a' <= character and character <= 'z') or \
            ('A' <= character and character <= 'Z') or character == '_':
                return True
        return False
    
    def isAlphanumeric(self, character):
        return self.isAlpha(character) or self.isDigit(character)
    
    def identifier(self):
        while(self.isAlphanumeric(self.peek()) and not self.isAtEnd()):
            self.advance()
        
        value = self.source[self.start:self.current]
        self.addToken(keywordMap.get(value, TokenType.IDENTIFIER), value)
                
    def isDigit(self, character):
        if '0' <= character and character <= '9':
            return True
        return False
    
    def number(self):
        while (self.isDigit(self.peek()) and not self.isAtEnd()):
            self.advance()
        
        if self.peek() == ' ' and self.isDigit(self.peekNext()):
            self.advance()
        
        while (self.isDigit(self.peek()) and not self.isAtEnd()):
            self.advance()
            
        self.addToken(TokenType.NUMBER, float(self.source[self.start: self.current]))
        
    def peekNext(self):
        if self.current + 1 <= len(self.source):
            return self.source[self.current + 1]
        return '\0'
            
    def handleString(self):
        while self.peek() != '"' and not self.isAtEnd():
            if(self.peek() == '\n'):
                self.line += 1
            self.advance()
            
        if self.isAtEnd():
            self.lox.error(self.line, "Improperly formatted string")
            return
        self.advance()
        value = self.source[self.start+1: self.current -1]
        self.addToken(TokenType.STRING, value)
    
    
    def peek(self):
        if not self.isAtEnd():
            return self.source[self.current]
        return '\0'
    
    def match(self, pattern):
        if self.isAtEnd():
            return False
        if self.source[self.current] != pattern:
            return False
        
        self.current += 1
        return True

    def addToken(self, token_type:TokenType, literal:str=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))
    
    def advance(self):
        output = self.source[self.current]
        self.current += 1
        return output
    
# def scanTokens(content):
#     # extract the list of valid tokens from content file
#     pass

lox = Lox()
content = ""
with open("CustomLanguage/loxpy/test.lox", "r") as f:
    content = f.read()
scanner = Scanner(content, lox)
tokens = scanner.scanTokens()