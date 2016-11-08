# -*- coding: UTF-8 -*-
'''
Created on 11/1/16
@author: 欧光乾
@email: guangqianou@pateo.com.cn
'''
import os
import platform
import time
import serial
from elements.audio import Audio
from utils.helpTools import ht
from utils.uiTools import uit
from utils.helpTools import d


class Common:

    def back_to_launcher(self):
        '''
        回到主界面
        :desription: 根据当前报名判断回到主界面的方法，然后调用相应方法回到主界面
        :return:
        '''
        pass

    # 播放语音文件唤醒应用
    def ivoka_start_app(self, voice_name):
        ivoka_flag = False

        ht.play_voice('你好语音助理.m4a')
        ele = d(text='你好，请说')
        ele1 = d(text='没听清，请再说一次')
        loop = 0
        while (loop <= 3) and (not ivoka_flag):
            if ele.wait.exists(timeout=8000):
                ht.play_voice(voice_name)
                ivoka_flag = True

                if ele1.wait.exists(timeout=8000):
                    ht.play_voice(voice_name)
                    ivoka_flag = True
            else:
                ht.play_voice('你好语音助理.m4a')
                loop += 1

        if not ivoka_flag:
            uit.raise_Exception_info('ivoka唤醒失败')


    def connect_special_wifi(self, ssid, pwd):
        '''
        用于持续集成中使用，方便自动连接无线网
        :param ssid: 无线网名称
        :param pwd: 无线网密码
        :return:
        '''
        pass

