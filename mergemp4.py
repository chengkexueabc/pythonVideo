from moviepy.editor import  *

p = 'D:\\Backup\\Documents\\Videos\\'
L = [p + '1.mp4', p+ '2.mp4']
V = []
for i in L:
    j = VideoFileClip(i)
    V.append(j)

final_clip = concatenate_videoclips(V)
final_clip.to_videofile(p + "all.mp4", fps=24, remove_temp = False)