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
    base_path = os.path.abspath('../lib')
    test_file_path = os.path.join(base_path, settings.WAVE_FILE)
    if not file_path :
        file_path = test_file_path

    data_result = get_response(settings.WAVE_TYPE,settings.VOICE_RATE,settings.USER_ID,get_token(settings.url),get_voice(file_path),get_size(file_path))

    if data_result['err_msg'] == 'success.':
        print "语音结果：" + data_result['result'][0].encode('utf-8')
    else:
        print data_result


if __name__ == '__main__':
    main()