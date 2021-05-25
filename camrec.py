import os
import moviepy.video.io.ImageSequenceClip
import moviepy.editor as mpe

image_folder='Temp'
fps=60

vidname = 'my_video.mp4'
audname = 'test.mp3'
outname = 'my_videof.mp4'
       
#image_files = [image_folder+'/'+img for img in os.listdir(image_folder)]# if img.endswith(".jpeg")]
#image_files = os.listdir(image_folder)

image_files = [image_folder+'/'+img for img in os.listdir(image_folder)]# if img.endswith(".jpeg")]
print("files scanned.")

clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)

'''
my_clip = mpe.VideoFileClip(vidname)
audio_background = mpe.AudioFileClip(audname)
final_clip = my_clip.set_audio(audio_background)
final_clip.write_videofile(outname,fps=fps)
'''


audio_background = mpe.AudioFileClip(audname)
final_clip = clip.set_audio(audio_background)
final_clip.write_videofile(outname,fps=fps)