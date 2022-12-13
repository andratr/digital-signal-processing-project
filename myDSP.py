# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 12:25:19 2021

@author: Alex
"""
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def createTime(t0,t1,fs):
    return np.arange(t0, t1+1/fs, 1/fs)

def sin(A,f,ph0,t):
    return A*np.sin(2*np.pi*f*t+ph0) 

def chirp(A,f1, f2, t):
    f=np.linspace(f1,f2, len(t))
    return A*np.cos(2*np.pi*f*t)

def plotInTime(x,fs):
    t = createTime(0,(len(x)-1)/fs, fs)
    plt.plot(t,x,'.-')
    plt.grid('on')
    
def plotInFrequency(x, fs):
    #abs(X) as function of freq
    X=np.fft.fft(x)
    N=int(np.ceil(len(X)/2))
    X=X[:N]
    f=np.linspace(0,fs/2,N)
    plt.plot(f, abs(X), '.-')
    plt.grid('on')
    
    
def play(x,fs):
    sd.play(x,fs)
    

def myDFT(x):
    N = len(x)
    X = np.zeros(N, dtype = 'complex_')
    pi = np.pi

    for k in range(N):  
        X[k] = 0
        for n in range(N):
            X[k] = X[k] + x[n] * np.exp(-1j * (2*pi/N)*n*k)
    return X    

def approxEqual(x,y):
    eps = 10**-6
    return np.sqrt(np.sum(x-y)**2) < eps


def whiteNoise(A,t):
    return A*np.random.uniform(-A, A, len(t))