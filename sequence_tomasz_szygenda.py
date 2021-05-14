# -*- coding: utf-8 -*-
"""
Created on Fri May  14 22:56:02 2021

@author: Tomasz_Szygenda
"""


sequence=[2,3,4,1,2,5]
n=6
maxx=sequence[0]
imax=0
a=1


while a<n:
    if sequence[a]>maxx:
        maxx=sequence[a]
        imax=a
        a=a+1
        
        
        
print(maxx,imax)
        
        