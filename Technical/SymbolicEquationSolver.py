#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 01:17:32 2023

@author: JuxtaR_YCT
"""
explist=[]
print("Enter the equation: ")
eqn=input()
a=0
for i in eqn:
    explist.append(i)
print(explist)
for i in range(len(explist)):
    if(explist[i]=="^" and explist[i+1]=="2"):
        if(explist[0].isalpha()==False and explist[0]=="-"):
            a=explist[1]
            a=int(a)
            a=-a
        else:
            a=explist[0]
            a=int(a)
