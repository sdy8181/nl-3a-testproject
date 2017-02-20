# -*- coding: UTF-8 -*-
"""
Created on 2017/2/17
@author: wangzhiyuan
@email: zhiyuanwang@pateo.com.cn
"""
from utils.helpTools import d


class OnCall:
    def __init__(self):
        pass

    def get_oncall_outing(self):
        return d(textContains='正在发送数据')

    def get_oncall_status(self):
        return d(text='通话中...')


    def get_oncall_endcalling(self):
        return d(resouceId='com.pateo.as.xcall:id/call_end_button')


    def get_oncall_back(self):
        return d(resourceId='com.pateo.as.xcall:id/bottombar_back_button')


    def get_oncall_deviceerror(self):
        return d(textContains='启动失败')


oncall = OnCall()