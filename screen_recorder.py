# pip install opencv-python
# pip install pywin32
# pip install numpy
# pip install PyAutoGUI
from turtle import width
import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time
width_of_screen = GetSystemMetrics(0)
heigth_of_screen = GetSystemMetrics(1)
dimension_of_screen = (width_of_screen, heigth_of_screen)
video_format = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("recorder.mp4", video_format, 30.0, dimension_of_screen)
now_time = time.time()
video_duration = 20 
end_time = now_time + video_duration
while True:
    image = pyautogui.screenshot()
    video_frame = np.array(image)
    frame_color = cv2.cvtColor(video_frame, cv2.COLOR_BGR2RGB)
    output.write(frame_color)
    current_time = time.time()
    if current_time > end_time:
        break
output.release()
print("---YOUR VIDEO IS COMPLETED---")
