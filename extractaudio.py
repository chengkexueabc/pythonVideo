from moviepy.editor import *
video = VideoFileClip("D:\\Backup\\Documents\\Videos\\test.mp4")
audio = video.audio
audio.write_audiofile("D:\\Backup\\Documents\\Videos\\test.wav")
