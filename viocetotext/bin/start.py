#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/28/2017 10:46 AM
# @Author  : Siyuan(Saiun)
# @Site    : 
# @File    : start.py.py
# @Software: PyCharm Community Edition


import sys
from viocetotext.conf import settings
from viocetotext.core.src import *

def main(file_path=None):
    base_path = os.path.abspath('../lib/voice')
    test_file_path = os.path.join(base_path, settings.WAVE_FILE)
    if not file_path :
        file_path = test_file_path

    vioce_file = os.path.join(os.path.abspath("../lib/voice"),"out.mp3")
    token = get_token(settings.token_url)

    get_voice("大家好!我来自中国上海",vioce_file,settings.getvoice_url,settings.USER_ID,token)

    data_result = get_response(settings.WAVE_TYPE,settings.VOICE_RATE,
                               settings.USER_ID,token,
                               get_speech(file_path),
                               get_size(file_path),
                               settings.LANGUE)

    if data_result['err_msg'] == 'success.':
        print("语音结果：\n" + data_result['result'][0])
    else:
        print(data_result)


if __name__ == '__main__':
    main()