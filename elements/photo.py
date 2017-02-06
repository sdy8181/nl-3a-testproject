# -*- coding: utf-8 -*-
"""
Created on 2/3/17
@author: 欧光乾
@email: guangqianou@pateo.com.cn
"""
from utils.helpTools import d
from utils.uiTools import uit


class Photo:
    """
    图片应用的操作
    """
    def __init__(self):
        """
        初始化图片的包名
        """
        self.__pkg_name = 'com.pateo.as.photo'

    def get_photo_folder_gridview(self):
        """
        获取图片文件夹列表视图
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/gridview')

    def get_photo_folder_by_name(self, folder_name):
        """
        根据文件夹名称获取图片文件夹
        :param folder_name:
        :return:
        """

        folder_search_txt = folder_name + ' ('
        # 获取文件夹列表视图控件
        grid_view_ele = self.get_photo_folder_gridview()
        if not grid_view_ele.wait.exists():
            uit.raise_Exception_info('图片列表视图控件不存在')
        else:
            # 滑动到指定文件夹 没有则抛出异常
            folder_exists_flag = grid_view_ele.scroll.vert.to(
                    textContains=folder_search_txt)
            if folder_exists_flag:
                return d(textContains=folder_search_txt)
            else:
                uit.raise_Exception_info('指定图片文件夹不存在')

    def get_photo_gridview(self):
        """
        获取图片列表视图
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/id_coverflow')

    def get_photo_by_name(self, photo_name):
        """
        根据图片名称查找图片并返回图片对象, 查找失败抛出异常
        :param photo_name:
        :return:
        """
        photo_listview_ele = self.get_photo_gridview()
        if not photo_listview_ele.wait.exists():
            uit.raise_Exception_info('图片列表视图不存在')
        else:
            photo_flag = photo_listview_ele.scroll.vert.to(text=photo_name)
            if photo_flag:
                return d(text=photo_name)
            else:
                uit.raise_Exception_info('没有找到指定图片文件')

    def get_photo_preview_prev(self):
        """
        获取图片预览界面的上一张图片控件
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/id_toolbar_btn_prev')

    def get_photo_preview_next(self):
        """
        获取图片预览界面的下一张图片控件
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/id_toolbar_btn_next')

    def get_photo_preview_del(self):
        """
        获取图片删除按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/id_toolbar_btn_delete')

    def get_photo_preview_fullscreen(self):
        """
        获取图片预览界面的全屏控件
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/id_toolbar_btn_fullscreen')

    def get_photo_preview_name(self):
        """
        获取图片预览界面的图片名称
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/id_photo_name')

    def get_photo_preview_image_ele(self):
        """
        获取图片查看界面元素控件
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/id_photo_image')


photo = Photo()





