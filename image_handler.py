from sim import similarity_numpy
import win32gui
from PIL import ImageGrab
import time
import numpy
from PIL import Image
import cv2

hwnd = win32gui.FindWindow(0,
                           "OBS 24.0.3 (64-bit, windows) - Profile: Untitled - Scenes: Untitled")

game_rect = win32gui.GetWindowRect(hwnd)
curr_image_numpy = None


def init_image_dict():
    global image_dict
    for item in local_images:
        image_dict[item] = cv2.imread("pics/" + item + ".png")


def grab(a, b, c, d):
    srcImage = ImageGrab.grab(
        (game_rect[0] + a, game_rect[1] + b, game_rect[2] + c,
         game_rect[3] + d))  # 左上右下
    return srcImage


def get_similarity(pname, threshold):
    global curr_image_numpy
    if curr_image_numpy is None:
        curr_image_numpy = numpy.array(grab(0, 0, 0, 0))
    loc = local_images[pname]
    crop_img = curr_image_numpy[loc[1]: loc[3], loc[0]: loc[2]]
    sim = similarity_numpy(numpy.array(image_dict[pname]), crop_img)
    print(f"{pname}-相似度-Numpy：", sim)
    if sim > threshold:
        return True
    return False


def get_similarity_abcd(pname, threshold, a, b, c, d):
    global curr_image_numpy
    if curr_image_numpy is None:
        curr_image_numpy = numpy.array(grab(0, 0, 0, 0))
    crop_img = curr_image_numpy[b: d, a: c]
    sim = similarity_numpy(numpy.array(image_dict[pname]), crop_img)
    print(f"{pname}-相似度-Numpy：", sim)
    if sim > threshold:
        return True
    return False


def grab_sample(pname):
    global curr_image_numpy
    if curr_image_numpy is None:
        curr_image_numpy = numpy.array(grab(0, 0, 0, 0))
    loc = local_images[pname]
    im = Image.fromarray(curr_image_numpy[loc[1]: loc[3], loc[0]: loc[2]])
    im.save("pics/" + pname + ".png")


def grab_sample_abcd(pname, a, b, c, d):
    global curr_image_numpy
    if curr_image_numpy is None:
        curr_image_numpy = numpy.array(grab(0, 0, 0, 0))
    im = Image.fromarray(curr_image_numpy[b:d, a:c])
    im.save("pics/" + pname + ".png")


def grab_pokemon(var):
    grab_sample_abcd("pokemon01", 380, 264 + var + 120 * 0, -1060,
                     -1170 + 120 * 0 + var)
    grab_sample_abcd("pokemon02", 380, 264 + var + 120 * 1, -1060,
                     -1170 + 120 * 1 + var)
    grab_sample_abcd("pokemon03", 380, 264 + var + 120 * 2, -1060,
                     -1170 + 120 * 2 + var)
    grab_sample_abcd("pokemon04", 380, 264 + var + 120 * 3, -1060,
                     -1170 + 120 * 3 + var)
    grab_sample_abcd("pokemon05", 380, 264 + var + 120 * 4, -1060,
                     -1170 + 120 * 4 + var)
    grab_sample_abcd("pokemon06", 380, 264 + var + 120 * 5, -1060,
                     -1170 + 120 * 5 + var)
    reset_curr_image()


def reset_curr_image():
    global curr_image_numpy
    curr_image_numpy = None


def check_if_home():
    reset_curr_image()
    if get_similarity("home_shop", 0.92) or get_similarity("home_photo", 0.92):
        reset_curr_image()
        return True
    return False


def check_if_release_pokemon():
    reset_curr_image()
    if get_similarity("release01", 0.9) \
            or get_similarity("release02", 0.9):
        print("疑似放生，A键取消释放")
        reset_curr_image()
        return True
    return False


def check_if_in_pokemon():
    reset_curr_image()
    var = -1
    if get_similarity("report", 0.9):
        grab_sample_abcd("save", 415, 320, -983, -715)
    elif get_similarity("pokemon_book_black", 0.9) \
            or get_similarity("pokemon_book_white", 0.9):
        grab_sample_abcd("pokemon_caught", 1320, 360, -352, -1150)
        grab_sample_abcd("pokemon_found", 1320 + 268, 360, -352 + 268, -1150)
    elif get_similarity("pokemon", 0.89):
        var = 0
    elif get_similarity("bag", 0.9):
        var = -4
    elif get_similarity("in_battle_general", 0.91):
        var = -55
    if var != -1:
        print("目前页面为宝可梦，进行截图")
        grab_pokemon(var)
        time.sleep(0.2)
    reset_curr_image()


HIGHT_T = 0.985
LOW_T = 0.97
LOWER_T = 0.95


# False = 0
# True = 1
def check_if_in_menu(duration, which_stick, i_round, if_in_menu):
    if duration < 9:
        return False
    if i_round > 2:
        if if_in_menu:
            return True
        else:
            return False
    if which_stick == "R_STICK":
        return False
    reset_curr_image()
    if get_similarity("black_menu_bar", HIGHT_T) and not get_similarity_abcd("black_menu_bar",
                                                                             HIGHT_T, 330,
                                                                             996 - 33, -880,
                                                                             -534 - 33):
        print("目前页面为某一目录，改变按键形式为十字键")
        reset_curr_image()
        return True

    if get_similarity("catch", LOW_T) or \
            get_similarity("chat_white_menu", HIGHT_T) or \
            get_similarity("chat_black_menu", LOWER_T) or \
            get_similarity("chat_dark_menu", HIGHT_T) or \
            get_similarity("controller_keyboard", HIGHT_T):
        print("目前为DPAD需求界面")
        reset_curr_image()
        return True

    if get_similarity("normal_battle_bar", LOW_T) or \
            get_similarity("normal_battle_bar_large", LOWER_T) or \
            get_similarity("normal_battle_bar_large_2", LOWER_T) or \
            get_similarity("normal_battle_bar_2p", LOW_T) or \
            get_similarity("normal_battle_bar_2p_large", LOW_T) or \
            get_similarity("challenge_battle_bar", LOW_T) or \
            get_similarity("challenge_battle_bar_large", LOW_T) or \
            get_similarity("challenge_battle_bar_2p", LOW_T):
        print("目前为DPAD需求界面")
        reset_curr_image()
        return True

    reset_curr_image()
    return False


# grab_sample("release02", 1425, 520, -350, -755)
# grab_sample("pokemon", 330, 150, -900, -1300)
# grab_sample("home", 330, 150, -900, -1300)
# grab_sample("report", 330, 150, -900, -1300)
# grab_sample("bag", 330, 150, -980, -1300)
# grab_sample("in_battle", 330, 140, -500, -1380)
# grab_sample("in_battle_general", 330, 140, -920, -1380)
# grab_sample("save", 415, 320, -983, -715)

# grab_sample("pokemon_book_white", 1350, 245, -100, -1200)
# grab_sample("pokemon_book_white", 1350, 245, -100, -1200)
# 494
# grab_sample("black_menu_bar", 330, 996, -880, -534)
# grab_sample("chat_black_menu", 1470, 865, -375, -565)
# grab_sample("controller_keyboard", 494-160, 980 - 30, -1261, -560+20)
# grab_sample("pokemon", 330, 150, -900, -1300)

local_images = {"bag": [330, 150, -980, -1305],
                "black_menu_bar": [330, 996, -880, -534],
                "chat_black_menu": [1470, 865, -375, -565],
                "chat_dark_menu": [1470, 865, -375, -565],
                "chat_white_menu": [1470, 865, -375, -565],
                "controller_keyboard": [494 - 160, 980 - 30, -1261, -560 + 20],
                "home_shop": [845, 750, -970, -680],
                "home_photo": [845 + 135, 750, -970 + 135, -680],
                "shop_dlc": [1450, 600, -130, -680],
                "in_battle_general": [330, 140, -920, -1380],

                "normal_battle_bar": [495, 980, -1261, -560],
                "normal_battle_bar_2p": [495, 980 - 18, -1261, -560 - 18],
                "normal_battle_bar_large": [530, 980, -1261, -560],
                "normal_battle_bar_large_2": [530, 980, -1261, -560],
                "normal_battle_bar_2p_large": [495, 980 - 18, -1261, -560 - 18],
                "challenge_battle_bar": [559, 980, -1170, -560],
                "challenge_battle_bar_2p": [559, 980 - 18, -1170, -560 - 18],
                "challenge_battle_bar_large": [559, 980, -1170, -560],
                # "challenge_battle_bar_2p_large": [559, 980 - 18, -1170, -560 - 18],
                "catch": [1830, 690, -40, -610],

                "pokemon": [330, 150, -900, -1300],
                "pokemon_book_black": [1350, 245, -270, -1200],
                "pokemon_book_white": [1350, 245, -270, -1200],
                "release01": [1425, 520, -350, -755],
                "release02": [1425, 520, -350, -755],
                "report": [330, 150, -900, -1300],
                }

image_dict = {}

reset_curr_image()
init_image_dict()
