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
from utils.helpTools import ht
from utils.uiTools import uit
from utils.helpTools import d, d_height, d_width

# 底部控制栏上各APP坐标，统一定义维护
Bottom_App_Coord = {
    '导航': (236, 670),
    '电话': (438, 670),
    '收音机': (640, 670),
    '多媒体': (842, 670),
    '天气': (1044, 670),
}


class Common:
    def back_to_launcher(self):
        '''
        回到主界面
        :desription: 根据当前报名判断回到主界面的方法，然后调用相应方法回到主界面
        :return:
        '''

        d.press.home()
        # 判断是否在第一屏
        while not d(text='媒体').wait.exists():
            d.swipe(0, d_height / 2, d_width, d_height / 2, 20)

    def connect_special_wifi(self, ssid, pwd):
        '''
        用于持续集成中使用，方便自动连接无线网
        :param ssid: 无线网名称
        :param pwd: 无线网密码
        :return:
        '''
        pass

    def get_current_package_name(self):
        """
        获取当前应用
        :return:
        """
        current_package_name = d.info['currentPackageName']
        if current_package_name == 'com.pateo.launcher':
            return '主页'
        elif current_package_name == 'com.pateo.as21.music':
            return '音乐'
        elif current_package_name == 'com.pateo.radio':
            return '收音机'
        elif current_package_name == 'com.pateo.video':
            return '视频'
        elif current_package_name == 'com.pateo.as.btphone' or \
                        current_package_name == 'com.pateo.as.contacts':
            return '蓝牙电话'
        elif current_package_name == 'com.pateo.as.photo':
            return '图片'
        else:
            raise Exception('当前应用未加入脚本，请联系维护人员')

    # 点击底部控制栏上的APP

    def click_bottom_app(self, text):
        '''
        点击底部控制栏各个应用
        :param text: 应用名称，eg“导航”
        :return:
        '''
        if text.strip() in Bottom_App_Coord.keys():
            x, y = Bottom_App_Coord[text]
            d.click(x, y)
        else:
            uit.raise_Exception_info("输入的底部应用未找到")


com = Common()
