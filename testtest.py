# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:57:58 2020

@author: Administrator
"""
from utils.datasets import letterbox
import cv2

path = "C:/Users/Administrator/Google Drive (jxu33689@gmail.com)/Colab Notebooks/coin/coinimg.txt"
imginfo = "../coin/imginfo.txt"
info = ""
ratio75 = []

with open(path, 'r') as fr:
    for l in fr.readlines():
        if l != "":
            print("*"*50)
            info = info + "*" * 50 + "\n"
            l = l.rstrip()
            print("l: ", l)
            info = info + "l: " + l + "\n"
            img = cv2.imread(l)
            print("img size: ", img.shape)
            if img.shape[0]/img.shape[1] in [4/3]:
                print("The L: ", l)
                ratio75.append(l)
            info = info + "img size: " + str(img.shape) + "\n"
            img, ratio, (dw,dh) = letterbox(img)
            print("ratio: ", ratio)
            info = info + "ratio: " + str(ratio) + "\n"
            print("(dw, dh): ", dw, dh)
            info = info + "(dw, dh): " + str(dw) + ", " + str(dh) + "\n"
            print("resized img size: ", img.shape)
            info = info + "resized img size: " + str(img.shape) + "\n"
            print("*"*50)
            info = info + "*" * 50 + "\n"
            if dw < 0 or dh < 0:
                break
    #        cv2.imshow("img", img)
    #        cv2.waitKey(0)

with open(imginfo, 'w') as fw:
    fw.write(info)

print("ratio75: ", ratio75)
print("Number of ratio: ", len(ratio75))
            