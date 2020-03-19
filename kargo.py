# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:16:43 2020 

@author: iCule10 (Dishant Naik)
"""
import numpy as np
def run(s1,s2):
    x = list(s1)
    x1 = np.unique(x)
    if(len(x1) == len(s2)):
        return("true")     
    else: return("false")
    
if __name__=='__main__':
    s1 = '123' 
    s2 = '321'
    print (run(s1,s2))