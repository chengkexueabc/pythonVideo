from moviepy.editor import  *
clip = VideoFileClip("test.mp4")
clip.write_gif('test.gif', fps=15)