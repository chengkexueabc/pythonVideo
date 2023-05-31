from moviepy.editor import *
clip = VideoFileClip("D:\\Backup\\Documents\\Videos\\1.mp4")
clip = clip.rotate(90)
clip.write_videofile("res.mp4")