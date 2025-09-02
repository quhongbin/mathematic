import numpy as np
from fractions import Fraction

#class calculate:
#    def __init__(self,angle) -> None:
#        print(f"{Fraction(angle/180)}"+u"\u03C0")
#        print(type(angle))
#calculate(90)

vectors = np.array([[ 3  , 4 ],
                    [ 4  ,-2 ],
                    [-2  , 4 ],
                    [-3  ,-5 ]])     #非0起点的向量，需要加上起点向量
x =np.array([[0, 1, -1, -1],[0, 1, -1, -1]])
print(x[:,1])