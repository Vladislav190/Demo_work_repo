from w_s.Trun_Funct import TF
from math import comb
from w_s.InLpfTf import *

def binom(T, n):
    a = []
    for i in range(n,-1,-1):
        a += [T**i * comb(n,i)]
    return a   

def createfilter(chain):
   w = TF([1],[1])
   for i in chain:
      match i:
         case lpfunction(deg=n, Tt=t)           : w = w * TF([1], binom(t, n)) 
         case TranceFunction(num=up, den=dw)    : w = w * TF(up, dw)
         case Integration()                     : w = w * TF([1], [1,0])
   return w