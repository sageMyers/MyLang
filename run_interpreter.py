import sys

from Interpreter import MyPythonInterpreter

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_interpreter.py <file_path>")
        return

    file_path = sys.argv[1]
    interpreter = MyPythonInterpreter()
    interpreter.interpret(file_path)

if __name__ == "__main__":
    main()
