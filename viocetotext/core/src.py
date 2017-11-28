#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/28/2017 10:47 AM
# @Author  : Siyuan(Saiun)
# @Site    : 
# @File    : src.py.py
# @Software: PyCharm Community Edition

import urllib2
import json
import base64
import  os

def get_voice(file_path):
    with open(file_path, 'rb') as f:
        speech =  base64.encodestring(f.read()).replace('\n', '')
    return speech

def get_size(file_path):
    return os.path.getsize(file_path)


def get_token(url):
    res = urllib2.urlopen(url).read()
    data = json.loads(res)
    return data["access_token"]

def get_response(wave_type,vocie_rate,user_id,token,speech, size):
    update_info = json.dumps(
        {"format":wave_type, "rate":vocie_rate, 'channel':1,'cuid':user_id,'token':token,'speech':speech,'len':size})
    headers = {'Content-Type': 'application/json'}
    url = "http://vop.baidu.com/server_api"
    req = urllib2.Request(url, update_info, headers)
    text = urllib2.urlopen(req)
    return json.load(text)
