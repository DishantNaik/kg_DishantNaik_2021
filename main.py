# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:16:43 2020 

@author: iCule10 (Dishant Naik)
"""
def run(s1,s2):
    if(len(s1) == len(s2)):
        tmp_s1, tmp_s2 = {},{}
        
        for i, val in enumerate(s1): tmp_s1[val] = tmp_s1.get(val,[]) + [i]
        
        for i, val in enumerate(s2): tmp_s2[val] = tmp_s2.get(val,[]) + [i]
        
        if sorted(tmp_s1.values()) == sorted(tmp_s2.values()): return("true")
        else: return("false")
    else: return("false")
    
if __name__=='__main__':
    s1 = 'ab' 
    s2 = 'xxy'
    print (run(s1,s2))
