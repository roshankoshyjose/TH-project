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

'''

NOTE :
    
    1) The application will run into an error if the song filename contains
       square brackets. It is because it uses markup language .
    
    2) As of now it only works with mp3 as pygame has errors with other extensions

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
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
#from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.properties import NumericProperty

# Profile
import cProfile

# pygame
#import pygame
from pygame import mixer

# librosa
# import librosa
from librosa import get_duration

# others
import time
'''
# functions
def playlist(filepath):
    mixer.music.unload()
    mixer.music.load(filepath)
    mixer.music.play()
    return
'''

# Base
class base(BoxLayout):

    seconds_string = StringProperty('')  # time count of audio
    slider_value = NumericProperty()     # slider value
    #plt = StringProperty('')            # playlist text
    #songlength = StringProperty('')     # song length
            
    '''def __init__(self):
        pass'''
    
    def select(self,filepath,key = 0):
        #print(filepath)
        global plist,current #,songlength
        
        song = (filepath)[filepath.rfind("\\")+1:-4] # song name
        refer = '[ref='+filepath+']'+song+'[/ref]'   # referal
        
        # if folder selected
        if filepath.find('.') == -1: return
        
        #print(song)
        #print(refer)
        
        if filepath not in plist or key == 1: 
            
            # shorten name of song
                
            plist.append(filepath)
            #print(plist)
            
            self.ids.playlist.text += '\n. '+ refer      # added text
        
        # to add song again
        else:
            
            pass
            '''
            # popup layout
            layout = GridLayout(cols = 1, padding = 10)
            BL = BoxLayout(orientation ='horizontal')
            
            # popup
            popup = Popup(title ='AiR',content = layout,size_hint =(None, None), 
                          size =(400, 200)) 
                   
            layout.add_widget(Label(text = "Would you like to add the song again?"))
            layout.add_widget(BL)
            BL.add_widget(Button(text = "yes",on_press = self.pseudo))    
            BL.add_widget(Button(text = "no",on_press = popup.dismiss))
      
            popup.open()   
            '''
                    
        if not mixer.music.get_busy():
            # play 
            
            try:
                mixer.music.unload()
                mixer.music.load(filepath)
                mixer.music.play() 
                
                current = filepath
                self.ids.current.text = "Now : "+song
            except:
                pass
            
            
            # song length
            #n = mixer.Sound(filepath).get_length()//1000
            #self.songlength = time.strftime("%H:%M:%S", time.gmtime(n))
        
        '''
        
        song = (filepath)[filepath.rfind("\\")+1:-4] # song name
        refer = '[ref='+filepath+']'+song+'[/ref]'   # referal
        
        self.ids.playlist.text += '\n. '+ refer      # added text
        
        mixer.music.unload()
        mixer.music.load(filepath)
        mixer.music.play()    
        '''
        
    def playpause(self):
        if mixer.music.get_busy():
            mixer.music.pause()
        else:
            mixer.music.unpause()
            
    def naudio(self): # next audio
        global plist,current
        
        try:     # check if last song
            filepath = plist[plist.index(current)+1]
            mixer.music.unload()
            mixer.music.load(filepath)
            mixer.music.play()
            
            current = filepath
            self.ids.current.text = "Now : "+(current)[current.rfind("\\")+1:-4]
            
        except:  # error
            mixer.music.unload()
            mixer.music.load(current)
            mixer.music.play()
            
    def paudio(self): # Previous audio
        global plist,current
        
        try:     # check if first song
            filepath = plist[plist.index(current)-1]
            mixer.music.unload()
            mixer.music.load(filepath)
            mixer.music.play()
            
            current = filepath
            self.ids.current.text = "Now : "+(current)[current.rfind("\\")+1:-4]
            
        except:  # error
            mixer.music.unload()
            mixer.music.load(current)
            mixer.music.play()
            
    # seeker
    def test(self,filepath):
        
        global current
        
        mixer.music.unload()
        mixer.music.load(filepath)
        mixer.music.play()
        
        current = filepath
        self.ids.current.text = "Now : "+(current)[current.rfind("\\")+1:-4]
        
        # song length
        # n = mixer.Sound(filepath).get_length()//1000
        # self.songlength = time.strftime("%H:%M:%S", time.gmtime(n))
    
    def pseudo(self,button):#,ps,pp):
        '''
        pp.dismiss()
        self.select(ps,1)
        '''
        return
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
        
        #self.plt = "[u]playlist[/u]"
        
        return base() 
    
    def on_start(self):
        
        # Profile
        self.profile = cProfile.Profile()
        self.profile.enable()

    def stop(self):
        
        # Profile
        self.profile.disable()
        self.profile.dump_stats('AiR_lastRun.profile')
        
        # pygame
        #mixer.stop()
        mixer.quit()
        
        # kivy
        Window.close()
        
    def update_time(self):
        global current
        #self.root.seconds_string = time.strftime("%S")
        n = mixer.music.get_pos()//1000
        
        if n == -1:
            n = 0
            y = 0
        else:
            #y = librosa.get_duration(filename = current)
            y = get_duration(filename = current)
            
        self.root.seconds_string = time.strftime("%H:%M:%S", time.gmtime(n))+' / '+time.strftime("%H:%M:%S", time.gmtime(y))
        #self.root.slider_value = (n*100)/(librosa.get_duration(filename = current))
        try:
            self.root.slider_value = (n*100)/(y)
        except:
            self.root.slider_value = -1

# App initialisation
if __name__ == "__main__":
    
    # initialisations
    mixer.init()                      # start pygame mixer
    plist = []                        # playlist
    current = 'Welcome to AiR.mp3'    # current audio
    #key = 0                          # just a key for the popup
    #songlength = ''                  # song length
    
    # The App
    main = airApp() 
    main.run()


# Output
            #self.ids.output.text = str(o)
            #self.ids.entry.text = ''

# To do
# 1) Volume
# 2) Seek
# 3) visualiser
# 4) Scroll/ update playlist + save playlist
