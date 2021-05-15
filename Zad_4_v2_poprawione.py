# -*- coding: utf-8 -*-
"""
Created on Sat May 15 08:21:12 2021

@author: Tomasz_Szygenda
"""

lista=[2,5,7,1,0,2,6,9]

n=len(lista)

for i in range (0,n-1):
    print("i:",i)
    for j in range (i+1,n):
        print("j:",j)
        if lista[i]>lista[j]:
            pom=lista[i]
            lista[i]=lista[j]
            lista[j]=pom
            
print(lista)
