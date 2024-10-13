# Cyrus: A Custom Programming Language

 **Overview**
 
Cyrus, our innovative programming language project, stands at the intersection of
simplicity, performance, and versatility. Rooted in the principles of user-friendliness, it
is implemented using Python and features an interpreter built on the newly developed
'Mojo' language. This strategic combination not only leverages the familiarity and ease
of Python but also integrates the robust performance attributes akin to C++ and Rust.
The uniqueness of Cyrus lies in its commitment to providing a unified programming
model, scalable across various levels of abstraction, from scripting languages to logic
programming.


The standout features of Cyrus extend beyond its technical foundations. With a focus
on strong type checking, enhanced memory efficiency, and expedited database access,
Cyrus aims to address the evolving demands of software development. LLVM
compiler and toolchain technologies are used to develop the frontend and backend for
any instruction set architecture in cyrus. LLVM is designed around a
language-independent intermediate representation (IR) that serves as a portable,
high-level assembly language that can be optimized with a variety of transformations
over multiple passes. Cyrus prioritizes community-driven development, fostering
collaboration through an open-source approach, extensive documentation, and a
vibrant ecosystem of libraries and tools. The ultimate goal of Cyrus is to offer
developers a powerful, adaptable, and collaborative language that not only meets
contemporary needs but also evolves alongside the dynamic landscape of
programming language.


**Key Features**

 **DATATYPES**
 
Data types are the classification or categorization of data items. It represents the kind
of value that tells what operations can be performed on a particular data.

  ● Integer: This value is represented by int class. It contains positive or negative
    whole numbers (without fractions or decimals).
   ```bash
   Syntax: int a=10
```
● Float: This value is represented by the float class. It is a real number with a
floating-point representation. It is specified by a decimal point.
```bash
Syntax: float x=2.5
```

● Let: You can reassign new values to a variable declared with let .
```bash
Syntax: let x=10
```

● List: Lists are just like dynamically sized arrays, a list is a collection of things,
enclosed in [ ] and separated by commas.
```bash
Syntax: List = [10, 14]
```

## Relational Operators

| Operator | Description                                         | Syntax   |
|----------|-----------------------------------------------------|----------|
| `>`      | Greater than: True if the left operand is greater than the right | `x > y`  |
| `<`      | Less than: True if the left operand is less than the right   | `x < y`  |
| `==`     | Equal to: True if both operands are equal                   | `x == y` |
| `!=`     | Not equal to: True if operands are not equal              | `x != y` |
| `>=`     | Greater than or equal to: True if the left operand is greater than or equal to the right | `x >= y` |
| `<=`     | Less than or equal to: True if the left operand is less than or equal to the right  | `x <= y` |


## Arithmetic Operators

| Operator | Description                                     | Syntax   |
|----------|-------------------------------------------------|----------|
| `+`      | Addition: adds two operands                     | `x + y`  |
| `-`      | Subtraction: subtracts the second operand from the first | `x - y`  |
| `*`      | Multiplication: multiplies two operands         | `x * y`  |
| `/`      | Division: divides the first operand by the second | `x / y`  |


**CONDITIONAL STATEMENTS**


● IF Statement: The IF statement is the most simple decision-making statement. It
is used to decide whether a certain statement or block of statements will be
executed or not.
```bash
Syntax:
IF<condition>THEN<expression>
```
● IF-ELSE Statement: The ELSE statement is used to specify a block of code to be
executed if the IF condition is false.
```bash
Syntax:
IF<condition>THEN<expression>
ELSE<expression>
```

● ELF Statement: The ELF statement is used to specify a new condition if the first
condition is false.
```bash
Syntax:
IF<condition>THEN<expression>
ELF<condition>THEN<expression>
…
…
ELSE <expression>
```

**LOOPS**

● **FOR Loop** : A for loop in Cyrus is a control flow statement that is used to
repeatedly execute a group of statements as long as the condition is satisfied.
Such a type of statement is also known as an iterative statement.
```bash
Syntax:
 FOR <initial value> RANGE <final value> BY <increment value>
 THEN
 #statements inside the body of loop#

```
```bash
Example: #Print numbers from 1 to 10#
 FOR i = 1 RANGE 11 BY 1 THEN PRINT(i)

```
**WHILE Loop**: It is used to execute a block of statements repeatedly until a given
condition is satisfied. When the condition becomes false, the line immediately after
the loop in the program is executed.

```bash
Syntax:
 initializationStatement
 WHILE(test expression)
 #Loop Statements#
 Updation

```
```bash
Example: int i
 WHILE(i <= 5)
 PRINT("%d\n", i)
 i+1

```
```bash

```

**DESIGN**


   ![design](https://github.com/user-attachments/assets/e5dd5bd7-3c68-4371-bb2c-2dc5e5371cf3)

The diagram shows the process of translating the code "print ""hello" from a high-level
language to machine code. The process can be broken down into the following steps:
1. Tokenizer (lexical analysis): The code is broken down into individual tokens, which
are the smallest units of meaning in the code. In this case, the tokens are "print" and
"hello".
2. Parser: The parser creates an abstract syntax tree (AST), which represents the structure
of the code.
3. Intermediate representation: The AST is then converted to LLVM IR, which is a
lower-level intermediate representation of the code.
4. CPU: At runtime, the LLVM IR is translated to machine code for the specific CPU
architecture.


**Here's a high-level overview of the process:**

Lexer and parser -> AST - > Generate LLVM IR -> Implement language-specific
optimizations -> Apply LLVM's built-in optimizations -> Generate target-specific
machine code -> Test and debug



**DEVELOPMENT PROCESS**

 **Language Design**
 
Language design is a critical aspect of creating a programming language like Cyrus. It
involves defining the syntax, semantics and features of the language to make it
expressive, readable, and efficient for its intended use cases.
 Syntax: The syntax of a programming language defines its structure and rules for
writing code. This includes the arrangement of keywords, operators, punctuation,
and other elements that form valid expressions and statements in the language.
Syntax design aims to strike a balance between simplicity and expressiveness,
making it easy for programmers to write code while allowing for flexibility and
power.


 Semantics: The semantics of a programming language define the meaning of its
syntax. This includes the behaviour of language constructs at runtime, such as how
variables are declared and assigned, how functions are defined and called, and how
control flow statements affect program execution. The semantic design aims to
ensure clarity, consistency, and predictability in the behaviour of the language,
making it easier for programmers to understand and reason about their code.


 Control Structures: Control structures determine the flow of execution in a
program, looping, and subroutine calls. Language design involves defining syntax
and semantics for control flow constructs such as if statements, while loops, for
loops, and function calls. Design choices may include the use of keyword-based
syntax, the placement of conditional expressions, and the handling of loop
termination conditions.

**LEXER**

 Tokenization (Lexical Analysis): The lexer begins by scanning the input source
code character by character and identifying meaningful units called tokens. These
tokens represent individual elements of the language syntax, such as keywords,
identifiers, literals, operators, and punctuation symbols. Tokenization involves
recognizing predefined patterns in the input character stream and classifying them
into different token types based on their syntactic role in the language.


 Regular Expressions or Finite Automata: The lexer uses regular expressions or
finite automata to define patterns for recognizing tokens in the input character
stream. Each regular expression corresponds to a specific token type and describes
the syntactic structure of tokens belonging to that type. The lexer applies these
regular expressions iteratively to match and extract tokens from the input stream,
moving from left to right until it reaches the end of the code.


 Token Classification: As the lexer scans the input character stream, it matches the
input characters against the predefined regular expressions and identifies the tokens
corresponding to those patterns. Each token is assigned a token type, which
represents its syntactic category (e.g., keyword, identifier, literal) and determines
how it will be processed by subsequent stages of the interpretation process.


 Whitespace and Comments: The lexer may also recognize and handle whitespace
characters and comments in the source code. Whitespace characters are typically
ignored by the lexer and discarded, as they do not contribute to the syntactic structure
of the code. Comments are also treated as tokens by the lexer but are usually ignored
or processed separately, depending on the language semantics.


 Error Handling: During tokenization, the lexer may encounter invalid or
unrecognized input characters or sequences that do not match any of the predefined
token patterns. In such cases, the lexer is responsible for reporting lexical errors to
the user, indicating the location and nature of the error, and attempting to recover
from the error to continue tokenizing the remaining code if possible.


**PARSER**


A parser is a fundamental component of an interpreter that analyzes the structure of
source code written in a programming language and produces a data structure known as
an Abstract Syntax Tree (AST). The parser performs syntactic analysis to ensure that
the code follows the grammar rules of the language and transforms the code into a form
that can be further processed by the interpreter.

 Parsing (Syntactic Analysis): Once the source code has been tokenized, the parser
analyzes the sequence of tokens to determine whether it conforms to the grammar 
rules of the programming language. This process, known as parsing or syntactic
analysis, involves constructing a parse tree or AST that represents the hierarchical
structure of the code according to the language grammar.

 Grammar Rules: The parser relies on a formal specification of the language
grammar, which defines the syntactic rules governing the formation of valid
expressions, statements, and other language constructs.

 Parse Tree or Abstract Syntax Tree (AST): The output of the parsing process is
a hierarchical data structure called a parse tree or AST, which represents the
syntactic structure of the code in a more abstract and structured form. In a parse tree,
each node corresponds to a syntactic construct, such as a keyword, operator, or
expression, and is labeled with the corresponding token or production rule. An AST
is a simplified version of the parse tree that abstracts away irrelevant details and
focuses on the essential elements of the code structure, making it easier to analyze
and manipulate during subsequent interpretation stages.

 Error Handling: During parsing, the parser may encounter syntax errors or
inconsistencies in the source code that violate the language grammar. In such cases,
the parser is responsible for reporting meaningful error messages to the user,
indicating the location and nature of the error, and attempting to recover from the
error to continue parsing the remaining code if possible. Error recovery strategies
may include inserting or deleting tokens to synchronize the parser state and resuming
parsing from a known recovery point.


**SYMBOL TABLE**

A symbol table is a data structure used by compilers and interpreters to store information
about the identifiers (such as variables, functions, classes, etc.) defined in a program and
their associated attributes. Symbol tables are essential for managing the scope, visibility,
and semantics of identifiers throughout the interpretation process.

 Identifier Management: Symbol tables serve as repositories for identifiers and
their attributes. Each identifier in the program, such as variables, functions, and
classes, is associated with a symbol table entry. This entry contains information like
the identifier's name, data type, scope (e.g., global, local), visibility (e.g., public,
private), and memory location. Symbol tables organize identifiers based on their
scope, allowing for efficient lookup and management of identifiers within different
contexts.

 Symbol Resolution: During compilation or interpretation, symbol tables are
consulted to resolve references to identifiers in the code. When an identifier is
encountered, the interpreter searches the symbol table to retrieve its attributes. This
process ensures that the identifier refers to a valid entity and helps determine its
properties and behavior within the program. Symbol resolution involves traversing
nested scopes and resolving identifier references based on lexical and contextual
information stored in the symbol tables.

 Error Detection and Type Checking: Symbol tables play a crucial role in error
detection and type checking. They detect issues such as undeclared identifiers,
redeclarations, conflicting types, and scope violations. For example, if a variable is
used without being declared or if a function is called with incorrect arguments, the
symbol table helps identify these errors and provides relevant diagnostic information
to the programmer. Additionally, symbol tables aid in type checking by ensuring
that operations performed on identifiers are compatible with their declared types. By
consulting the symbol table entries, the compiler or interpreter verifies the
correctness of type assignments, expressions, and function calls, helping prevent
type-related errors and ensuring program reliability.




 **RUNTIME SYSTEM**

 
During runtime, LLVM (Low-Level Virtual Machine) plays a crucial role in the
execution of interpreted code. It acts as a just-in-time (JIT) interpreter converting the
intermediate representation (IR) into machine code that can be executed directly by the
CPU. Here's a detailed explanation of how LLVM behaves during runtime:

 IR Execution Engine: The ExecutionEngine is the primary component of LLVM
that manages the runtime environment. It provides an interface for loading modules,
interpreting functions, and executing them. The ExecutionEngine can be configured
to use different code generators, such as JIT or Ahead-of-Time (AOT).

 Optimization: After generating the IR, LLVM applies a series of optimization
passes to improve the performance and efficiency of the code. These optimizations
include common subexpression elimination, dead code elimination, loop 
optimization, and many others. LLVM's optimizer operates on the IR level, allowing
it to perform high-level optimizations that are agnostic to the target architecture.

 Execution and Runtime Support: Once the machine code is generated, LLVM
hands over control to the operating system's runtime environment for execution. This
may include initialization routines, dynamic memory allocation, exception handling,
and other runtime support services provided by the target platform's runtime
libraries.



**Key Learnings**

Through the development of Cyrus, several key insights were gained:

**Code Interpretation**: Understanding the steps involved in processing and interpreting code from tokens to executable actions was crucial.
**Error Handling**: Implementing error-handling mechanisms provided meaningful feedback when users encountered syntax or runtime errors.
**Memory Managemen**t: Developed a foundational understanding of memory allocation and variable scoping within the language’s interpreter.


**Future Improvements**

Several enhancements are planned for Cyrus:

Support for Additional Data Types: Introducing data types such as dictionaries to expand functionality.

Advanced Error Handling and Debugging Tools: Integration of tools like LLVM for improved debugging capabilities.

**LLVM**

   ![llvm](https://github.com/user-attachments/assets/8920487e-8874-405e-a780-ce11881c4a7e)


Low Level Virtual Machine (LLVM) is a set of compiler and toolchain technologies
that can be used to develop a frontend for any programming language and a backend for
any instruction set architecture. LLVM is designed around a language-independent
intermediate representation (IR) that serves as a portable, high-level assembly language
that can be optimized with a variety of transformations over multiple passes.

The LLVM pass manager is responsible for running a series of passes over the LLVM
IR to optimize and analyze the code. The pass manager decides the order in which the
passes are executed and ensures that the passes have access to the necessary data.

The LLVM IR consists of a set of instructions that are used to represent the program's
behaviour. These instructions operate on operands that can be LLVM-level variables,
memory, or constants. The LLVM IR uses the Static Single Assignment (SSA) form,
where each variable is defined exactly once, and each use of a variable is dominated by
that variable's definition.

LLVM optimizations include:

Constant Propagation: This pass propagates constants from global variables,
constants, and other constants that can be derived in the code. This allows LLVM to
simplify instructions and remove unnecessary branches.

Dead Code Elimination (DCE): DCE is a basic block pass that removes instructions
that are never executed. This allows LLVM to eliminate redundant computations and
optimize the generated code further.

Instruction Combining (IC): IC is a function pass that combines multiple instructions
into a single instruction, improving the efficiency of the generated code. This can
involve replacing complex sequences of instructions with simpler instructions that
perform the same operation.

Loop Unrolling: Loop unrolling is a loop pass that duplicates the instructions in the
loop body to reduce the overhead of the loop. This allows LLVM to generate more
efficient code by reducing the overhead of loop control structures.

Function Inlining: Function inlining is a function pass that replaces function calls with
the body of the called function. This allows LLVM to optimize the generated code
further by eliminating the overhead of function calls and improving locality of reference.

Global Variable Optimization (GVN): GVN is a module pass that optimizes global
variables by removing redundant stores and loads. This allows LLVM to generate more
efficient code by removing unnecessary memory accesses.

Performance Optimizations: Focusing on optimizations particularly for handling larger datasets or complex operations efficiently.


**Conclusion**

Cyrus represents a significant step in custom programming language development, emphasizing usability, efficiency, and flexibility. With ongoing improvements planned, it aims to become an even more powerful tool for developers across various domains.
