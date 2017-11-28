#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/28/2017 10:47 AM
# @Author  : Siyuan(Saiun)
# @Site    : 
# @File    : settings.py.py
# @Software: PyCharm Community Edition


baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
grant_type = "client_credentials"
api_key = "eUxwP1Xud8hmEMw3gZnlcG4y"
secret_key = "6b5dea0df4d8fff8c5608dad356ec5c4"

url = baidu_server+"grant_type="+grant_type+"&client_id="+api_key+"&client_secret="+secret_key


#设置音频属性，根据百度的要求，采样率必须为8000，压缩格式支持pcm（不压缩）、wav、opus、speex、amr
VOICE_RATE = 8000
WAVE_FILE = "8k.wav" #音频文件的路径
USER_ID = "user_test" #用于标识的ID，可以随意设置
WAVE_TYPE = "wav"