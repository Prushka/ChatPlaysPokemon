import urllib
import random
import hashlib
from urllib.request import urlopen
import sys
import time
import os
import json


def youdao_translate(text, fromLang='auto', toLang='auto'):
    if ('#' in text):
        text = text.replace('#', '')
        text = text.replace(' ', '')
    appKey = ''
    secretKey = ''

    myurl = 'http://openapi.youdao.com/api'
    q = text
    salt = random.randint(1, 65536)

    sign = appKey + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode('utf-8'))
    sign = m1.hexdigest()
    myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = urlopen(myurl)
        response = eval(httpClient.read().decode())

        return response


    except Exception as e:
        print(e)


def outputResult(input):
    attempt = 0
    translate = youdao_translate(input)
    result = translateToNeat(translate)
    while (not "TR" in result and attempt < 3):
        attempt += 1
        print(str(attempt) + 'st Attempt')
        time.sleep(0.3)
        translate = youdao_translate(input)
        result = translateToNeat(translate)
    if ("TR" in result):
        return result
    else:
        return 'nu233' + '\n'


def jsonToString(input):
    return json.dumps(input, ensure_ascii=False)


def neatJson(input):
    parsed = json.loads(input)
    print(json.dumps(parsed, indent=4, sort_keys=True, ensure_ascii=False))


def translateToNeat(translate):
    if translate is None:
        return ""
    result = ""
    if ("basic" in translate):
        if ("uk-phonetic" in translate["basic"]):
            result += "UK:" + jsonToString(
                translate["basic"]["uk-phonetic"]) + "\n"
        if ("us-phonetic" in translate["basic"]):
            result += "US:" + jsonToString(
                translate["basic"]["us-phonetic"]) + "\n"
        if ("explains" in translate["basic"]):
            result += "EX:" + jsonToString(
                translate["basic"]["explains"]) + "\n"
        if ("wfs" in translate["basic"]):
            result += "WF:" + jsonToString(translate["basic"]["wfs"]) + "\n"
    if ("web" in translate):
        result += "WEB:" + jsonToString(translate["web"]) + "\n"
    if ("translation" in translate):
        result += "TR:" + jsonToString(translate["translation"]) + "\n"
    return result
