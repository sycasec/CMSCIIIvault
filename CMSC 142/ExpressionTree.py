import re

class InputError(RuntimeError):
    def __init__(self, *arg):
        self.args = arg
    def __str__(self):
        return f'{self.args[0]}'

def a(x,y): return x+y
def s(x,y): return x-y
def m(x,y): return x*y
def d(x,y): return x/y
def p(x,y): return x**y

class Evaluator:
    def __init__(self, string: str):
        self.to_convert = string
        self.stack = []
        self.precedenceTable = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.evals = {'+': a, '-': s, '*': m, '/': d, '^': p}


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


    def infixToPostfix(self, string=None, strict=False):
        copy = string if string else self.to_convert
        if isinstance(copy, str):
            copy = list(copy)
        out = []

        for i in range(len(copy)):
            if isinstance(copy[i], int) and not self.isOperator(str(copy[i])):
                out.append(copy[i])
            
            elif copy[i] == '(':
                self.stack.append(copy[i])
            
            elif copy[i] == ')':
                while len(self.stack) > 0 and self.stack[-1] != '(':
                    out.append(self.stack.pop())
                
                if len(self.stack) > 0 and self.stack[-1] != '(':
                    self.illegal("unmatched closing parenthesis")
                else:
                    self.stack.pop() 
            else:
                while (len(self.stack) > 0 and self.lessThan(copy[i], self.stack[-1], (copy[i] != "^" if strict else False))):
                    out.append(self.stack.pop())
                self.stack.append(copy[i])

        
        while len(self.stack) > 0:
            out.append(self.stack.pop())
        return out 
      
    
    def clean_negatives(self, string:str):
        cp = list(string)
        for i in range(len(cp)-1):
            if cp[i].isdigit():
                cp[i] = int(cp[i])
            if cp[i] == '-' and cp[i+1].isdigit():
                cp[i+1] = -int(cp[i+1])
                del cp[i]

        return cp

    def infixToPrefix(self, string=None):
        copy = string if string else self.to_convert
        
        copyList = [c for c in copy] 
        copyList.reverse() 
        for index in range(len(copyList)):
            if copyList[index] == '(':
                copyList[index] = ')'
            elif copyList[index] == ')':
                copyList[index] = '('
        return reversed(self.infixToPostfix(copyList, True))
        
    def validExpression(self, string):
        for i in range(len(string)-1):
            if string[i] in '*+-/^' and string[i+1] in '*+-/^':
                return False
            if not self.isOperator(string[i]) and not self.isOperator(string[i+1]):
                return False
        return True
        
    def illegal(self, errmsg: str):
        raise InputError("Invalid input: " + errmsg)
     

    def validExpression(self, string):
        for i in range(len(string)-1):
            if string[i] in '*+-/^' and string[i+1] in '*+-/^':
                return False 
        return True    

    def checkParens(self, string):
        pc = 0
        for i in range(len(string)):
            if string[i] == '(':
                pc += 1
            elif string[i] == ')':
                pc -= 1
            
            if pc < 0:
                return False

        if pc != 0:
            return False
        return True

    def postfix_eval(self, string:str):
        s = []
        for c in string:
            if isinstance(c, str) and self.isOperator(c):
                so = s.pop()
                fo = s.pop()
                s.append(self.evals[c](fo,so))
            else:
                s.append(int(c))

        if len(s) > 1:
            self.illegal("evaluation error. stack contains multiple values with no operation to resolve.")
        return s[0]

    def evaluate(self):
        for char in self.to_convert:
            if not self.isOperator(char) and not char.isdigit():
                self.illegal("input expression contains variables or symbols")
        
        if not self.validExpression(self.to_convert): self.illegal("expression contains consecutive operators.")
        if not self.checkParens(self.to_convert): self.illegal("expression has unmatched parenthesis.")

        try: 
            copy = self.clean_negatives(self.to_convert)
            postfix = self.infixToPostfix(copy)
            prefix = self.infixToPrefix(copy)
            print(*prefix, sep=' ')
            print(*postfix, sep=' ')
            print(self.postfix_eval(postfix))  

        except InputError as e:
            print(e)



def main():
    string = input()
    clean_string = re.sub(r"\s+", "", string, flags=re.UNICODE)
    e = Evaluator(clean_string)
    e.evaluate()
        


if __name__ == "__main__":
    main()
