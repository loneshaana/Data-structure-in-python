class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def PoP(self):
        return self.items.pop()

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        return None

    def __str__(self):
        return str(self.items)

def infixToPostfix(infixexpr):
    import string
    prec={}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    opstack =stack()
    postfixlist = []
    for item in infixexpr:
        if item in 'QWERTYUIOPLKJHGFDSAZXCVBNM' or item in '1234567890':
            postfixlist.append(item)
        elif item == '(':
            opstack.push(item)

        elif item == ')':
            getToken = opstack.PoP()

            while getToken != '(':
                postfixlist.append(getToken)
                getToken = opstack.PoP()
        else:
            while True:
                peekoperator = opstack.peek()
                if peekoperator != None:
                    if peekoperator in '-+/*' :
                        #check if peek operator has high precedence as current token
                        if prec[peekoperator] >= prec[item]:
                            postfixlist.append(opstack.PoP())
                        else:
                            break
                    else:
                        break
                else:
                    break
            opstack.push(item)
    while not opstack.isEmpty():
        postfixlist.append(opstack.PoP())

    return ''.join(postfixlist)
print(infixToPostfix("(A+B)*C-(D-E)*(F+G)"))
