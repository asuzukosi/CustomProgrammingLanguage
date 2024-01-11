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
        
    def scanTokens(self):
        while not self.isAtEnd():
            start = current
            self.scanToken()
        
        self.tokens.append(Token(TokenType.EOF, "", None, line))
        return self.tokens
            
    
def scanTokens(content):
    # extract the list of valid tokens from content file
    pass