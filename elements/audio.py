# -*- coding: UTF-8 -*-
'''
Created on 11/1/16
@author: 欧光乾
@email: guangqianou@pateo.com.cn
'''
from utils.helpTools import d

class Audio:

    def __init__(self):

        self.pkg_name = "com.qinggan.app.music"  # 初始化应用包名

    def get_audio_search_ele(self):
        '''
        获取音乐搜索控件
        :return:
        '''
        return d(resourceId=self.pkg_name + ':drawable/menu_selector_search')

# 创建对象
audio = Audio()










