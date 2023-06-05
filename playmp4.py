from moviepy.editor import *
import pygame

clip = VideoFileClip("test.mp4")
print(dir(clip))
print(clip.size)
print(clip.duration)
clip.preview()