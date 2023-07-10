#!/usr/bin/env python3
import re

class Evaluator:
    def __init__(self, string: str):
        self.to_convert = string
        self.stack = []
        self.precedenceTable = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isOperator(self, char: str) -> bool:
        if char in "*+-/^()":
            return True
        return False

    def prefixToInfix(self):
        copy = self.to_convert
        try:
            for char in reversed(copy):
                if not self.isOperator(char):
                    self.stack.append(char)
                else:
                    string = '(' + self.stack.pop() + char + self.stack.pop() + ')'
                    self.stack.append(string)
            return self.stack.pop()
        except:
            self.illegal("input expression has improper syntax.")

    def postfixToInfix(self):
        copy = self.to_convert
        try:
            for char in copy:
                if not self.isOperator(char):
                    self.stack.append(char)
                else:
                    first = self.stack.pop()
                    second = self.stack.pop()
                    string = '(' + second + char + first + ')'
                    self.stack.append(string)
            return self.stack.pop()
        except:
            self.illegal("input expression has improper syntax.")
        
    def illegal(self, errmsg: str):
        raise Exception("Invalid input: " + errmsg)

    def fixPower(self, string: str):
        copy = [c for c in string]
        for i in range(len(copy)):
            if copy[i] == '^':
                copy[i] = '**'
        return ''.join(copy)

    def evaluate(self):
        for char in self.to_convert:
            if not self.isOperator(char) and not char.isdigit():
                self.illegal("input expression contains variables.")

        if self.to_convert[0] not in '()' and self.isOperator(self.to_convert[0]): #prefix
            infix_string = self.fixPower(self.prefixToInfix())
            print(f"Answer: {eval(infix_string):10.5f}")

        elif self.to_convert[-1] not in '()' and self.isOperator(self.to_convert[-1]): #postfix
            infix_string = self.fixPower(self.postfixToInfix())
            print(f"Answer: {eval(infix_string):10.5f}")
            
        else:
            print(f"Answer: {eval(self.fixPower(self.to_convert)):10.5f}")


def load_defaultExpressions() -> list[str]:
    with open('eval_tests.txt', 'r') as file:
        clean_lines: [str] = []
        for line in file: # remove all whitespaces
            cleaned = re.sub(r"\s+", "", line, flags=re.UNICODE)
            clean_lines.append(cleaned.rstrip())

        return clean_lines


def main():
    while True:
        choice = input("\nLoad default expressions? [y/n] -- 'exit' to exit]: ")
        if choice == 'exit':
            return
        elif choice in ['y', 'Y', 'yes', 'Yes']:
            for exp in load_defaultExpressions():
                calcul8r = Evaluator(exp)
                calcul8r.evaluate()
                del calcul8r
        else:
            string = input("\nEnter your expression: ")
            clean_string = re.sub(r"\s+", "", string, flags=re.UNICODE)
            calc = Evaluator(clean_string)
            calc.evaluate()
        


if __name__ == "__main__":
    main()
