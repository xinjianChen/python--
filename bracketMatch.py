def checkOut(arg):
    #判断长度是否大于等于2
    length = len(arg)-1
    #判断长度是否为偶数
    if length<1 or length & 1 == 0:
        return False
    #储存括号种类
    leftParenthesis = "("
    rightParenthesis = ")"
    leftBrackets = "["
    rightBrackets = "]"
    leftBrace = "{"
    rightBrace = "}"
    #栈
    stack = []
    while length>=0:
        #栈为空时取最右一个入栈
        if len(stack)==0:
            stack.append(arg[length])
            length -= 1
        #获取栈顶括号和字符串当前括号
        argCur = arg[length]
        stackCur = stack[len(stack)-1]
        #校验，匹配则删除，不匹配则入栈
        if stackCur == rightBrace and argCur == leftBrace:
            stack.pop()
        elif stackCur == rightBrackets and argCur == leftBrackets:
            stack.pop()
        elif stackCur == rightParenthesis and argCur == leftParenthesis:
            stack.pop()
        else:
            stack.append(argCur)
        length -= 1
    #栈为空时匹配正确
    if len(stack)==0:
        return True
    return False
