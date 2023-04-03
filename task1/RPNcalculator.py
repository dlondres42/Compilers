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
        tokens = expression.split()
        for token in tokens:
            if self.is_operand(token):
                self.stack.append(float(token))
            else:
                y = self.stack.pop()
                x = self.stack.pop()

                if token == "+":
                    self.stack.append(x + y)
                elif token == "-":
                    self.stack.append(x - y)
                elif token == "*":
                    self.stack.append(x * y)
                elif token == "/":
                    self.stack.append(x / y)
        return self.stack.pop()


with open("task1/Calc1.stk", "r") as file:
    lines = file.readlines()
    entrada = ""
    for line in lines:
        entrada += line.strip() + " "
    print(entrada.strip())

calc = RPNCalculator()
result = calc.evaluate(entrada)
print(result)