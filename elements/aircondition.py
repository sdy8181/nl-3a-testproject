# -*- coding: UTF-8 -*-
"""
Created on 10/2/10
@author: wangzhiyuan
@email: zhiyuanwang@pateo.com.cn
"""
from utils.helpTools import d


class Aircondition:
    def __init__(self):
        pass

    def get_home_aircondition_id(self):
        '''
        主界面上的空调响应区域
        :return:
        '''
        return d(resourceId='com.pateo.launcher:id/air_layout')

    def get_home_aircondition_lefttemp(self):
        '''
        主界面上显示左区域的控件
        :return:
        '''
        return d(resourceId='com.pateo.launcher:id/air_view_left_temperature')

    def get_home_aircondition_righttemp(self):
        '''
        主界面上显示右区域的
        :return:
        '''
        return d(resouceId='com.pateo.launcher:id/air_view_right_temperature')

    def get_home_aircondition_mode(self):
        '''
        主界面上显示空调模式
        :return:
        '''
        return d(resourceId='com.pateo.launcher:id/air_view_status')

    def get_aircondition_AC_id(self):
        '''
        空调应用里A/C按钮
        :return:
        '''
        return d(resourceId='com.pateo.airconditioner:id/ac_checkbox')


    def get_aircondition_ACMAX_id(self):
        '''
        空调应用里AC MAX按钮
        :return:
        '''
        return d(resourceId='com.pateo.airconditioner:id/ac_max_checkbox')

    def get_aircondition_cycle(self):
        '''
        空调应用里外循环
        :return:
        '''
        return d(resouceId='com.pateo.airconditioner:id/air_cycle_checkbox')


    def get_aircondition_drefost(self):
        '''
        空调应用里A/C按钮
        :return:
        '''
        return d(resourceid='com.pateo.airconditioner:id/front_defrost_with_leg_checkbox')

    def get_aircondition_dual(self):
        '''
        空调应用里Dual
        :return:
        '''
        return d(resourceId='com.pateo.airconditioner:id/dual_checkbox')

    def get_aircondition_left_temp_up(self):
        '''

        :return:
        '''
        return d(resourceId='com.pateo.airconditioner:id/left_temp_up_button')

    def get_aircondition_left_temp_down(self):
        '''

        :return:
        '''
        return d(resourceId='com.pateo.airconditioner:id/left_temp_down_button')

    def get_aircondition_close(self):
        '''

        :return:
        '''
        return d(resourceId='com.pateo.airconditioner:id/power_checkbox')


    def get_aircondition_front_defrost(self):
        '''
        前挡风玻璃除霜
        :return:
        '''
        return d(resourceId='com.pateo.airconditioner:id/front_defrost_checkbox')


    def get_aircondition_rear_defrost(self):
        '''
        后玻璃和倒车镜除霜
        :return:
        '''
        return d(resourceId='com.pateo.airconditioner:id/rear_defrost_checkbox')
