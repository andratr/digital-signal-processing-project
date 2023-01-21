# Music Player - Digital Signal Processing Project

For our 3rd Year project at the Digital Signal Processing subject, we have developed a music player using Python. 

## Functionalities 

The project has the following functionalities: playing, loading, stopping and pausing music files in the format of WAV and MP3. 
Furthermore, the projects shows how appling filters modifies the frequency of the song. The 2 studied filters are Finite Impulse Response filter and Infinite Impulse Response filter. On applying a filter, a graphical representation is displayed. 

## Technologies Used

The Music Player is an aplication built in Python using the following libraries:
- pygame – for playing sounds
- tkinter – for creating the interface and loading files
- numpy – for numerical functions
- scipy – for dealing with signals
- matplotlib – for displaying graphics
- myDSP – it is a module created by us to create signals

The I.D.E. used to develop the application is Spyder.

## Front End

Each button is responsible for keeping in order all possible states of the application. Only
one file can be loaded at a time, and during its playtime it can be paused or stopped.
Using the application, we can observe how the same melody sounds with a filter modifier

## Screenshots
![image](https://user-images.githubusercontent.com/64592227/213886818-c3e75f3f-8b9b-4da0-9b04-40af16c76491.png)

## Installation
To install the libraries:
```
pip install pygame --pre
pip install sounddevice   
pip install matplotlib 
pip install scipy 
pip install numpy  
```
To run the player:
```
python "music player with GUI.py"
```
## Team members
- Alexandru Hang
- Cezar Biculescu
- Andra Trandafir

