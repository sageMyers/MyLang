class MyPythonInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def interpret(self, file_path):
        """
        Interpret the code from a specified file path.

        :param file_path: Path to the file containing the code to interpret.
        """
        try:
            with open(file_path, 'r') as file:
                code = file.read()
                blocks = self.parse_blocks(code)
                for block in blocks:
                    self.execute_block(block)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def parse_blocks(self, code):
        """
        Parse the code into blocks based on indentation.

        :param code: The code to parse.
        :return: List of blocks.
        """
        blocks = []
        current_block = []
        indentation = None  # Variable to store the detected indentation
        lines = code.split('\n')
        line_number = 1
        try:
            for line in lines:
                if line.strip():  # Skip empty lines
                    line_indentation = len(line) - len(line.lstrip())
                    if indentation is None:  # Detect indentation
                        indentation = line_indentation
                    if line_indentation == indentation:  # Check if indentation matches
                        if current_block:
                            blocks.append(current_block)
                        current_block = [line.strip()]
                    elif line_indentation > indentation:
                        current_block.append(line.strip())
                    else:
                        raise IndentationError(f"Incorrect indentation detected at line {line_number}.")
                    line_number += 1
            if current_block:
                blocks.append(current_block)
            return blocks
        except Exception as e:
            print(f"Error: {e}")

    def execute_block(self, block):
        """
        Execute a block of code.

        :param block: The block of code to execute.
        """
        try:
            for line in block:
                print("Executing:", line)  # Print the line before executing
                self.execute_line(line)
        except Exception as e:
            print(f"Error executing block: {e}")

    def execute_line(self, line):
        """
        Execute a single line of code.

        :param line: The line of code to execute.
        """
        try:
            print("Executing line handler:", line)  # Print the handler name
            # Handle assignment statements
            if line.startswith("assign"):
                self.handle_assignment_statement(line.split())
            # Handle function statements
            elif line.startswith("def"):
                self.handle_function_definition(line.split())                
            # Handle function statements
            elif line.startswith("call"):
                self.call_function(line.split())
            # Handle input statements
            elif line.startswith("input"):
                self.handle_input_statement(line.split())
            # Handle inputStr statements
            elif line.startswith("inputStr"):
                self.handle_inputStr_statement(line.split())                    
            # Handle 'mult' statement
            elif line.startswith("mult"):
                self.handle_mult_statement(line.split())
            # Handle 'repeat' statement
            elif line.startswith("repeat"):
                self.handle_repeat_statement(line.split())
            # Handle 'write from list' statement
            elif line.startswith("writeL"):
                self.handle_write_from_list_statement(line.split())
            # Handle 'write reverse' statement
            elif line.startswith("reverse"):
                self.handle_write_reverse_statement(line.split())
            # Handle 'write' statement
            elif line.startswith("write"):
                self.handle_write_statement(line.split())
            # Handle 'while' statement
            elif line.startswith("while"):
                self.handle_while_statement(line.split())
            # Handle variable reference
            elif line.strip().isalpha():
                print(self.variables.get(line.strip(), f"Undefined variable '{line.strip()}'"))
        except Exception as e:
            print(f"Error executing line '{line}': {e}")

    def call_function(self, function_name, args):
        """
        Call a function with the given arguments.

        :param function_name: Name of the function to call.
        :param args: Arguments to pass to the function.
        """
        try:
            if function_name in self.functions:
                function_args = self.functions[function_name]
                if len(args) != len(function_args):
                    raise ValueError(f"Function '{function_name}' expects {len(function_args)} arguments.")
                # Print the name of the function being called
                print(f"Calling function handler: {function_name}")
                # Construct function call with arguments
                function_call = f"{function_name}({', '.join(args)})"
                # Execute the function call
                self.execute_line(function_call)
            else:
                raise ValueError(f"Function '{function_name}' is not defined.")
        except Exception as e:
            print(f"Error calling function '{function_name}': {e}")

    def handle_function_definition(self, tokens):
        """
        Handle function definition command.

        :param tokens: List of tokens from the function definition command.
        """
        try:
            print("Function definition handler:", tokens)  # Print the handler name and tokens
            function_name = tokens[1]
            args = tokens[2:]
            self.functions[function_name] = args
        except Exception as e:
            print(f"Error handling function definition: {e}")

    def handle_mult_statement(self, tokens):
        """
        Handle multiplication statement.

        :param tokens: List of tokens from the multiplication statement.
        """
        try:
            print("Multiplication statement handler:", tokens)  # Print the handler name and tokens
            if len(tokens) >= 3:
                num1 = int(self.variables.get(tokens[1]))
                num2 = int(self.variables.get(tokens[2]))
                result = self.multiply_numbers(num1, num2)
                self.variables[tokens[3]] = result
            else:
                print("Invalid 'mult' statement format")
        except Exception as e:
            print(f"Error handling 'mult' statement: {e}")



    def handle_write_statement(self, tokens):
        """
        Handle write statement.

        :param tokens: List of tokens from the write statement.
        """
        try:
            
            print("Write statement handler:", tokens)  # Print the handler name and tokens
            if len(tokens) > 1:
                content = " ".join(tokens[1:])
                print(content)
            else:
                print("Invalid 'write' statement format")
        except Exception as e:
            print(f"Error handling 'write' statement: {e}")
            
    def handle_write_from_list_statement(self, tokens):
        """
        Handle write statement.

        :param tokens: List of tokens from the write statement.
        """
        try:
            
            # print("Write statement handler:", self.variables(tokens[1])) # Print the handler name and tokens
            if len(tokens) > 1:
                content = self.variables.get(tokens[1])
                print("result: " ,content)
            else:
                print("Invalid 'write' statement format")
        except Exception as e:
            print(f"Error handling 'write' statement: {e}")
    def handle_write_reverse_statement(self, tokens):
        """
        Handle write statement.

        :param tokens: List of tokens from the write statement.
        """
        try:
            
            print("Write statement handler:", tokens)  # Print the handler name and tokens
            if len(tokens) > 1:
                content = self.variables.get(tokens[1])
                reversed_string = content[::-1]
                print(reversed_string)
            else:
                print("Invalid 'write' statement format")
        except Exception as e:
            print(f"Error handling 'write' statement: {e}")
    def handle_assignment_statement(self, tokens):
        """
        Handle variable assignment statement.

        :param tokens: List of tokens from the assignment statement.
        """
        try:
            print("Assignment statement handler:", tokens)  # Print the handler name and tokens
            if len(tokens) >= 3:
                var_name = tokens[1]
                value = int(tokens[2]) if tokens[2].isdigit() else self.variables.get(tokens[2], None)
                if value is not None:
                    self.variables[var_name] = value
                else:
                    raise ValueError(f"Invalid assignment: {tokens[2]} is not a valid value")
            else:
                print("Invalid 'assign' statement format")
        except Exception as e:
            print(f"Error handling assignment statement: {e}")

    def handle_if_statement(self, tokens):
        """
        Handle if statement.

        :param tokens: List of tokens from the if statement.
        """
        try:
            print("If statement handler:", tokens)  # Print the handler name and tokens
            if len(tokens) < 2:
                print("Invalid 'if' statement format")
                return

            condition = " ".join(tokens[1:])
            if if_condition_result := self.evaluate_condition(condition):
                self.execute_if_block(tokens)
        except Exception as e:
            print(f"Error handling 'if' statement: {e}")

    def execute_if_block(self, tokens):
        """
        Execute the block of code within the 'if' statement.

        :param tokens: List of tokens from the if statement.
        """
        try:
            if_index = tokens.index(':')
            if_block_tokens = tokens[if_index + 1:]
            if_block_code = "\n".join(if_block_tokens)
            self.execute_block(self.parse_blocks(if_block_code)[0])
        except Exception as e:
            print(f"Error executing 'if' block: {e}")

    def handle_input_statement(self, tokens):
        """
        Handle input statement.

        :param tokens: List of tokens from the input statement.
        """
        if len(tokens) >= 2:
            var_name = tokens[1]
            user_input = input(f"Enter value for {var_name}: ")
            self.variables[var_name] = int(user_input) if user_input.isdigit() else user_input
        else:
            print("Invalid 'input' statement format")

    def handle_inputStr_statement(self, tokens):
        """
        Handle inputStr statement.

        :param tokens: List of tokens from the input statement.
        """
        if len(tokens) >= 2:
            var_name = tokens[1]
            self.variables[var_name] = input(f"Enter value for {var_name}: ")
            print("String:", var_name, "=", self.variables[var_name])
        else:
            print("Invalid 'input' statement format")

    def handle_while_statement(self, tokens):
        """
        Handle while loop statement.

        :param tokens: List of tokens from the while loop statement.
        """
        try:
            print("While statement handler:", tokens)  # Print the handler name and tokens
            if len(tokens) < 2:
                print("Invalid 'while' statement format")
                return

            condition = tokens[2]
         

            while self.evaluate_condition(condition, tokens):
                print(self.variables.get(tokens[5], 'Key not found'))
                self.variables[tokens[1]] = self.variables.get(tokens[1], 0) + int(tokens[4])
        except Exception as e:
            print(f"Error handling 'while' statement: {e}")

    def evaluate_condition(self, condition, tokens):
        """
        Evaluate the condition for a while loop.

        :param condition: Condition to evaluate.
        :return: Boolean value of the condition.
        """
        try:
            # Remove any spaces in the condition
            condition = condition.replace(" ", "")

            # Check if the condition contains a comparison operator
            if '<' in condition:
                return self.variables.get(tokens[1], 0) < self.variables.get(tokens[3], 0)
            elif '>' in condition:
                return self.variables.get(tokens[1], 0) > self.variables.get(tokens[3], 0)
            elif '==' in condition:
                return self.variables.get(tokens[1], 0) == self.variables.get(tokens[3], 0)
            elif '<=' in condition:
                return self.variables.get(tokens[1], 0) <= self.variables.get(tokens[3], 0)
            elif '>=' in condition:
                return self.variables.get(tokens[1], 0) >= self.variables.get(tokens[3], 0)
            else:
                # If no comparison operator is found, check if the variable exists
                return condition in self.variables
        except Exception as e:
            print(f"Error evaluating condition: {e}")
            return False

    @staticmethod
    def multiply_numbers(num1, num2):
        """
        Static method to perform multiplication.

        :param num1: First number.
        :param num2: Second number.
        :return: Result of num1 * num2.
        """
        try:
            return num1 * num2
        except Exception as e:
            print(f"Error multiplying numbers: {e}")
            return None

    
