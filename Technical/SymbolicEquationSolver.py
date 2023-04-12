#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 01:17:32 2023

@author: JuxtaR_YCT
"""
import re
import math



# explist=[]
# m=[]
print("Enter the equation in the form of ax^2+bx+c=0 : ")
eqn=input()


checker=r'^([+-]?\d+)x\^2([+-]\d+x)?([+-]\d+)?$'
check=re.match(checker,eqn)

if check:
    a = int(check.group(1))
    b = int(check.group(2).replace("x", "")) if check.group(2) else 0
    c = int(check.group(3)) if check.group(3) else 0
    d=0
    d=float(d)
    
    
    d=b**2-4*a*c
    
    if(d==0):
        root1=0
        root1=float(root1)
        root1=-b/(2*a)
    elif(d<0):
        imaginary=0
        imaginary=float(imaginary)
        real=0
        real=float(real)
        imaginary=(abs(b^2-4*a*c)/(2*a))**0.5
        real=-b/(2*a)
        print("The solutions to the equation are:\n Root-1: " ,real,"+",imaginary,"i")
        



# a=0
# l=eqn.split("+")
# for i in range(len(l)):
#     m.append(l[i].split("-"))
# print(m)

# for i in eqn:
#     explist.append(i)
# print(explist)
# for i in range(len(explist)):
#     if(explist[i]=="^" and explist[i+1]=="2"):
#         if(explist[0].isalpha()==False and explist[0]=="-"):
#             a=explist[1]
#             a=int(a)
#             a=-a
            
#         else:
#             a=explist[0]
#             a=int(a)

            
            

