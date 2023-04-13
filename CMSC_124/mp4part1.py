#!/usr/bin/env python3

class Converter:
    def __init__(self, string: str):
        self.to_convert = string
        self.stack = []
        self.precedenceTable = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def lessThan(self, operator: str, compared: str, strict=False) -> bool:
        try:
            x = self.precedenceTable[operator]
            y = self.precedenceTable[compared]

            if strict:
                if x < y:
                    return True
                return False
            else:
                if x <= y:
                    return True
                return False
        except KeyError:
            return False

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
            print("input expression does not qualify for proper syntax.")

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
            print("input expression does not qualify for proper syntax.")

    def infixToPostfix(self, string=None, strict=False):
        copy = string if string else self.to_convert
        out = []

        for char in copy:
            if not self.isOperator(char):
                out.append(char)
            
            elif char == '(':
                self.stack.append(char)
            
            elif char == ')':
                while len(self.stack) > 0 and self.stack[-1] != '(':
                    out.append(self.stack.pop())
                
                if len(self.stack) > 0 and self.stack[-1] != '(':
                    self.illegal("unmatched closing parenthesis")
                else:
                    self.stack.pop()

            else:
                while (len(self.stack) > 0 and self.lessThan(char, self.stack[-1], (char != "^" if strict else False))):
                    out.append(self.stack.pop())
                self.stack.append(char)

        
        while len(self.stack) > 0:
            out.append(self.stack.pop())
        return ''.join(out)
      
    def infixToPrefix(self, string=None):
        copy = string if string else self.to_convert
        
        copyList = [char for char in copy]
        copyList.reverse() 
        for index in range(len(copyList)):
            if copyList[index] == '(':
                copyList[index] = ')'
            elif copyList[index] == ')':
                copyList[index] = '('
        
        return ''.join(reversed(self.infixToPostfix(''.join(copyList), True)))
        
    def illegal(self, errmsg: str):
        raise Exception("Invalid input: " + errmsg)

    def alchemy(self):
        print(f"\nbase notation: {self.to_convert}")
        if self.to_convert[0] not in '()' and self.isOperator(self.to_convert[0]): #prefix
            temp = self.prefixToInfix()
            print(f"infix notation: {temp}")
            print(f"postfix notation: {self.infixToPostfix(temp)}")
        elif self.to_convert[-1] not in '()' and self.isOperator(self.to_convert[-1]): #postfix
            temp = self.postfixToInfix()
            print(f"infix notation: {temp}")
            print(f"prefix notation: {self.infixToPrefix(temp)}")
        else:
            base_copy = self.to_convert
            print(f"prefix notation: {self.infixToPrefix()}")
            print(f"postfix notation: {self.infixToPostfix(base_copy)}")

def load_table() -> [[str, str, str]]:
    table = []
    with open('table.txt', 'r') as file:
        for line in file:
            table.append(line.rstrip().split())
    return table

def main():
    while True:
        table = load_table()
        choice = input("\n(1) Load basic infix\n(2) Load basic prefix\n(3) Load basic postfix\n(4) enter custom expression\n(5) exit\n> ")
        if choice == '5':
            return
        elif choice in '123':
            for exp in [row[int(choice)-1] for row in table]:
                soil = Converter(exp)
                soil.alchemy()
                del soil
        elif choice == '4':
            string = input("\nEnter your expression: ")
            chalk = Converter(string)
            chalk.alchemy()

        else: print("\ninput error.\n")
        


if __name__ == "__main__":
    main()
