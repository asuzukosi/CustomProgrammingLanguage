from typing import List
import sys
from loxparser import scanTokens


class InvalidArgCount(Exception):
    pass

class Lox: 
    hadError = False
    
    def main(self, args: List):
        if len(args) > 1:
            raise InvalidArgCount("Usage: loxpy [script]")        
        elif len(args) == 1:
            self.runFile(args[0])
        else:
            self.runPrompt()
        
    def runFile(self, filename: str):
        # executes single loxpy script
        if (self.hadError):
            sys.exit(65)
            
        content = ""
        with open(filename, "r") as f:
            content = f.read()
        self.execute(content)
    
    def runPrompt(self):
        # runs loxpy interactively by accepting commands and running them
        while True:
            try:
                command = input("> ")
                if len(command) > 0:
                    self.execute(command)
                    self.hadError = False
                else:
                    break
            except EOFError:
                break

    
    def execute(self, content):
        # executes a loxpy script based on the content of the script
        tokens: List = scanTokens(content)
        for t in tokens:
            print(t)
            
    
    def error(self, line, message):
        self.report(line, "", message)
        
    def report(self, line, where, message):
        print("[line " + line + "] Error" + where + ": " + message)
        self.hadError = True
        
        
    
    
if __name__ == "__main__":
    lox = Lox()
    Lox.main(sys.argv[1:])