# -*- coding: utf-8 -*-
"""
Created on 1/9/17
@author: 欧光乾
@email: guangqianou@pateo.com.cn
"""

from utils.helpTools import d
from utils.uiTools import uit


class Process:
    """
    应用进程管理
    """

    def __init__(self):
        """
        初始化进程管理的包名
        """
        self.__pkg_name = 'com.android.systemui'

    def get_processes_view(self):
        """
        获取进程视图列表
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/processes_view')

    def get_process_eles(self):
        """
        获取进程控件
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/kill_process_layout')

    def get_process_name_eles(self):
        """
        获取进程名称控件
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/process_name')

    def get_process_kill_it_eles(self):
        """
        获取进程上面的关闭控件
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/kill_it')

    def get_kill_process_btn_by_name(self, process_name):
        """
        根据名字获取关闭进程控件
        :param process_name:
        :return:
        """
        process_view = self.get_processes_view()
        if process_view.scroll.vert.to(text=process_name):
            process_name_ele_list = self.get_process_name_eles()
            kill_it_ele_list = self.get_process_kill_it_eles()
            for i in range(len(process_name_ele_list)):
                if process_name_ele_list[i].text.strip() == process_name:
                    return kill_it_ele_list[i]

            # process_layout = self.get_process_eles()
            # for p in process_layout:
            #     if p.child_by_text(process_name).exists:
            #         kill_it = p.child(resourceId=self.__pkg_name + ':id/kill_it')
            #         return kill_it
            else:
                uit.raise_Exception_info('没有找到指定进程关闭控件')
        else:
            uit.raise_Exception_info('没有找到指定进程')


process = Process()
