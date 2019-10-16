import json
from translation import youdao_translate
import bilibili_avatar

root = "Resources/"
txts_path = f"{root}txts/"
webs_path = f"{root}web/"
web_chat_lines_allowed = 5

message_dict = {
    "Bilibili": {
        "NOT_COMMAND": "非指令",
        "FINISHED": "完毕",
        "EXCUTING": "执行中",
        "REMAINING": "剩余",
        "RELEASE01": "违规操作",
        "RELEASE02": " | 您已被记录，可能会被公示+黑名单",
        "L_STICK": "左摇杆",
        "R_STICK": "右摇杆",
        "等待": "等待"
    },
    "Twitch": {
        "NOT_COMMAND": "Chat",
        "FINISHED": "Finished",
        "EXCUTING": "Excuting",
        "REMAINING": "Remaining",
        "RELEASE01": "You're not permitted to release any pokemons",
        "RELEASE02": "",
        "L_STICK": "L-Stick",
        "R_STICK": "R-Stick",
        "等待": "Wait"
    }
}

with open(txts_path + "index_cat.txt", 'r', encoding='utf-8') as f:
    cat_index = int(f.readline().rstrip())


def append_to_file(fname, line):
    with open(txts_path + fname, 'a', encoding='utf-8') as f:
        f.write(line + "\n")


def write_to_file(fname, line):
    with open(txts_path + fname, 'w', encoding='utf-8') as f:
        f.write(line + "\n")


def total_danmu_write(total_danmu):
    write_to_file('obs_danmu_lines.txt', f"弹幕总数：{total_danmu}")
    if (total_danmu / 100).is_integer():
        write_to_cat(
            f"<dark-red>弹幕总数达到了</dark-red><red style='font-size:22px;'>{total_danmu}！</red>")


def init_gift():
    f = open(txts_path + "gifts_count.txt", "r", encoding='utf-8')
    lines = f.readlines()
    user_gift = []
    gift_sent_users = []
    for line in lines:
        if len(line) < 4:
            continue
        line_ = line.rstrip()
        line_ = line_.split(",")
        user_gift.append(
            [line_[0], int(line_[1]), int(line_[2]), int(line_[3])])
        gift_sent_users.append(line_[0])
    return user_gift, gift_sent_users,


def init_danmu_lines():
    f = open(txts_path + "all_danmu.txt", "r", encoding='utf-8')
    lines = f.readlines()
    total_danmu = 89879 + 5700
    for line in lines:
        total_danmu += 1
    f.close()
    return total_danmu


def init_macro():
    with open(txts_path + 'macro.json', "r", encoding='utf-8') as f:
        d = json.load(f)
    return d


def init_day_gift():
    with open(txts_path + 'gift_by_day.json', "r", encoding='utf-8') as f:
        d = json.load(f)
    return d


def init_day_gift_user():
    with open(txts_path + 'gift_by_day_user.json', "r", encoding='utf-8') as f:
        d = json.load(f)
    return d


def record_gift_by_day(gift_by_day):
    with open(txts_path + 'gift_by_day.json', 'w', encoding='utf-8') as f:
        json.dump(gift_by_day, f, ensure_ascii=False, indent=4)


def record_gift_by_day_user(gift_by_day_user):
    with open(txts_path + 'gift_by_day_user.json', 'w', encoding='utf-8') as f:
        json.dump(gift_by_day_user, f, ensure_ascii=False, indent=4)


def record_macro_commands(macro_dict):
    with open(txts_path + 'macro.json', 'w', encoding='utf-8') as f:
        json.dump(macro_dict, f, ensure_ascii=False, indent=4)


def write_to_html(msg_list):
    result = "".join(msg_list)
    with open(webs_path + "include_chat.html", 'w', encoding='utf-8') as f:
        f.write(result)


def write_to_cat(msg):
    global cat_index
    cat_index += 1
    write_to_file("index_cat.txt", str(cat_index))
    index = f"[{cat_index:07d}]"
    with open(webs_path + "live2d/cat_message.txt", 'w', encoding='utf-8') as f:
        f.write(index + msg)


def write_to_leaderboard(msg, fname):
    write_to_file("index_cat.txt", str(cat_index))
    with open(webs_path + f"live2d/{fname}.txt", 'w', encoding='utf-8') as f:
        f.write(msg)


def init_cat():
    index = f"[{cat_index:07d}]"
    with open(webs_path + "live2d/cat_message.txt", 'w', encoding='utf-8') as f:
        f.write(index + "初始化成功...")


def get_user_html(uname, uid, curr_len):
    avatar = bilibili_avatar.fetch_img_src(uid)
    result = f"<span id='a{curr_len}'><img class='author-face' src='live2d/{avatar}'>{uname}：</span>\n"
    # result = f"<span id='a{curr_len}'>{uname}：</span>\n"
    return result


def append_obs_display_chat(curr_chat_info, curr_chat):
    uname, msg, uid, which_platform = curr_chat_info[0], curr_chat_info[1], curr_chat_info[2], curr_chat_info[3]
    if len(curr_chat) > web_chat_lines_allowed:
        for i in range(len(curr_chat)):
            curr_chat[i] = curr_chat[i].replace(f"{i}'>", f"{i - 1}'>")
        curr_chat.pop(0)
    curr_len = len(curr_chat)
    result = get_user_html(uname, uid, curr_len)
    msg += "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
    result += f"<span id='c{curr_len}'>{msg}<div class='running'>[执行中]</div></span>\n"
    curr_chat.append(result)
    write_to_html(curr_chat)


def append_obs_display_gift(curr_chat_info, gift_name, gift_num, curr_chat):
    uname, msg, uid, which_platform = curr_chat_info[0], curr_chat_info[1], curr_chat_info[2], curr_chat_info[3]
    if len(curr_chat) > web_chat_lines_allowed:
        for i in range(len(curr_chat)):
            curr_chat[i] = curr_chat[i].replace(f"{i}'>", f"{i - 1}'>")
        curr_chat.pop(0)
    curr_len = len(curr_chat)
    result = get_user_html(uname, uid, curr_len)
    result += f"<span class='gift-message' id='c{curr_len}'>{gift_name}x{gift_num}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<div class='gift_command'>[这条不是指令，但似乎很重要٩( 'ω' )و ]</div></span>\n"
    curr_chat.append(result)
    write_to_html(curr_chat)


def update_obs_display_chat(curr_chat_info, curr_chat, is_finished, is_command, curr_command="",
                            remaining_command="", finished_command=""):
    uname, msg, uid, which_platform = curr_chat_info[0], curr_chat_info[1], curr_chat_info[2], curr_chat_info[3]
    curr_chat.pop(-1)
    curr_len = len(curr_chat)
    result = get_user_html(uname, uid, curr_len)
    msg += "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
    if not is_command:
        result += f"<span id='c{curr_len}'>{msg}<div class='not_command'>[非指令]</div></span>\n"
    elif is_finished:
        result += f"<span id='c{curr_len}'>{msg}<div class='finished'>[完毕<div class='finished-commands'>({finished_command})</div>]</div></span>\n"
    else:
        if not remaining_command == "" and not curr_command == "放生":
            remaining_command = f" | 剩余：{remaining_command}"
        if curr_command == "放生":
            curr_command = "违规操作"
            remaining_command = message_dict[which_platform]['RELEASE02']
        elif not curr_command == "":
            curr_command = curr_command.replace("L_STICK", "左摇杆")
            curr_command = curr_command.replace("R_STICK", "右摇杆")
            curr_command = f"执行中 -> {curr_command}"

        result += f"<span id='c{curr_len}'>{msg}<div class='running'>[{curr_command}<div class='remaining'>{remaining_command}</div>]</div></span>\n"
    curr_chat.append(result)
    write_to_html(curr_chat)


def write_translation(word, uname):
    if len(word) <= 2:
        exp = ["未找到该词~ (´・ω・｀)"]
    try:
        exp = youdao_translate(word)["basic"]["explains"]
    except:
        try:
            exp = youdao_translate(word)["translation"]
        except:
            exp = ["未找到该词~ (´・ω・｀)"]
    exp_str = f"<red>{word}</red> -> "
    if exp is not None:
        print(exp)
        for i in exp:
            exp_str += i + " | "
        write_to_cat(exp_str[0:-3])


def get_white_list():
    f = open(txts_path + "white_list.txt", "r", encoding='utf-8')
    lines = f.readlines()
    uids = []
    for line in lines:
        uids.append(int(line.rstrip()))
    f.close()
    return uids


def init_all_gift_by_day():
    gifts = {}
    for a in range(32):
        gifts[str(a)] = 0

    record_gift_by_day(gifts)


def init_all_gift_by_day_user():
    gifts = {}
    for a in range(32):
        gifts[str(a)] = {}

    record_gift_by_day_user(gifts)


def calc_danmu_to_list():
    f = open(txts_path + "all_danmu_b.txt", "r", encoding='utf-8')
    lines = f.readlines()
    user_dict = {}
    for line in lines:
        line_ = line.rstrip()
        user = line_.split('：')[0]
        if "赠送" in line_ and "（" in line:
            continue
        if user not in user_dict:
            user_dict[user] = 0
        user_dict[user] += 1
    f.close()
    user_tuple = sorted(user_dict.items(), key=lambda e: e[1], reverse=True)
    print(user_tuple)
    f_string = ""
    for item in user_tuple:
        f_string += item[0] + ":" + str(item[1]) + "\n"
    with open(txts_path + 'user_danmu_lines.json', 'w', encoding='utf-8') as f:
        f.write(f_string)
