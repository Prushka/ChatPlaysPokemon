import os
import sys

import win32gui
from PIL import ImageGrab
from sim import similarity_numpy
import time
import cv2
import numpy

hwnd = win32gui.FindWindow(0, "OBS 24.0.3 (64-bit, windows) - Profile: Untitled - Scenes: Untitled")
game_rect = win32gui.GetWindowRect(hwnd)

road_compare = numpy.array(cv2.imread("pics/road_compare_3.png"))


def get_similarity(a, b, c, d):
    sim = similarity_numpy(road_compare, numpy.array(grab(a, b, c, d)))
    # print(sim)
    if sim > 0.85:
        return True
    return False


def grab_sample(direct, name, a, b, c, d):
    grab(a, b, c, d).save(direct + '/' + name + '.png')


def grab(a, b, c, d):
    srcImage = ImageGrab.grab(
        (game_rect[0] + a, game_rect[1] + b, game_rect[2] + c,
         game_rect[3] + d))  # 左上右下
    return srcImage


def handle_fatal_error(e):
    print('Error: ' + str(e))
    os.execl(sys.executable, sys.executable, *sys.argv)


# grab_sample("Pics", "road_display", 1275, 880, -66, -602)
# grab_sample("Pics", "road_compare_1", 1275, 880, -440, -602)
# grab_sample("Pics", "road_compare_2", 1275 + 374, 880, -66, -602)
# grab_sample("Pics","road_compare_3",1320, 943, -30, -589)

while True:
    time.sleep(0.17)
    if get_similarity(1320, 943, -30, -589):
        grab_sample("pics", "road_display", 1275, 880, -66, -602)
