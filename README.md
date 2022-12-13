Music Player - 
DSP project

Our project scope is to create a music player capable of playing, loading, stopping, and
pausing music from WAV and MP3 files, and it can apply a Finite Impulse Response filter
and Infinite Impulse Response filter displaying information graphics (the filters work only
on WAV files).

The Music Player represents an application built in Python using the following libraries:
a. pygame – for playing sounds
b. tkinter – for creating the interface and loading files
c. numpy – for numerical functions
d. scipy – for dealing with signals
e. matplotlib – for displaying graphics
f. myDSP – it is a module created by us to create signals

The I.D.E. used to develop the application is Spyder.

Each button is responsible for keeping in order all possible states of the application. Only
one file can be loaded at a time, and during its playtime it can be paused or stopped.
Using the application, we can observe how the same melody sounds with a filter modifier
