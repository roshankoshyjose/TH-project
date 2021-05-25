# https://medium.com/analytics-vidhya/how-to-create-a-music-visualizer-7fad401f5a69
import time
torch = time.time()
print("Initialising.\n")

import librosa
import numpy as np
import pygame
import time 
import os


# Ensure we have somewhere for the frames
image_folder='Temp'
try:
    os.makedirs(image_folder)
except OSError:
    pass


def clamp(min_value, max_value, value):

    if value < min_value:
        return min_value

    if value > max_value:
        return max_value

    return value


class AudioBar:

    def __init__(self, x, y, freq, color, width=50, min_height=10, max_height=100, min_decibel=-80, max_decibel=0):

        self.x, self.y, self.freq = x, y, freq

        self.color = color

        self.width, self.min_height, self.max_height = width, min_height, max_height

        self.height = min_height

        self.min_decibel, self.max_decibel = min_decibel, max_decibel

        self.__decibel_height_ratio = (self.max_height - self.min_height)/(self.max_decibel - self.min_decibel)

    def update(self, dt, decibel):

        desired_height = decibel * self.__decibel_height_ratio + self.max_height

        speed = (desired_height - self.height)/0.1

        self.height += speed * dt

        self.height = clamp(self.min_height, self.max_height, self.height)

    def render(self, screen):

        pygame.draw.rect(screen, self.color, (self.x, self.y + self.max_height - self.height, self.width, self.height))


filename = "test.mp3"

time_series, sample_rate = librosa.load(filename)  # getting information from the file

# getting a matrix which contains amplitude values according to frequency and time indexes
stft = np.abs(librosa.stft(time_series, hop_length=512, n_fft=2048*4))

spectrogram = librosa.amplitude_to_db(stft, ref=np.max)  # converting the matrix to decibel matrix

frequencies = librosa.core.fft_frequencies(n_fft=2048*4)  # getting an array of frequencies

# getting an array of time periodic
times = librosa.core.frames_to_time(np.arange(spectrogram.shape[1]), sr=sample_rate, hop_length=512, n_fft=2048*4)

time_index_ratio = len(times)/times[len(times) - 1]

frequencies_index_ratio = len(frequencies)/frequencies[len(frequencies)-1]


def get_decibel(target_time, freq):
    return spectrogram[int(freq * frequencies_index_ratio)][int(target_time * time_index_ratio)]


pygame.init()

infoObject = pygame.display.Info()

screen_w = int(infoObject.current_w/2.5)
screen_h = int(infoObject.current_w/2.5)

# Set up the drawing window
screen = pygame.display.set_mode([screen_w, screen_h])


bars = []


frequencies = np.arange(100, 8000, 100)

r = len(frequencies)


width = screen_w/r


x = (screen_w - width*r)/2

for c in frequencies:
    bars.append(AudioBar(x, 300, c, (255, 0, 0), max_height=400, width=width))
    x += width

t = pygame.time.get_ticks()
getTicksLastFrame = t

#pygame.mixer.music.load(filename)
#pygame.mixer.music.play(0)

# Run until the user asks to quit
running = True

number = 1
fps = 60
lfps = 1/fps
lfpst = 1/fps
song_duration = librosa.get_duration(filename=filename)
#clock = pygame.time.Clock()
print("\nStarting shots.\n")
while running:
    framerate = time.time()
    
    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    for b in bars:
        b.update(deltaTime, get_decibel(lfps, b.freq))
        b.render(screen)

    # Flip the display
    pygame.display.flip()
    
    #print(time.time() - framerate)
    filename = "temp/%04d.jpeg" % number
    pygame.image.save(screen, filename)
    #lfps.append(time.time() - framerate)
    lfps += lfpst
    
    number+=1
    #print(pygame.mixer.music.get_pos()//1000)
    '''
    c = pygame.mixer.music.get_pos()//1000
    if not (c < song_duration and c!=-1):
        pygame.quit()
        running = False'''
    print(lfps,"/", song_duration)
    if not (lfps < song_duration):# and c!=-1):
        pygame.quit()
        running = False
    
    

# Done! Time to quit.
pygame.quit()
print("Screenshots Generated.\n")
#fps = int(1//np.mean(lfps))
#exec(open("./camrec.py").read())
##########################################
"""
vidname ='temp.mp4'
audname = filename
outname = filename[:filename.rfind('.')]+'.mp4'

'''
vidname = 'my_video.mp4'
audname = 'test.mp3'
outname = 'my_videof.mp4'
'''  
#image_files = [image_folder+'/'+img for img in os.listdir(image_folder)]# if img.endswith(".jpeg")]
#image_files = os.listdir(image_folder)
'''
image_files = [image_folder+'/'+img for img in os.listdir(image_folder)]# if img.endswith(".jpeg")]

clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile(vidname)

my_clip = mpe.VideoFileClip(vidname)
audio_background = mpe.AudioFileClip(audname)
final_clip = my_clip.set_audio(audio_background)
final_clip.write_videofile(outname,fps=fps)
'''

image_files = [image_folder+'/'+img for img in os.listdir(image_folder)]# if img.endswith(".jpeg")]
print("\nfiles scanned.\n")

clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
print("\nVideo temp done.\n")
audio_background = mpe.AudioFileClip(audname)
final_clip = clip.set_audio(audio_background)
final_clip.write_videofile(outname,fps=fps)
print("\nVideo done.\n")


    
#convert(filename,image_folder,fps)




try: 
    shutil.rmtree("temp")
    os.remove("temp.mp4") 
    print("\nTemp files deleted.\n")
except:
    pass
"""
print("total time = ",time.time()-torch)