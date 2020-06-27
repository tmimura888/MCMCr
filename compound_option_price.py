#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 17:33:16 2020

@author: mimuratakuma
"""

from scipy.stats import norm, mvn
from scipy import exp,log,sqrt,optimize,pi,sign
import numpy as np

def BS_Call(S, sigma ,r,q,T,K):
    d1 = (log(S / K) + (r -q+ sigma**2 / 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    BS_Call = S * exp(-q * T) * norm.cdf(x=d1, loc=0, scale=1) \
             -K * exp(-r * T) * norm.cdf(x=d2, loc=0, scale=1)
    return BS_Call

def h(S_sol):
    return BS_Call(S_sol, sigma ,r,q,T2-T1,K2)-K1

def M_MVN(a,b,c):
    mean = np.array([0,0])
    Sigma = np.array([[1,c],[c,1]])
    lower=np.array([-10000,-10000])
    upper=np.array([a,b])
    p,i=mvn.mvnun(lower,upper,mean,Sigma)   
    return p

def CoC_AN_MVN(S0,T1,T2,K1,K2):
    S_star=float(optimize.fsolve(h,100)) #配列形式を数値に変換
    a1 = (log(S0 / S_star) + (r-q + sigma**2 / 2) * T1) / (sigma * sqrt(T1))
    a2 = a1 - sigma * sqrt(T1)
    b1 = (log(S0 / K2) + (r-q + sigma**2 / 2) * T2) / (sigma * sqrt(T2))
    b2 = b1 - sigma * sqrt(T2)
    CoC_AN = S0  * exp(-q * T2)*M_MVN(a1,b1,sqrt(T1/T2))\
          - K2 * exp(-r * T2) *M_MVN(a2,b2,sqrt(T1/T2))\
          -K1* exp(-r * T1) *norm.cdf(x=a2, loc=0, scale=1)
    return CoC_AN

S0=100
sigma=30/100
r=5/100
q=0/100
T1=1
T2=2
K1=20
K2=100
rho=0.3
SampleT1=100
SampleT2=100
SampleOP=100





















