# -*- coding: utf-8 -*-

import asyncio
import os
import sys
import blivedm
import joycon
from codec_constants import JOYCON_DICT
import time

from image_handler import check_if_in_pokemon, check_if_in_menu, check_if_home, check_if_release_pokemon
from file_handler import *
from command_handler import calculate_keyboard, buttons_to_text, directional_commands, msg_handler, macro_msg_handler, \
    init_msg_handler, clean_ur_command

import irc.bot
import requests
import threading
import traceback
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Shanghai')
os.system('color')
joycon = joycon.JoyconManager(0)

clockwise = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0],
             [-1, -1], [0, -1]]
counterclockwise = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0],
                    [-1, -1], [0, -1]]
counterclockwise.reverse()

curr_chat = []
curr_chat_info = ["uname", "msg", "uid", "which_platform"]
curr_formatted_msg = ""

sec_button = ""

do_i_release = True
IN_PRESS = False
allow_exec = True

user_gift, gift_sent_users = init_gift()
total_danmu = init_danmu_lines()
silver_times = 0.2
gold_times = 0.6

macro_dict = init_macro()
write_to_file("obs_alert.txt", "")

achievement = {
    "溜了": 21
}
init_cat()
gift_cat_counter = 0

gift_by_day = init_day_gift()
SHORTEST = 3
SHORTER = 5
SHORT = 6
LONG = 10

BUTTON_GAP = 0.05
PAUSE_TIME = 1
remaining_command = ""
white_list = get_white_list()
white_list_commands = {"🏘", "📷", "HOME", "CAPTURE"}
coin_goal = 50000

user_gift_by_day = init_day_gift_user()


def curr_day():
    china_now = datetime.now(tz).day
    return str(china_now)


def base_press(button, rounds=4):
    if button in white_list_commands and curr_chat_info[2] not in white_list:
        return False
    if button == "B" or button == "A" or button == "R" or button == "L":
        check_if_in_pokemon()
    if button == "A" and check_if_release_pokemon():
        update_obs_display_chat(curr_chat_info, curr_chat, False, True, "放生", "")
        return False
    for _ in range(rounds):
        if button in JOYCON_DICT:
            update_obs_display_chat(curr_chat_info, curr_chat, False, True, button, remaining_command)
            joycon.press(button)
        time.sleep(BUTTON_GAP)
    return True


def base_release(button):
    if do_i_release and button in JOYCON_DICT:
        joycon.release(button)


def base_directional(x, y, rounds=7, which_stick="L_STICK"):
    for i in range(rounds):
        if sec_button != "":
            joycon.press(which_stick, x, y)
            joycon.press("B")
            update_obs_display_chat(curr_chat_info, curr_chat, False, True,
                                    f"{which_stick}+{sec_button}",
                                    remaining_command)
        else:
            joycon.press(which_stick, x, y)
            update_obs_display_chat(curr_chat_info, curr_chat, False, True, f"{which_stick}",
                                    remaining_command)
        time.sleep(BUTTON_GAP)


def press(buttons, duration, which_stick, formatted_msg=""):
    global allow_exec, remaining_command
    if_home = check_if_home()
    if if_home and allow_exec:
        allow_exec = False
        base_press("A")
        base_release("A")
        write_to_file("obs_alert.txt", "所有输入已被禁止，这种情况可能由于\n某位超出权限的人来到了主界面\n或者说游戏它崩溃了哦 @(｡･o･)@")
        time.sleep(5)
        print("checing if home")
        if not check_if_home():
            allow_exec = True
            write_to_file("obs_alert.txt", "")
        # write_to_file("obs_alert.txt",
        #              "It seems that the game quits..\nThis is only supposed to happen when the game crashed.\nUnfortunatelly all inputs are blocked for the moment.\nGo get yourself a cup of coffee @(｡･o･)@")
    if not allow_exec:
        if curr_chat_info[2] not in white_list:
            return
        elif not check_if_home():
            write_to_file("obs_alert.txt", "")
            allow_exec = True
    if_in_menu = False
    for button in buttons:
        for i_round in range(button[1]):
            if button[0] in directional_commands:
                if button[0] == "顺":
                    print(f"连续 {button[1]} 次 顺时针")
                    for a in clockwise:
                        base_directional(a[0], a[1], 1, which_stick)
                elif button[0] == "逆":
                    print(f"连续 {button[1]} 次 逆时针")
                    for a in counterclockwise:
                        base_directional(a[0], a[1], 1, which_stick)
                elif button[0] == "P":
                    update_obs_display_chat(curr_chat_info, curr_chat, False, True, "等待",
                                            remaining_command)
                    time.sleep(PAUSE_TIME)
                else:
                    if do_i_release and (
                            which_stick == "DPAD" or check_if_in_menu(duration, which_stick, i_round, if_in_menu)):
                        joycon.release("L_STICK")
                        joycon.release("R_STICK")
                        if_in_menu = True
                        base_directional(directional_commands[button[0]][0],
                                         directional_commands[button[0]][1],
                                         SHORTEST, "L_STICK")
                        base_release("L_STICK")
                        if i_round >= 2:
                            time.sleep(0.08)
                    else:
                        base_directional(directional_commands[button[0]][0],
                                         directional_commands[button[0]][1],
                                         duration, which_stick)
                    if do_i_release:
                        if duration == SHORT or duration == SHORTER:
                            base_release(which_stick)
                            time.sleep(0.2)
            else:
                base_release(which_stick)
                if base_press(button[0]):
                    base_release(button[0])
                    time.sleep(0.76)
                else:
                    return False
            button[1] -= 1
            remaining_command = buttons_to_text(buttons)
            update_obs_display_chat(curr_chat_info, curr_chat, False, True, button[0],
                                    remaining_command)
        if duration == LONG:
            base_release(which_stick)
    base_release(which_stick)
    remaining_command = ""
    update_obs_display_chat(curr_chat_info, curr_chat, True, True, "", remaining_command, formatted_msg)


def handle_msg(msg):
    global IN_PRESS, sec_button, curr_formatted_msg, do_i_release, curr_chat
    if IN_PRESS:
        return
    formatted_msg, buttons = msg_handler(msg)
    curr_formatted_msg = formatted_msg
    if "CLICK" not in curr_chat_info[1].upper() and ((len(msg) > 7 and len(buttons) <= 2) or (
            len(msg) > 15 and len(buttons) <= 6) or len(buttons) == 0):
        print(formatted_msg)
        print(f"该弹幕并非指令，已取消 【{msg}】")
        update_obs_display_chat(curr_chat_info, curr_chat, True, False)
        return
    print(buttons)
    IN_PRESS = True
    which_stick = "L_STICK"
    if "*" in msg or "＊" in msg:
        which_stick = "R_STICK"
    if "#" in msg:
        sec_button = "B"
    if "$" in msg or "转" in msg or "顺" in msg or "逆" in msg:
        do_i_release = False
    if "!" in formatted_msg or "！" in formatted_msg:
        press(buttons, SHORT, which_stick, formatted_msg)
    elif "&" in formatted_msg:
        press(buttons, SHORTER, which_stick, formatted_msg)
    elif "@" in msg:
        msg = msg.replace("@", "")
        press(buttons, 10, "DPAD", formatted_msg)
    else:
        press(buttons, LONG, which_stick, formatted_msg)
    base_release("L_STICK")
    base_release("R_STICK")
    if IN_PRESS:
        IN_PRESS = False
    joycon.release("B")
    sec_button = ""
    if not do_i_release:
        do_i_release = True
        release_all()


def release_all():
    print("releasing all buttons")
    joycon.release("L_STICK")
    joycon.release("R_STICK")
    joycon.release("A")
    joycon.release("B")
    joycon.release("X")
    joycon.release("Y")
    joycon.release("L")
    joycon.release("R")
    joycon.release("ZL")
    joycon.release("ZR")
    joycon.release("LCLICK")
    joycon.release("RCLICK")


def refresh_gift_cat():
    global gift_cat_counter
    gift_cat_counter += 1
    if gift_cat_counter == 10:
        gift_cat_counter = 0
        coin_today = gift_by_day[curr_day()]
        coin_cat_string = f"今日已收到瓜子数：<blue>{coin_today}</blue>"
        if coin_today > coin_goal:
            coin_cat_string += "<br /><green>已经完成目标，感谢你们的支持！</green>"
        else:
            diff = coin_goal - coin_today
            coin_cat_string += f"<br />距离目标还差<dark-red>{diff}个瓜子</dark-red>ㅍ_ㅍ"
        write_to_cat(coin_cat_string)


def on_receive(uname, msg, uid, which_platform):
    global total_danmu, curr_chat_info, curr_chat
    refresh_gift_cat()
    chat_string = f'{uname}：{msg}'
    curr_chat_info = [uname, msg, uid, which_platform]
    print(chat_string)
    if uid != 0:
        append_to_file('all_danmu.txt', chat_string)
    append_obs_display_chat(curr_chat_info, curr_chat)
    msg = init_msg_handler(msg)
    if "反馈" in msg:
        update_obs_display_chat(curr_chat_info, curr_chat, True, False)
        append_to_file("record_danmu.txt", chat_string)
        write_to_cat(f"<green>【{uname}】</green>：<red>{msg}</red> 已被成功记录(╯>д<)╯⁽˙³˙⁾")
    elif "查词" in msg:
        update_obs_display_chat(curr_chat_info, curr_chat, True, False)
        msg = msg.replace("查词", "")
        word = msg.replace(" ", "")
        write_translation(word, uname)
    elif "删除" in msg:
        update_obs_display_chat(curr_chat_info, curr_chat, True, False)
        if "=" in msg:
            macro = msg[msg.find("=") + 1:]
            if uname in macro_dict and macro in macro_dict[uname]:
                del macro_dict[uname][macro]
                record_macro_commands(macro_dict)
    elif "投票" in msg:
        update_obs_display_chat(curr_chat_info, curr_chat, True, False)
        write_to_cat(f"<green>【{uname}】</green>：<red>{msg}</red> 已被成功记录(╯>д<)╯⁽˙³˙⁾")
    elif "=" in msg:
        update_obs_display_chat(curr_chat_info, curr_chat, True, False)
        macro, formatted_msg = macro_msg_handler(msg)
        if formatted_msg != "":
            if uname not in macro_dict:
                macro_dict[uname] = {}
            macro_dict[uname][macro] = formatted_msg
            record_macro_commands(macro_dict)
            write_to_cat(
                f"<green>{uname}</green>：<red>【{macro}】</red> 已被成功记录，等效<red>【{formatted_msg}】</red>_(:3」∠❀)_")
    else:
        if uid in white_list:
            msg = msg.upper()
            msg = msg.replace("HOME", "🏘")
            msg = msg.replace("CAPTURE", "📷")
        else:
            msg = clean_ur_command(msg)
        if uname in macro_dict and msg in macro_dict[uname]:
            msg = macro_dict[uname][msg]
        if "[" in msg and "]" in msg:
            msg = msg[msg.find("[") + 1: msg.find("]")]
            msg = calculate_keyboard(msg)
        handle_msg(msg.replace(" ", ""))
        total_danmu += 1
        total_danmu_write(total_danmu)


def generate_leaderboard(a, user_gift_by_day_sorted):
    try:
        uid = user_gift_by_day_sorted[a][0]
        uname = user_gift_by_day_sorted[a][1][3]
        avatar = bilibili_avatar.fetch_img_src(uid)
        result = f"{a + 1}. <img class='author-face' src='{avatar}'>" + uname + ": " + str(
            user_gift_by_day_sorted[a][1][2]) + "分"
    except:
        result = f"{a + 1}. " + "今天该位置还没有人~"
    return result


def on_receive_gift(uname, uid, coin_type, coin_count, gift_name, gift_count):
    gift_string = f'{uname} 赠送{gift_name}x{gift_count} （{coin_type}币x{coin_count}）'
    print(gift_string)
    append_obs_display_gift([uname, "", uid, "Bilibili"], gift_name, gift_count, curr_chat)
    append_to_file("gifts.txt", gift_string)
    append_to_file('all_danmu.txt', gift_string)
    bilibili_avatar.fetch_uid(uid)
    uid = str(uid)
    gift_string = f"感谢<blue>{uname}</blue>的<red>{gift_count}个{gift_name}！</red>"
    if uname not in gift_sent_users:
        user_gift.append([uname, 0, 0, 0])
        gift_sent_users.append(uname)

    if uid not in user_gift_by_day[curr_day()]:
        user_gift_by_day[curr_day()][uid] = [0, 0, 0, uname]

    if coin_type == "silver":
        position = 1
        gift_string += F"<green>{coin_count}银瓜子</green>"
    else:
        position = 2
        gift_string += F"<green>{coin_count}金瓜子</green>"
    for i in range(len(user_gift)):
        if uname == user_gift[i][0]:
            user_gift[i][position] += coin_count
            user_gift[i][3] = int(
                user_gift[i][1] * silver_times + user_gift[i][2] * gold_times)
    user_gift.sort(key=lambda x: x[3], reverse=True)
    result = ""
    ranking = 0
    user_ranking = 999
    for user_line in user_gift:
        ranking += 1
        if uname == user_line[0]:
            user_ranking = ranking
        result += ",".join(str(x) for x in user_line) + "\n"
    write_to_file("gifts_count.txt", result)
    gift_string += f" | 您在直播间的排名：<blue>{user_ranking}</blue>"
    write_to_cat(gift_string)
    gift_by_day[curr_day()] += coin_count
    record_gift_by_day(gift_by_day)

    curr_user_gift_by_day = user_gift_by_day[curr_day()][uid]
    curr_user_gift_by_day[position - 1] += coin_count
    curr_user_gift_by_day[2] = int(
        curr_user_gift_by_day[0] * silver_times * 3 + curr_user_gift_by_day[1] * gold_times * 3)

    record_gift_by_day_user(user_gift_by_day)

    user_gift_by_day_sorted = sorted(user_gift_by_day[curr_day()].items(), key=lambda e: e[1][2], reverse=True)

    leaderboard_1 = f"<tips><red>【今日应援榜单】</red><br /><purple>{generate_leaderboard(0, user_gift_by_day_sorted)}<br />{generate_leaderboard(1, user_gift_by_day_sorted)}</purple></tips>"
    leaderboard_2 = f"<tips><red>【今日应援榜单】</red><br /><purple>{generate_leaderboard(2, user_gift_by_day_sorted)}<br />{generate_leaderboard(3, user_gift_by_day_sorted)}</purple></tips>"
    # leaderboard_3 = f"{generate_leaderboard(4, user_gift)}<br />{generate_leaderboard(5, user_gift)}"
    write_to_leaderboard(leaderboard_1, "cat_leaderboard_1")
    write_to_leaderboard(leaderboard_2, "cat_leaderboard_2")


def handle_fatal_error(e):
    trace = traceback.format_exc()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    info = f"{curr_chat_info[0]} : {curr_chat_info[1]}  |  {curr_chat_info[2]}"
    print(now)
    append_to_file("errors.txt", now)
    print(info)
    append_to_file("errors.txt", info)
    print(trace)
    append_to_file("errors.txt", trace)
    os.execl(sys.executable, sys.executable, *sys.argv)


on_receive("User", "", 0, "Bilibili")


class MyBLiveClient(blivedm.BLiveClient):
    # 演示如何自定义handler
    _COMMAND_HANDLERS = blivedm.BLiveClient._COMMAND_HANDLERS.copy()

    async def __on_vip_enter(self, command):
        print(command)

    _COMMAND_HANDLERS['WELCOME'] = __on_vip_enter  # 老爷入场

    async def _on_receive_popularity(self, popularity: int):
        # print(f'当前人气值：{popularity}')
        pass

    async def _on_receive_danmaku(self, danmaku: blivedm.DanmakuMessage):
        try:
            on_receive(danmaku.uname, danmaku.msg, danmaku.uid, "Bilibili")
            bilibili_avatar.fetch_uid(danmaku.uid)
        except BaseException as e:
            handle_fatal_error(e)

    async def _on_receive_gift(self, gift: blivedm.GiftMessage):
        try:
            on_receive_gift(gift.uname, gift.uid, gift.coin_type, gift.total_coin, gift.gift_name, gift.num)
        except BaseException as e:
            handle_fatal_error(e)

    async def _on_buy_guard(self, message: blivedm.GuardBuyMessage):
        print(f'{message.username} 购买{message.gift_name}')
        try:
            append_to_file("gifts.txt",
                           f'{message.username} 购买{message.gift_name}')
        except BaseException as e:
            handle_fatal_error(e)

    async def _on_super_chat(self, message: blivedm.SuperChatMessage):
        print(f'醒目留言 ¥{message.price} {message.uname}：{message.message}')


async def main():
    # 139是黑桐谷歌的直播间
    # 如果SSL验证失败就把ssl设为False
    client = MyBLiveClient(617546, ssl=True)
    future = client.start()
    try:
        await future
    finally:
        await client.close()


class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        # Get the channel id, we will need this for v5 API calls
        url = 'https://api.twitch.tv/kraken/users?login=' + channel
        headers = {'Client-ID': client_id,
                   'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()
        self.channel_id = r['users'][0]['_id']

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print('Connecting to ' + server + ' on port ' + str(port) + '...')
        irc.bot.SingleServerIRCBot.__init__(self,
                                            [(server, port, 'oauth:' + token)],
                                            username, username)

    def on_welcome(self, c, e):
        print('Joining ' + self.channel)

        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        # If a chat message starts with an exclamation point, try to run it as a command
        msg = e.arguments[0]
        uname = e.tags[3]["value"]
        on_receive(uname, msg, "Twitch")
        return


def bot():
    bot = TwitchBot("", "",
                    "", "")
    bot.start()


if __name__ == '__main__':
    # t = threading.Thread(target=bot, args=())
    # t.start()
    asyncio.get_event_loop().run_until_complete(main())
