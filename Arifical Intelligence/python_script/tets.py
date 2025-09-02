"""
File: tets.py
Autor: Qu Hongbin
Date: 2025-08-13
description: 
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rcParams
from contextlib import contextmanager
import os

FILENAME = os.path.basename(__file__)
DIROFFILE = os.path.dirname(__file__)

@contextmanager
def change_directory(new_path):
    original_path = os.getcwd()
    try:
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        os.chdir(new_path)
        yield original_path
    finally:
        os.chdir(original_path)

# 设置中文字体支持
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False


with change_directory(f"{DIROFFILE}/images/{FILENAME}") as original_path:
    # save the pictures or videos in the ....../Arifical Intelligence/images/{FILENAME}/{FILENAME.postfix}
    plt.savefig(f"{FILENAME}.png")