#########角度和弧度的转换#########

import numpy as np
from fractions import Fraction
class calculate:
    def get_radian(angle):
        print(f"{Fraction(angle/180)}"+u"\u03C0")   #pi符号的unicode码为03C0
    def get_angle(radian):
        print(f"{Fraction(180*radian)}"+u"\u00B0")  #度数符号的unicode码为00B0
    def __init__(self,temp):
        if isinstance(temp,str):    #判断输入的类型是不是字符
            input_tuple=tuple(temp)
            if input_tuple[-1]=="i" and input_tuple[-2]=="p" and input_tuple[1] == "/": #判断输入的弧度制格式是否正确
                print(f"{Fraction(180*int(input_tuple[0])/int(input_tuple[2]))}"+u"\u00B0")
            elif temp.isdigit():    #判断输入是否全为数字
                temp=int(temp)  #将输入的字符串转换为数字（可优化）
                calculate.get_radian(temp)  
            elif input_tuple[1] != "/":
                print(f"请输入以/表示的分数(如:1/2)")
            else:
                print("请输入以字符pi结尾的弧度制值!")

print(calculate(input(f"请输入要转换的数值(角度直接输入数字,弧度的输入(如:1/2pi):)")))

# i="1/2pi"
# ii=list(i)
# print(ii[0:-2])
