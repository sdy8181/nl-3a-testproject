# -*- coding: utf-8 -*-
"""
Created on 1/6/17
@author: 欧光乾
@email: guangqianou@pateo.com.cn
"""

from utils.helpTools import d
from utils.uiTools import uit


class Video:
    """
    视频应用的元素控件获取
    """
    def __init__(self):
        """
        初始化视频应用的包名
        """
        self.__pkg_name = 'com.pateo.video'

    def get_video_grid_view(self):
        """
        获取视频列表视图控件
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/videoList')

    def get_video_by_name(self, video_name):
        """
        根据视频名称获取视频控件并返回
        :param video_name:
        :return:
        """
        grid_view_ele = self.get_video_grid_view()
        if grid_view_ele.wait.exists():

            video_flag = grid_view_ele.scroll.vert.to(text=video_name)
            if video_flag:
                return d(text=video_name)
            else:
                uit.raise_Exception_info('没有找到指定视频')
        else:
            uit.raise_Exception_info('视频视图不存在')

    def get_video_prev_btn(self):
        """
        获取上一个视频按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/prevBtn')

    def get_video_next_btn(self):
        """
        获取下一个视频按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/nextBtn')

    def get_video_play_btn(self):
        """
        获取视频播放或者暂停控件
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/playBtn')

    def get_video_play_view_ele(self):
        """
        获取视频播放视图
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/video_view')

    def get_video_name_ele(self):
        """
        获取当前视频名称控件
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/video_name')

    def get_video_list_btn(self):
        """
        获取视频列表按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/listBtn')

    def get_video_bottom_back_btn(self):
        """
        获取视频底部返回按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/as_bar_back_id')

    def get_video_bottom_home_btn(self):
        """
        获取视频底部主页按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/as_bar_home_id')


video = Video()
