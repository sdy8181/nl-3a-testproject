# -*- coding: utf-8 -*-
'''
Created on 11/1/16
@author: 欧光乾
@email: guangqianou@pateo.com.cn
'''
import os
import time
import math
import platform
import operator
import subprocess
from PIL import Image
from functools import reduce
from uiautomator import Device, Adb
from configparser import ConfigParser

# DEVICE_IP = "192.168.95.2:5578"


TIME_OUT = 5000  # 超时时间
LONG_TIME_OUT = 30000  # 超时时间
# 定义全局变量初始化
global MAP_VAR
MAP_VAR = {}


class HelpTools:

    def initWifiADB(self):

        '''
            通过wifi方式建立adb连接，避免了通过usb连接adb繁琐的设置以及无法使用user版本
             环境：PC与车机同一个局域网
        adb.exe需要同一个进程调用，不然会被打断，所以统一用uiautomator方法初始化
        '''

        adb = Adb()
        try:
            line = adb.raw_cmd("connect", self.get_conf_value("deviceIPaddress").strip() + ":5578").communicate()[0].decode("utf-8")
            if "connected to" in line:
                return True
            else:
                raise Exception('Connect to adb fail via wifi ')
        except IOError as e:
            return False
            print(e)

    def get_phone_obj(self):
        '''
        获取设备操作实例
        :return:返回手机对象
        '''

        phone_serialNum = self.get_conf_value('phoneSerial')
        return Device(phone_serialNum)

    def get_device_obj(self):
        '''
        获取设备操作实例
        :return:返回IPDA对象
        '''

        serial_number = self.get_conf_value('deviceSerial')
        return Device(serial_number)

    def unicode_input(self, text):
        '''
        输入中文 采用utf7ime 调用jar包实现中文输入
        :param text: 中文文本信息
        :return: unicode编码
        '''

        cur_dir = os.path.dirname(os.path.realpath(__file__))

        jar_path = os.path.join(os.path.dirname(cur_dir), 'support', 'utf7ime4py.jar')
        unicode_str = os.popen('java -jar ' + jar_path + ' ' + text).read()
        return unicode_str

    def get_cur_tinymix(self):
        '''
        获取当前的放音通道
        :return: 放音通道结果
        '''
        result = os.popen('adb -s ' + self.get_conf_value('deviceSerial') + ' shell tinymix 0').read()
        print('查询的tinymix的结果为: ' + result)
        tmp = str(result).split('>')[1]
        idx = tmp.index('ASP', len('ASP'), len(tmp) - 1)
        ret = tmp[:idx].strip()
        print('获取当前的放音通道为: ' + ret)
        return ret

    # 播放音乐
    def play_voice(self, voice_name):
        cmd = self.get_conf_value('player') + ' ' + os.path.join(self.get_conf_value('voiceDir'), voice_name)
        os.popen(cmd)

    def get_conf_value(self, key):
        '''
        获取配置文件的值
        :param key: 配置项名称
        :return: 配置项的值
        '''

        cur_dir = os.path.dirname(os.path.realpath(__file__))
        ini_path = os.path.join(os.path.dirname(cur_dir), 'support', 'config.ini')

        cf = ConfigParser()
        cf.read(ini_path)
        ret_val = cf.get('baseconf', key)
        # print('获取配置项《' + key + '》的值为: ' + ret_val)
        return str(ret_val)

    def get_usb_music(self):
        '''
        获取U盘音乐列表，从配置文件中读取
        :return: USB歌曲列表
        '''

        usbMusic_value = self.get_conf_value('usbMusic')
        usb_music = tuple(usbMusic_value.split(','))
        return usb_music


    def check_is_connected(self, serial_num):
        '''
        校验设备是否USB连接，没有则通过wifi连接ADB
        :param serial_num: 设备序列号
        :return: 连接状态， True: 成功， False: 失败
        '''

        command = 'adb devices'

        res = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).stdout.readlines()
        for s in res:
            s = s.decode().strip()
            if serial_num in s:
                return True
        return self.initWifiADB()


    def get_wifi_conn_status(self):
        '''
        # 获取wifi连接状态
        :return: True: 连接， False: 没有连接
        '''

        device_serial = self.get_conf_value('deviceSerial')

        if platform.system() == 'Linux':
            ret = os.popen('adb -s ' + device_serial + ' shell netcfg | grep wlan0').read()
        else:
            ret = os.popen('adb -s ' + device_serial + ' shell netcfg | findstr wlan0').read()

        while ret.__contains__('  '):
            ret = ret.replace('  ', ' ')

        retList = ret.split(' ')

        print(retList[2])

        if retList[2].__contains__('0.0.0.0'):
            print('没有连接wifi')
            return False
        else:
            print('已经连接wifi')
            return True

    def get_image_diff_data(self, image1, image2):
        '''
        比对图片
        :param image1:
        :param image2:
        :return: 差异数据:比对数据越大，图片越不一致
        '''
        # get init image
        img1 = Image.open(image1)
        img2 = Image.open(image2)

        h1 = img1.histogram()
        h2 = img2.histogram()

        result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
        return result

ht = HelpTools()
d = ht.get_device_obj()
p = ht.get_phone_obj()

if __name__ == '__main__':
    print(LONG_TIME_OUT)
