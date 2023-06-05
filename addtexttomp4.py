from moviepy.editor import *

video1 = VideoFileClip("test.mp4")
text_clip = TextClip('程老师系列课程', fontsize=50, font=r'c:\windows\fonts\STXINGKA.TTF', color='black', bg_color='transparent', transparent=True).set_position(('right','top')).set_duration(1200).set_start(0)
video = CompositeVideoClip([video1, text_clip])
video.write_videofile("testABC.mp4")

