# MyPythonInterpreter

MyPythonInterpreter is a simple interpreter written in Python that can execute custom scripting language commands defined in text files.

## Overview

This interpreter is designed to read script files containing custom commands and execute them accordingly. It supports basic functionalities such as variable assignment, input/output operations, conditional statements, loops, function definitions, and function calls.

## Features

- **Variable Assignment:** Assign values to variables using the `assign` command.
- **Input Operations:** Get user input for variables using the `input` and `inputStr` commands.
- **Output Operations:** Print messages or variable values using the `write` command.
- **Arithmetic Operations:** Perform arithmetic operations such as multiplication using the `mult` command.
- **Conditional Statements:** Execute code conditionally based on boolean expressions using the `if` command.
- **Loops:** Execute code repeatedly using the `while` command.
- **Function Definitions:** Define custom functions with parameters using the `def` command.
- **Function Calls:** Call user-defined functions with arguments using the `call` command.

## Usage

To use the interpreter, follow these steps:

1. Write your script in a text file with a `.txt` extension.
2. Write your custom commands in the script file using the supported syntax.
3. Use the `interpret()` method of the `MyPythonInterpreter` class to execute the script file.

## in command line 
'python run_interpreter.py <text.txt>'
