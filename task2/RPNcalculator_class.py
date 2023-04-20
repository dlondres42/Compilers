from enum import Enum

class TokenType(Enum):
    NUM = 1
    PLUS = 2
    MINUS = 3
    TIMES = 4
    DIVIDE = 5

class Token:
    def __init__(self, token_type, lexeme):
        self.type = token_type
        self.lexeme = lexeme

class RPNCalculator:
    def __init__(self):
        self.stack = []

    def is_operand(self, op):
        try:
            float(op)
            return True
        except ValueError:
            return False

    def evaluate(self, expression):
        tokens = self.scan(expression)
        for token in tokens:
            if token.type == TokenType.NUM:
                self.stack.append(float(token.lexeme))
            else:
                y = self.stack.pop()
                x = self.stack.pop()

                if token.type == TokenType.PLUS:
                    self.stack.append(x + y)
                elif token.type == TokenType.MINUS:
                    self.stack.append(x - y)
                elif token.type == TokenType.TIMES:
                    self.stack.append(x * y)
                elif token.type == TokenType.DIVIDE:
                    self.stack.append(x / y)
        return self.stack.pop()

    def scan(self, expression):
        tokens = []
        for lexeme in expression.split():
            if self.is_operand(lexeme):
                tokens.append(Token(TokenType.NUM, lexeme))
            elif lexeme == "+":
                tokens.append(Token(TokenType.PLUS, lexeme))
            elif lexeme == "-":
                tokens.append(Token(TokenType.MINUS, lexeme))
            elif lexeme == "*":
                tokens.append(Token(TokenType.TIMES, lexeme))
            elif lexeme == "/":
                tokens.append(Token(TokenType.DIVIDE, lexeme))
            else:
                raise ValueError(f"Unexpected character: {lexeme}")
        return tokens


with open("task2/Calc2.stk", "r") as file:
    lines = file.readlines()
    entrada = ""
    for line in lines:
        entrada += line.strip() + " "
    print(entrada.strip())

calc = RPNCalculator()
tokens = calc.scan(entrada)
for token in tokens:
    print(f"Token [type={token.type.name}, lexeme={token.lexeme}]")
result = calc.evaluate(entrada)
print(result)