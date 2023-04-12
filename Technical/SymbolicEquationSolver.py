#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 01:17:32 2023

@author: JuxtaR_YCT
"""
explist=[]
print("Enter the equation: ")
eqn=input()
for i in eqn:
    explist.append(i)
print(explist)
for i in explist:
    if(i=="^"):
        if(explist[i+1]==2):
    
            if(explist[0].isalpha()==False):
                a=explist[0]
                a=int(a)
            else:
                a=1
for i i