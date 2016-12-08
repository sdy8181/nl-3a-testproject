# -*- coding: utf-8 -*-
'''
Created on 11/1/16
@author: 欧光乾
@email: guangqianou@pateo.com.cn
'''

import os
import platform
import time
import serial
from PIL import Image

from utils.helpTools import ht
from utils.helpTools import d

class UiTools:

    def take_screenshot(self):
        '''
        截图
        :return: 截图保存路径
        '''
        file_name = time.strftime('%Y%m%d%H%M%S') + '.png'
        log_path = ht.get_conf_value('logPath')
        time_dir = time.strftime('%Y%m%d')

        file_path = os.path.join(log_path, time_dir, 'screenshots', file_name)
        dir_path = os.path.dirname(file_path)

        # 判断目录是否存在, 不存在创建目录
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        d.screenshot(file_path)
        return file_path

    def chk_crash(self):
        '''
        检查是否crash
        :return: True: 有crash， False: 无crash
        '''
        print('开始检查应用是否crash')
        if d(resourceId='android:id/message').wait.exists():
            print('应用crash')
            d(resourceId='android:id/button1').click.wait()
            return True
        else:
            return False

    def raise_Exception_info(self, err_msg=''):
        '''
        抛出异常
        :param err_msg: 自定义异常信息 ,默认为空
        :return:
        '''
        png_path = self.take_screenshot()
        if self.chk_crash():
            raise Exception('应用crash，' + err_msg + '请参考截图信息: file:///' + png_path)
        else:
            raise Exception('用例运行失败，' + err_msg + '请参考截图信息: file:///' + png_path)

    def controlPoweroff(self):
        '''
        模拟拔出U盘
        :return:
        '''
        s = serial.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=None)
        poweroff = '005A560005010000B7'.decode("hex")
        if not s.isOpen():
            s.open()
        s.write(poweroff)
        s.close()

    def controlPoweron(self):
        '''
        模拟插上U盘
        :return:
        '''
        s = serial.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=None)
        poweron = '005A560005010000B6'.decode("hex")
        if not s.isOpen():
            s.open()
        s.write(poweron)
        s.close()

    def get_media_volume(self):
        '''
        获取media音量
        :return:
        '''
        if platform.system() == 'Linux':
            cmd = '''adb  -s ''' + ht.get_conf_value('deviceSerial') + ''' shell "echo 'select * from system;'|sqlite3 /data/data/com.android.providers.settings/databases/settings.db" | grep "volume_music_speaker"'''
        else:
            cmd = '''adb  -s ''' + ht.get_conf_value('deviceSerial') + ''' shell "echo 'select * from system;'|sqlite3 /data/data/com.android.providers.settings/databases/settings.db" | findstr "volume_music_speaker"'''
        volume_ret = os.popen(cmd).read().strip()
        volume_value = volume_ret.split('|')[2].strip()
        print(volume_value)
        return volume_value

    def cutting_device_screenshot(self, file_name, position):
        '''
        根据坐标截屏，保存到指定文件
        :param file_path: 保存的文件名
        :param position: 坐标位置参数
        :return:
        '''
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        diffImages_path = os.path.join(os.path.dirname(cur_dir), 'support', 'diffImages')

        if not os.path.exists(diffImages_path):
            os.mkdir(diffImages_path)

        init_png = os.path.join(diffImages_path, 'raw.png')

        try:
            os.remove(init_png)
        except:
            pass

        d.screenshot(init_png)
        im = Image.open(init_png)

        coordinate = (position['left'], position['top'], position['right'], position['bottom'])
        region = im.crop(coordinate)

        file_path = os.path.join(diffImages_path, file_name)
        try:
            os.remove(file_path)
        except:
            pass

        region.save(file_path)

        return file_path

    def get_clickcoord_from_bounds(self, **kwargs):
        """
        获取指定元素的中心坐标
        :param kwargs:
        :return:
        """
        ele = d(**kwargs)
        if ele.wait.exists():
            bounds = ele.info['bounds']
            x = (bounds['left'] + bounds['right']) / 2
            y = (bounds['bottom'] + bounds['top']) / 2
            return (x, y)
        else:
            self.raise_Exception_info('指定元素不存在')

    def get_clickcoord_by_ele(self, ele):
        """
        获取指定元素的中心坐标
        :param ele: 元素对象
        :return:
        """
        bounds = ele.info['bounds']
        x = (bounds['left'] + bounds['right']) / 2
        y = (bounds['bottom'] + bounds['top']) / 2
        return x, y

uit = UiTools()
# ele = d(resourceId='com.pateo.launcher:id/multimediaLayout')
# bounds = ele.info['bounds']
# p1 = uit.cutting_device_screenshot('a.png', bounds)
# time.sleep(10)
# p2 = uit.cutting_device_screenshot('b.png', bounds)
# ret = ht.get_image_diff_data(p1, p2)
# print(ret)

