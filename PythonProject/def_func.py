import numpy as np
from fractions import Fraction

class calculate:
    def __init__(self,angle) -> None:
        print(f"{Fraction(angle/180)}"+u"\u03C0")
        print(type(angle))
calculate(90)
