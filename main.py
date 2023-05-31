import os
import cv2
import subprocess

os.chdir("D:\Backup\Documents\Videos")
v_path = 'test.mp4'
image_save = './'

cap = cv2.VideoCapture(v_path)
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

for i in range(int(frame_count)):
    _, img=cap.read()
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #cv2.COLOR_RGB2HSV     cv2.COLOR_BGR2GRAY
    cv2.imwrite('./pic/image{}.jpg'.format(i), img)


print(dir(cv2))
