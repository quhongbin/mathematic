#########栈的四则运算#########
r="1+(1/3)-4"
def StackCalulateToPostfix(expression):
    stack=[]
    result_postfix=[]
    for i in expression:
        if i.isdigit():
            result_postfix.append(i)
        elif len(stack)==0:                 #如果目标栈为空，直接压栈
            stack.append(i)
        elif i in "*/(":                    #如果遍历到乘除和右括号，直接压入栈(stack)
            stack.append(i)
        elif i in ")":                      #如果遍历到左括号，将stack栈中的符号依次弹进
            temp=stack.pop()                #后缀表达式栈result_postfix中
            while temp!="(":                #直至遍历到右括号结束   但此处变量temp依然存在为消除
                result_postfix.append(temp)
                temp=stack.pop()
        elif i in "+-":                     #如果便利到+，-直接压入栈中
            stack.append(i)
    while stack:                            #最后将栈stack中的元素依次从末尾弹进
        result_postfix.append(stack.pop())  #后缀表达式result_postfix栈中
    return result_postfix                   #返回后缀表达式到全局变量中

    print(result_postfix)
    print(stack)

print(StackCalulateToPostfix(r))
def PostfixCalculate(values):
    # num=[]
    # for j in values:
    #     base_opt=["-","+","*","/"]
    #     if j.isdigit():
    #         num.append(j)
    #     if j in base_opt:
    #         res=postfix_calculate_method(num[-2],num[-1],j)
    #         num.append(res)
    # return num
    num=[]
    for j in values:
        base_opt=["-","+","*","/"]
        if j.isdigit():          #如果遍历到数字，直接压入栈num中
            num.append(j)
        elif j in base_opt:      #如果遍历到符号，弹出栈顶和栈顶-1元素进行运算
            num2=num.pop()
            num1=num.pop()
            res=PostfixCalculateMethod(num1,num2,j)
            num.append(res)      #运算完成后，将结果压入栈num中
    return num[0]                #返回结果

def PostfixCalculateMethod(num1,num2,j):
    if j in "+":
        result=float(num1)+float(num2)
    elif j in "-":
        result=float(num1)-float(num2)
    elif j in "*":
        result=float(num1)*float(num2)
    elif j in "/":
        result=float(num1)/float(num2)
    return result
    
            





print(PostfixCalculate(StackCalulateToPostfix(r)))
