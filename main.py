# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:16:43 2020 

@author: iCule10 (Dishant Naik)
"""
def run(s1,s2):
    #Both string must be of same length
    if(len(s1) == len(s2)):
        tmp_s1, tmp_s2 = {},{}
        
        #Assigning key to each value in s1
        for i, val in enumerate(s1): tmp_s1[val] = tmp_s1.get(val,[]) + [i]
        
        #Assigning key to each value in s2
        for i, val in enumerate(s2): tmp_s2[val] = tmp_s2.get(val,[]) + [i]
        
        #Compare if number of distinc values + same same values(all same valses counts as 1 e.g (aab = [[0,1],2]))in s1 is equal to s2 then return true
        #else return false
        if sorted(tmp_s1.values()) == sorted(tmp_s2.values()): return("true")
        else: return("false")
    else: return("false")
