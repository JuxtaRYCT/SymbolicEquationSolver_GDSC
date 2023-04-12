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
print("Enter the quadratic equation in the form of ax^2+bx+c=0 : ")
eqn=input()

checker=r'^([+-]?\d+)x\^2([+-]\d+x)?([+-]\d+)?$'
check=re.match(checker,eqn)

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

            
            

