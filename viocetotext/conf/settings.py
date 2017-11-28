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

token_url = baidu_server+"grant_type="+grant_type+"&client_id="+api_key+"&client_secret="+secret_key

getvoice_url = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s"

VOICE_RATE = 8000
WAVE_FILE = "8k.wav"
USER_ID = "user_test"
WAVE_TYPE = "wav"
LANGUE = "zh"