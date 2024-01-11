### Learning notes from building an interpreter

#### Language
We would be building the lox programming language this is a simple python like object oriented programming language
We would be building the langugage initially in python, then cpp then rust, we would be benchmarking the performance across the various language implementations and seeing how the performance of the interpreter changes as the implementation language changes. 

The parts of the interpreter to be built are: 
- The Tokenizer = breaks text document into tokens
- The parser = breaks down tokens and groups them
- Build AST = builds an AST using information extracted from the parser
- Create IR = We would be creating an intermediate representation from the AST which would be used for optimization
- Perform logic by parsing operation form the tree = everything up until this point is referred to as the fronted of the interpreter, this point would serve as the beginning of the execution of the backend
- Convert code to optimized code that is to be executed on a virtual machine which runs the programming language

#### Tree walk interpreter
##### Scanning
Scanning takes all the characters from the source file and groups them into related pairs called tokens, these are the meaningful words that make up the language grammer. 
##### Lexemes and Tokens
In this example `var language = 'lox';` we can see that the tokens are var, langeuage, =, lox and ;. Lexical analysis is scanning through the document and grouping them into the smallest number of sequences that mean something. We can bundle lexemes toghether with other useful data to form tokens.
Such useful imformation include
- Token type = Lexemes can be grouped into broad catergories like:
- Literal values = These are numbers and strings that are used in the execution of the program
- Location Informaton = We need to keep track of where our tokens exist, so if an error occurs we can easily point to the location of the tokens existence. 

We can build a complete scanner using regular expressions, but for the purpose of this project, since the focus is on handcrafting we would be traversing through the tokens in the content of the source code manually.
