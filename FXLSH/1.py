#!/usr/bin/env python 
# -*- coding:utf-8 -*-
m,n = input().split(',')
m=int(m)
n=int(n)
print(m,n)
items="我有一所房子面朝大海春暖花开"
item2="我有一所房子面朝大海春暖花开"
lst=list(items)
lst1=list(item2)
print(lst)
for i in range(m,n):
    print(i)
    print(lst[i])
    lst1.remove(lst[i])
print(lst1)