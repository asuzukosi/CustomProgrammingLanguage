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

One character lookahead is when yo uonly look one character into the future when you are trying to determine the nature of a token. The smaller the number for the character lookahead, the faster the parser runs. Most languages use one or two character lookaheads

Maximal munch in a programming parsers is when two patterns can fit a particular sequence, we go for the longest valid sequence.

Reserved words are identifiers that have been claimed for use in the language. 

After the completion of the scanner, we now have a list of all the tokens from the source file, these tokens hold information such as the token type, literal value, lexeme and line location.  While this is a notable acheivement to be able to use the tokens gathered to reasonably understand our program we need to convert these list of tokens into a higher level data structure which would represent sematic information about our code.  This high levle data structure is the abstract syntax tree, we shall use the tokens gathered from the scanner to contruct our AST, this phase is known as parsing. 

The abstract syntax tree would be a semantic representation for our code. This should be easy for the parser to produce and for the interpreter to consume. 

We are moving up the chomsky's language heirarchy, instead of looking at the language just in the form of regular expression, we are now beginning to consider context-free grammar. At the level of the CFG, each token is an alphabet as we have moved up a layer of abstaction. We are moving from Lexical Grammar to Syntactic Grammar. In programming language design, context-free grammars help you crystalize your language syntax design. They also come as a handy tool for communicating the syntax of your programming language to other language hackers. 

At the very least, both parsers and interpreters would be making use of the AST. 
