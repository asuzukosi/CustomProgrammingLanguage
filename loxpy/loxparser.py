# parser utilities for lox
from enum import Enum, auto
from typing import List


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


class Token:
    def __init__(self, type: TokenType, lexeme: str, literal, line: int):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
    
    def __str__(self) -> str:
        return self.type + " " + self.lexeme + " " + self.literal
    
    
class Scanner:
    def __init__(self, source: str):
        self.source = source
        self.tokens: List[Token] = []
        self.start = 0
        self.current = 0
        self.line = 1
        
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
            case _:
                raise Exception("Unhandled token type")
            
            
    def addToken(self, token_type:TokenType, literal:str=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))
    
    def advance(self):
        output = self.source[self.current]
        self.current += 1
        return output
    
def scanTokens(content):
    # extract the list of valid tokens from content file
    pass