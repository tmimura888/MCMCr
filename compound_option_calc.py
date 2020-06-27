#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:34:08 2020

@author: mimuratakuma
"""
import random
import numpy as np
from math import exp,sqrt

def gBM(S, sigma, mu, t, z):
    gBM= S*exp((mu- sigma**2/2)*t + sigma * sqrt(t) *z)
    return gBM


#evaluating original option based off of montecarlo simulation 
def BSMC_Call(S_t,K,T,n):
    S_T=np.zeros(n)
    Call_T=np.zeros(n)
    Sum_Call_T=0
    for j in range(n):
        S_T[j]=gBM(S_t, sigma,r-q,T,random.gauss(0,1))
        Call_T[j]=max(S_T[j]- K, 0)
        Sum_Call_T=Sum_Call_T+Call_T[j]
    Expected_Call_Value=Sum_Call_T / n
    Call_Value=exp(-r*T)*Expected_Call_Value
    return Call_Value


#call on call compund option price 
def CoC_MC(S0,K1,K2,T1,T2,SampleT1,SampleOP,SampleT2):
    S_T1=np.zeros(SampleT1)
    S_T2=np.zeros(SampleT1*SampleT2)
    Call_T1=np.zeros(SampleT1)
    Call_T2=np.zeros(SampleT1*SampleT2)
    Sum_Call=0
    for n in range(SampleT1):
        S_T1[n]=gBM(S0,sigma,r-q,T1,random.gauss(0,1))
        Call_T1[n]=BSMC_Call(S_T1[n],K2,T2-T1,SampleOP)
        if Call_T1[n]>K1:
            for m in range(SampleT2):
                S_T2[n*SampleT1+m]=gBM(S_T1[n],sigma,r-q,T2-T1,random.gauss(0,1))
                Call_T2[n*SampleT1+m]=max(S_T2[n*SampleT1+m]-K2,0)
                Sum_Call=Sum_Call+Call_T2[n*SampleT1+m]-exp(r*(T2-T1))*K1
    Expected_CoC_Value=Sum_Call / SampleT1/SampleT2
    CoC_Value=exp(-r*T2)*Expected_CoC_Value
    return CoC_Value



S0=100
sigma=30/100
r=5/100
q=0/100
T1=1
T2=2
K1=20
K2=100
SampleT1=100
SampleT2=100
SampleOP=100


CoC_MC(S0,K1,K2,T1,T2,SampleT1,SampleOP,SampleT2)
print(CoC_MC)





















        