# -*- coding: utf-8 -*-
'''
Created on 11/28/16
@author: 欧光乾
@email: guangqianou@pateo.com.cn
'''
from utils.helpTools import d


class Home:
    def __init__(self):
        self.__pkg_name = 'com.pateo.launcher'

    def get_music_play_pause_btn(self):
        '''
        获取主页音乐播放暂停按钮
        :return:
        '''
        return d(resourceId=self.__pkg_name + ':id/playPause')

    def get_music_next_btn(self):
        '''
        获取主页音乐播放下一首按钮
        :return:
        '''
        return d(resourceId=self.__pkg_name + ':id/next')

    def get_music_prev_btn(self):
        '''
        获取主页音乐播放上一首按钮
        :return:
        '''
        return d(resourceId=self.__pkg_name + ':id/prev')

    def get_music_info_ele(self):
        '''
        获取主页音乐信息
        :return:
        '''
        return d(resourceId=self.__pkg_name + ':id/album_info')

    def get_home_date_ele(self):
        """
        获取主页上的日期元素
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/date')

    def get_home_week_ele(self):
        """
        获取主页上的星期元素
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/week')

    def get_home_multimediaLayout_ele(self):
        """
        获取主页音乐布局
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/multimediaLayout')



# 初始化对象
home = Home()
