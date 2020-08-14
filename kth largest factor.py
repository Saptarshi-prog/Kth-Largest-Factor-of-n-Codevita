# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 21:59:59 2020

@author: Saptarshi
"""

num, k = [int(i) for i in input().split(",")]
factor = []
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count += 1
        factor.append(i)

if count < k:
    print("1")
else:
    print(factor[-k])