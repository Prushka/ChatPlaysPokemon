from codec_constants import JOYCON_DICT
import re

MAX_COMMAND = 23


def replace_str(replace_dict, msg):
    for to_replace, place in replace_dict.items():
        msg = msg.replace(to_replace, place)
    return msg


def remove_at(i, s):
    return s[:i] + s[i + 1:]


translate_to_eng = {"上": "UP",
                    "下": "DOWN",
                    "左": "LEFT",
                    "右": "RIGHT",
                    "等待": "WAIT",
                    "十字键": "DPAD",
                    "摇杆": "Stick"
                    }


def translate(msg):
    return replace_str(translate_to_eng, msg)


directional_commands = {"上": [0, -1, "十字键-上"],
                        "下": [0, 1, "十字键-下"],
                        "左": [-1, 0, "十字键-左"],
                        "右": [1, 0, "十字键-右"],
                        "顺": [],
                        "逆": [],
                        "转": [],
                        "P": []}

formatted_replace = {"UP": "上",
                     "DOWN": "下",
                     "LEFT": "左",
                     "RIGHT": "右",

                     "ZL": "Q",
                     "ZR": "E",
                     "LT": "Q",
                     "RT": "E",
                     "LCLICK": "I",
                     "RCLICK": "O",
                     "，": "",
                     ",": "",
                     "*": "",
                     "！": "!",
                     "＋": "+",
                     "【": "[",
                     "】": "]",
                     "¥": "$",
                     "￥": "$",
                     "目录": "X", "信息": "Y",
                     "一": "1",
                     "二": "2",
                     "三": "3",
                     "四": "4",
                     "五": "5",
                     "六": "6",
                     "七": "7",
                     "八": "8",
                     "九": "9",
                     "存档": "XRA",
                     "连接交换": "YA下A3右2下A上左2A下右A下左A+A3",

                     "圈": "",
                     "时针": "",

                     "确认": "A",
                     "确定": "A",
                     "返回": "B",
                     "PLUS": "+",
                     "MINUS": "-",
                     "——": "-",
                     "等待": "P",
                     "等": "P",
                     "WAIT": "P",
                     }

formatted_button_beautify = {
    "Q": "ZL",
    "E": "ZR",
    "I": "LCLICK",
    "O": "RCLICK"
}
single_replace = {
    "前": "上",
    "W": "上",
    "↑": "上",

    "后": "下",
    "↓": "下",
    "S": "下",

    "LE": "左",
    "←": "左",

    "D": "右",
    "→": "右",

    "!!": "&",
}

formatted_button_replace = {"转": ["上", "左", "下", "右"]}

init_handler = {
    "翻译": "查词",
    "词典": "查词",
    "字典": "查词",
}


def init_msg_handler(msg):
    msg = replace_str(init_handler, msg)
    return msg


def msg_handler(msg):
    msg = msg.upper()
    msg = replace_str(formatted_replace, msg)
    msg = replace_str(single_replace, msg)
    buttons = []
    c = 0
    while c < len(msg):
        """
        if msg[c] == "[":
            is_in_bracket = True
            c += 1
            continue
        elif msg[c] == "]":
            is_in_bracket = False
            try:
                times = int(msg[c + 1] + msg[c + 2])
                if times > 12:
                    times = 12
                buttons.append([f"cts{temp_str}", times])
                c += 3
            except:
                try:
                    times = int(msg[c + 1])
                    buttons.append([f"cts{temp_str}", times])
                    c += 2
                except:
                    times = 1
                    buttons.append([f"cts{temp_str}", times])
                    c += 1

            temp_str = ""
            continue
        
        if is_in_bracket:
            if msg[c] in JOYCON_DICT or msg[c] in directional_commands:
                temp_str += msg[c]
            c += 1
        """
        if msg[c] in JOYCON_DICT or msg[c] in directional_commands or msg[c] in formatted_button_beautify:
            try:
                times = int(msg[c + 1] + msg[c + 2])
                if times > MAX_COMMAND:
                    times = MAX_COMMAND
                buttons.append([msg[c], times])
                c += 3
            except:
                try:
                    times = int(msg[c + 1])
                    buttons.append([msg[c], times])
                    c += 2
                except:
                    times = 1
                    buttons.append([msg[c], times])
                    c += 1

        else:
            c += 1

    sec_buttons = []
    for button in buttons:
        if button[0] in formatted_button_replace:
            for b in range(button[1]):
                for a in formatted_button_replace[button[0]]:
                    sec_buttons.append([a, 1])
        elif button[0] in formatted_button_beautify:
            sec_buttons.append([formatted_button_beautify[button[0]], button[1]])
        else:
            sec_buttons.append([button[0], button[1]])

    return msg, sec_buttons


def macro_msg_handler(msg):
    macro = msg[:msg.find("=")]
    command = msg[msg.find("=") + 1:]
    formatted_msg, buttons = msg_handler(command)
    if len(buttons) == 0:
        return "", ""
    total_duration = 0
    for b in buttons:
        total_duration += b[1]
    # if total_duration > 40:
    #     return "", ""
    return macro, formatted_msg


def buttons_to_text(buttons):
    result = ""
    for button in buttons:
        if button[1] == 0:
            continue
        result += button[0] + str(button[1])
    return result


keyboard_position = {"1": [1, 1],
                     "2": [2, 1],
                     "3": [3, 1],
                     "4": [4, 1],
                     "5": [5, 1],
                     "6": [6, 1],
                     "7": [7, 1],
                     "8": [8, 1],
                     "9": [9, 1],
                     "0": [10, 1],
                     "-": [11, 1],
                     "——": [11, 1],

                     "q": [1, 2],
                     "w": [2, 2],
                     "e": [3, 2],
                     "r": [4, 2],
                     "t": [5, 2],
                     "y": [6, 2],
                     "u": [7, 2],
                     "i": [8, 2],
                     "o": [9, 2],
                     "p": [10, 2],
                     "/": [11, 2],

                     "a": [1, 3],
                     "s": [2, 3],
                     "d": [3, 3],
                     "f": [4, 3],
                     "g": [5, 3],
                     "h": [6, 3],
                     "j": [7, 3],
                     "k": [8, 3],
                     "l": [9, 3],
                     ":": [10, 3],
                     "、": [11, 3],

                     "z": [1, 4],
                     "x": [2, 4],
                     "c": [3, 4],
                     "v": [4, 4],
                     "b": [5, 4],
                     "n": [6, 4],
                     "m": [7, 4],
                     ",": [8, 4],
                     "，": [8, 4],
                     "。": [9, 4],
                     "?": [10, 4],
                     "？": [10, 4],
                     "!": [11, 4],
                     "！": [11, 4],
                     }


def guide_to_key(previous_key, key):
    result = ""
    try:
        downward = keyboard_position[key][1] - keyboard_position[previous_key][1]
        rightward = keyboard_position[key][0] - keyboard_position[previous_key][0]
        if downward > 0:
            result += f"下{downward}"
        elif downward < 0:
            result += f"上{-downward}"
        if rightward > 0:
            result += f"右{rightward}"
        elif rightward < 0:
            result += f"左{-rightward}"
    except:
        result = ""
    return result


def calculate_keyboard(keys):
    keys = keys.lower()
    result = ""
    key_lst = list(keys)
    previous_key = "1"
    for index in range(len(key_lst)):
        key = key_lst[index]
        key_str = guide_to_key(previous_key, key)
        if key_str == "":
            return ""
        result += key_str + "a"
        previous_key = key
    result += guide_to_key(previous_key, "1")
    return "@" + result


not_white_list_commands = {
    "HOME": "",
    "CAPTURE": "",
    "🏘": "",
    "📷": ""
}


def clean_ur_command(msg):
    msg = msg.upper()
    return replace_str(not_white_list_commands, msg)
