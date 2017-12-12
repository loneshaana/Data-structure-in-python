operatorPrecedence={
'(' :0,
')' :0,
'+' :1,
'-' :1,
'*' :2,
'/' :2
}
def postfixConvert(infix):
    stack =[]
    postfix =[]
    for char in infix:
        if char not in operatorPrecedence:
            postfix.append(char)
        else:
            if char =='(':
                stack.append(char)
            elif char == ')':
                while stack[len(stack) -1] != '(':
                    postfix.append(stack.pop())
                stack.pop()

            elif operatorPrecedence[char] > operatorPrecedence[stack[len(stack) - 1]]:
                stack.append(char)
            else:
                while len(stack) != 0:
                    if stack[len(stack) -1] == '(':
                        break
                    postfix.append(stack.pop())
                    stack.append(char)
    while(len(stack) !=0):
        postfix.append(stack.pop())
        return postfix
print postfixConvert("(5+3)*6")
