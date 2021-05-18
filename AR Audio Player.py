# BFH pgm for a audio equalizer
# Pgm by Aromal and Roshan
# DOB : 17 - 05 - 2021 sometime in the evening
# The AiR Player

'''
Aim : Make a media player

VISUAL :
    
1. Have a GUI
2. Locate
3. Play
   # things normally have
4. Equalizer
5. other basic functions

'''

'''

what would u prefer when u right a code. my heads just over heated right now and 
im thinking, should i complicate stuff or should i just write as it is. Ahh hell.

so first think kivy or tkinter

well kivy is gonna be more complicated, so why not.

'''

# Imports

# kivy it is!!!
import kivy
from kivy.app import App
from kivy.config import Config 
from kivy.core.window import Window

# UIX
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.pagelayout import PageLayout 
from kivy.uix.carousel import Carousel
from kivy.clock import Clock
from kivy.properties import StringProperty

# pygame
import pygame
from pygame import mixer

# others
import time

# Base
class base(BoxLayout):
    
    '''def __init__(self):
        pass'''
        
    seconds_string = StringProperty('')
        
    def select(self,filepath):
        #print(filepath)
        mixer.music.unload()
        mixer.music.load(filepath)
        mixer.music.play()
    
    def playpause(self):
        if mixer.music.get_busy():
            mixer.music.pause()
        else:
            mixer.music.unpause()
            
    # seeker
    def test(self):
        pass
    
'''
# custom task bar

    def Minus_app_button(self):
        App.get_running_app().root_window.minimize()
        print("hello")
        
    def MaxiMin_app_button(self):
        print("hello")
        if Window.fullscreen:
            Window.fullscreen = False
        else:
            Window.fullscreen = True

    def close_app_button(self):
        App.get_running_app().stop()
'''
 
class airApp(App):
    
    def build(self):
        
        # Layout dimensions
        #Config.set('graphics', 'resizable', False)
        #Config.set('graphics', 'borderless', 'True')
        #Config.set('graphics', 'width', '400') 
        #Config.set('graphics', 'height', '300')    
        
        Clock.schedule_interval(lambda dt: self.update_time(), 1)
        
        self.title = 'AiR Player'
        #self.icon = 'AiR.png'
        Window.size = (1000,600)
        #Window.borderless = True
        
        return base()   

    def update_time(self):
        #self.root.seconds_string = time.strftime("%S")
        self.root.seconds_string = str(mixer.music.get_pos()//1000)
# App initialisation
if __name__ == "__main__":
    
    mixer.init()
    
    kric = airApp() 
    kric.run()


# Output
            #self.ids.output.text = str(o)
            #self.ids.entry.text = ''
