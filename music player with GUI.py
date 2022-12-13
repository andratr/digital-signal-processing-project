# -*- coding: utf-8 -*-
"""
Created on Wed May 19 12:45:42 2021

@author: Alex
"""

import myDSP
import numpy as np
from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
from scipy.io import wavfile
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, window ):
        window.geometry('600x200'); window.title('Music Player'); window.resizable(0,0); window.configure(background='black')
        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load, bg='#45A29E', fg='white')
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play,  bg='#86C232', fg='white')
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause, bg='#960740', fg='white')
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop , bg='red', fg='white')
        ApplyFIR = Button(window ,text = 'Apply FIR',  width = 10, font = ('Times', 10), command = self.playWithFIR)
        ApplyIIR = Button(window ,text = 'Apply IIR',  width = 10, font = ('Times', 10), command = self.playWithIIR)
        Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);
        Stop.place(x=110,y=60);
        ApplyFIR.place(x=0,y=120);ApplyIIR.place(x=220,y=120);
        
        text = Text(root, height=8,bg='black', fg='white')
        text.pack()
        text.insert('1.0', ' Music player with filters \n by Alex Hang \n Cezar Biculescu \n Andra Trandafir \n FILS 2021')
        text.place(x = 300,y = 20)
        
        self.music_file = False
        self.playing_state = False
        self.fs=[]
        self.x =[]
        
        
    def load(self):
        self.music_file = filedialog.askopenfilename()
        print(self.music_file)
        self.fs,self.x = wavfile.read(self.music_file)
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
    def playWithFIR(self):
        numtaps = 7
        f1 = 20  
        f2 = 4000
        fs = self.fs
        ft = 100
        rp = 0.3
        rs = 50
        x = self.x
        myFilter = signal.firwin(numtaps, cutoff=[f1,f2], pass_zero=False,fs=fs, window='flattop')
        filteredSignal = signal.convolve(x, myFilter, mode='valid') 
        myDSP.play(filteredSignal,fs)
        fig, (ax_orig, ax_win, ax_filt) = plt.subplots(3, 1, sharex=True)
        X_axis = np.linspace(0,2700,numtaps)
        ax_orig.plot(x)
        ax_orig.set_title('Original pulse')
        ax_win.plot(X_axis,myFilter)
        ax_win.set_title('Filter response')
        ax_win.margins(x=1,y=0.5, tight=True)
        ax_filt.plot(filteredSignal)
        ax_filt.set_title('Filtered signal')
        ax_filt.margins(0, 0.1)
        fig.tight_layout()
        fig.show()
        
    def playWithIIR(self):
        Fs = self.fs
        fc1 = 500
        fc2 = 7000
        fp = np.array([fc1, fc2])  
        ft = 100
        fcs = np.array([fc1-(ft/2), fc2+(ft/2)])
        rp = 0.4
        rs = 50 
        wp = fp/(Fs/2) 
        ws = fcs/(Fs/2) 
        N, wc = signal.ellipord(wp, ws, rp, rs)
        b,a = signal.ellip(N, rp, rs, wc, 'bandpass') 
        wz, hz = signal.freqz(b, a) 
        Mag = 20*np.sin(abs(hz))
        Phase = np.unwrap(np.arctan2(np.imag(hz),np.real(hz)))*(180/np.pi)
        Freq = wz*Fs/(2*np.pi) 
        plt.close('all') 
        fig = plt.figure()
        
        p0 = plt.subplot(2, 2, 1)
        p0.stem(b) 
        p0.set_title('Filter Coeficients')
        p0.grid()
         
        p1 = plt.subplot(2, 2, 2)
        p1.plot(Freq, Mag)
        p1.set_title('Magnitute Response')
        p1.grid()
        
        p2 = plt.subplot(2, 2, 3)
        p2.plot(Freq, Phase)
        p2.set_title('Phase response')
        p2.grid()
        
        impulse = np.repeat(0., 60)
        impulse[0] = 1.
        x = np.arange(0, 60)
        response = signal.lfilter(b, a, impulse)
         
        plt.subplot(2, 2, 4)
        plt.stem(x, response)
        plt.title('Impulse response', fontsize=15) 
        filteredSignal = signal.convolve(self.x, b, mode='valid') 
        myDSP.play(filteredSignal,Fs)
        
root = Tk()
app= MusicPlayer(root)
root.mainloop()

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:03:44 2021

@author: Alex
"""


# fc1=1000 #cut frequency
# fs,x = wavfile.read('Klingon Windows start.wav')

# wc=np.array([fc1])/(fs/2)

# N=31

# b=sp.firwin(N, wc, pass_zero=True)

# f,H=sp.freqz(b,1,worN=512,fs=fs)


# y=sp.lfilter(b,1,x)

# myDSP.play(x,fs)
# time.sleep(10)
# myDSP.play(y,fs)