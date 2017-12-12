class stack:
    def __init__(self):
        self.items =[]

    def push(self,item):
        pushed = self.items.append(item)


    def pop(self):
        popped = self.items.pop()
        return popped

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []


def postFixEvel(postfixexpr):
    tokenlist = str(postfixexpr)
    operandstack = stack()
    for token in tokenlist:
        if token in '0123456789':
            operandstack.push(token)
        else:
            op2 = int(operandstack.pop())
            op1 = int(operandstack.pop())
            result = doMath(token ,op1,op2)
            operandstack.push(result)
    return operandstack.pop()

def doMath(operator ,operand1,operand2):
    if operator == '*':
        return operand1 * operand2
    elif operator == '+':
        return operand1 + operand2
    elif operator == '/':
        return operand1 // operand2
    else:
        return operand1 - operand2

print(postFixEvel("123*+5-"))
