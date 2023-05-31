from vidgear.gears import CamGear
import cv2
import time


stream = CamGear(source=0).start()

totalTime = 0
num = 100


videoWriter=cv2.VideoWriter('1.avi',cv2.VideoWriter_fourcc('X','V','I','D'),3,(640, 480))


# 循环读取100帧
for i in range(num):

    start = time.time()
    frame = stream.read()

    end = time.time()
    totalTime += (end-start)

    if frame is None:
        break

    cv2.imshow("Output", frame)
    videoWriter.write(frame)

    # 按q退出
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

print("平均每帧读取时间为{:.2f}ms".format(1000.0*totalTime/num))

# 关闭窗口
cv2.destroyAllWindows()

# 释放视频流
stream.stop()