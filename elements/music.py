# -*- coding: UTF-8 -*-
"""
Created on 11/1/16
@author: 欧光乾
@email: guangqianou@pateo.com.cn
"""
from utils.helpTools import d
from utils.uiTools import uit


class Music:
    def __init__(self):
        self.__pkg_name = "com.pateo.as21.music"  # 初始化应用包名

    def get_music_usb_btn(self):
        """
        获取U盘音乐按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/usb_text')

    def get_music_bt_btn(self):
        """
        获取蓝牙音乐按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/bluetooth_text')

    def get_music_mylove_btn(self):
        """
        获取最爱音乐按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/mylove_text')

    def get_music_name_ele(self):
        """
        获取音乐名称
            -- 先获取timeInfo控件
            -- 根据timeInfo控件获取当前播放的音乐名字
        :return:
        """
        # 获取timeInfo控件
        time_info = d(resourceId=self.__pkg_name + ':id/timeInfo')
        if time_info.wait.exists():
            return time_info.sibling(resourceId=self.__pkg_name + ':id/musicName')
        else:
            return d(resourceId=self.__pkg_name + ':id/musicName')

    def get_music_artist_name_ele(self):
        """
        获取音乐歌手名称
            -- 先获取timeInfo控件
            -- 根据timeInfo控件获取当前播放的音乐名字
        :return:
        """
        # 获取timeInfo控件
        time_info = d(resourceId=self.__pkg_name + ':id/timeInfo')
        if time_info.wait.exists():
            return time_info.sibling(resourceId=self.__pkg_name + ':id/artistName')
        else:
            return d(resourceId=self.__pkg_name + ':id/artistName')

    def get_music_play_pause_coordinate(self):
        """
        获取音乐播放或者暂停坐标
        :return:
        """
        if d(resourceId=self.__pkg_name + ':id/musicCoverFlow').wait.exists():
            return uit.get_clickcoord_from_bounds(resourceId=self.__pkg_name + ':id/musicCoverFlow')
        else:
            return uit.get_clickcoord_from_bounds(resourceId=self.__pkg_name + ':id/musicName')

    def get_music_artists_list_btn(self):
        """
        获取歌手列表
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/searchartistBtn')

    def get_music_album_list_btn(self):
        """
        获取专辑列表
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/searchalbumBtn')

    def get_music_folder_list_btn(self):
        """
        获取文件夹列表
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/folderBtn')

    def get_music_ivoka_btn(self):
        """
        获取音乐语音按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/ivokaBtn')

    def get_music_bottom_back_btn(self):
        """
        获取音乐底部返回按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/as_bar_back_id')

    def get_music_bottom_home_btn(self):
        """
        获取音乐底部主页按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/as_bar_home_id')

    def get_music_prev_btn(self):
        """
        获取音乐上一首按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/prevBtn')

    def get_music_next_btn(self):
        """
        获取音乐下一首按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/nextBtn')

    def get_music_collect_btn(self):
        """
        获取音乐收藏控件
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/collectBtn')

    def get_music_collect_btn_by_artist(self, artist_name):
        """
        根据歌手信息返回相应收藏控件
        :param artist_name: 歌手
        :return:
        """
        # 获取歌手列表listview
        list_view = d(resourceId=self.__pkg_name + ':id/artist_list')
        if list_view.exists:
            exists_flag = list_view.scroll.vert.to(text=artist_name, resourceId=self.__pkg_name + ':id/artistName')
            if exists_flag:
                artist_ele = d(text=artist_name, resourceId=self.__pkg_name + ':id/artistName')
                return artist_ele.sibling(resourceId=self.__pkg_name + ':id/collectBtn')
            else:
                uit.raise_Exception_info('找不到指定歌手')
        else:
            uit.raise_Exception_info('歌手列表不存在')

    def get_music_collect_btn_by_album(self, album_name):
        """
        根据专辑信息返回相应收藏控件
        :param album_name: 专辑
        :return:
        """
        # 获取专辑列表listview
        list_view = d(resourceId=self.__pkg_name + ':id/album_list')
        if list_view.exists:
            exists_flag = list_view.scroll.vert.to(text=album_name, resourceId=self.__pkg_name + ':id/albumName')
            if exists_flag:
                artist_ele = d(text=album_name, resourceId=self.__pkg_name + ':id/albumName')
                return artist_ele.sibling(resourceId=self.__pkg_name + ':id/collectBtn')
            else:
                uit.raise_Exception_info('找不到指定专辑')
        else:
            uit.raise_Exception_info('专辑列表不存在')

    def get_album_from_album_list_by_album_name(self, album_name):
        """
        获取专辑列表中指定专辑名称的元素
        :param album_name
        :return:
        """
        # 获取收藏列表listview
        list_view = d(resourceId=self.__pkg_name + ':id/album_list')
        if list_view.wait.exists():
            exists_flag = list_view.scroll.vert.to(text=album_name, resourceId=self.__pkg_name + ':id/albumName')
            if exists_flag:
                return d(text=album_name, resourceId=self.__pkg_name + ':id/albumName')
            else:
                uit.raise_Exception_info('找不到指定专辑')
        else:
            uit.raise_Exception_info('专辑列表不存在')

    def get_artist_from_artist_list_by_artist_name(self, artist_name):
        """
        获取歌手列表中指定歌手名称的元素
        :param artist_name
        :return:
        """
        # 获取收藏列表listview
        list_view = d(resourceId=self.__pkg_name + ':id/artist_list')
        if list_view.wait.exists():
            exists_flag = list_view.scroll.vert.to(text=artist_name, resourceId=self.__pkg_name + ':id/artistName')
            if exists_flag:
                return d(text=artist_name, resourceId=self.__pkg_name + ':id/artistName')
            else:
                uit.raise_Exception_info('找不到指定歌手')
        else:
            uit.raise_Exception_info('歌手列表不存在')

    def get_music_collect_btn_by_collect(self, collect_name):
        """
        根据收藏列表标题信息返回相应收藏控件
        :param collect_name: 收藏列表标题
        :return:
        """
        # 获取收藏列表listview
        list_view = d(resourceId=self.__pkg_name + ':id/collect_list')
        if list_view.exists:
            exists_flag = list_view.scroll.vert.to(text=collect_name, resourceId=self.__pkg_name + ':id/musicName')
            if exists_flag:
                artist_ele = d(text=collect_name, resourceId=self.__pkg_name + ':id/musicName')
                return artist_ele.sibling(resourceId=self.__pkg_name + ':id/collectBtn')
            else:
                uit.raise_Exception_info('找不到指定收藏标题')
        else:
            uit.raise_Exception_info('收藏列表不存在')

    def get_music_from_collect_list_by_music_name(self, music_name):
        """
        获取收藏列表中指定音乐名称的元素
        :param music_name:
        :return:
        """
        # 获取收藏列表listview
        list_view = d(resourceId=self.__pkg_name + ':id/collect_list')
        if list_view.wait.exists():
            exists_flag = list_view.scroll.vert.to(text=music_name, resourceId=self.__pkg_name + ':id/musicName')
            if exists_flag:
                return d(text=music_name, resourceId=self.__pkg_name + ':id/musicName')
            else:
                uit.raise_Exception_info('找不到指定音乐')
        else:
            uit.raise_Exception_info('收藏列表不存在')

    def get_music_album_from_collect_list_by_music_name(self, music_name):
        """
        获取收藏列表中指定音乐的专辑名
        :param music_name:
        :return:
        """
        ele = self.get_music_from_collect_list_by_music_name(music_name)
        if ele.wait.exists():
            return ele.sibling(resourceId=self.__pkg_name + ':id/albumName')
        else:
            uit.raise_Exception_info('指定收藏音乐不存在')

    def get_music_artist_from_collect_list_by_music_name(self, music_name):
        """
        获取收藏列表中指定音乐的歌手名
        :param music_name:
        :return:
        """
        ele = self.get_music_from_collect_list_by_music_name(music_name)
        if ele.wait.exists():
            return ele.sibling(resourceId=self.__pkg_name + ':id/artistName')
        else:
            uit.raise_Exception_info('指定收藏音乐不存在')

    def get_music_share_btn(self):
        """
        获取音乐界面的分享至U盘按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/shareBtn')

    def get_music_play_btn(self):
        """
        获取音乐播放按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/playBtn')

    def get_music_cur_time_ele(self):
        """
        获取音乐当前播放时间
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/current_time')

    def get_artist_collect_status_from_artist_list_by_name(self, artist_name):
        """
        获取指定歌手名称是否在歌手列表中
        :param artist_name:
        :return: True: 已收藏, False: 未收藏
        """
        # 获取收藏列表listview
        list_view = d(resourceId=self.__pkg_name + ':id/artist_list')
        if list_view.exists:
            exists_flag = list_view.scroll.vert.to(text=artist_name, resourceId=self.__pkg_name + ':id/artistName')
            return exists_flag
        else:
            uit.raise_Exception_info('收藏列表不存在')


    def get_album_collect_status_from_album_list_by_name(self, album_name):
        """
        获取指定专辑名称是否在专辑列表中
        :param album_name:
        :return: True: 已收藏, False: 未收藏
        """
        # 获取收藏列表listview
        list_view = d(resourceId=self.__pkg_name + ':id/album_list')
        if list_view.exists:
            exists_flag = list_view.scroll.vert.to(text=album_name, resourceId=self.__pkg_name + ':id/albumName')
            return exists_flag
        else:
            uit.raise_Exception_info('收藏列表不存在')

    def get_music_collect_status_from_collect_list_by_name(self, music_name):
        """
        获取指定音乐名称是否在收藏列表中
        :param music_name:
        :return: True: 已收藏, False: 未收藏
        """
        # 获取收藏列表listview
        list_view = d(resourceId=self.__pkg_name + ':id/collect_list')
        if list_view.exists:
            exists_flag = list_view.scroll.vert.to(text=music_name, resourceId=self.__pkg_name + ':id/musicName')
            return exists_flag
        else:
            uit.raise_Exception_info('收藏列表不存在')

    def get_music_play_status_from_collect_list_by_name(self, music_name):
        """
        从收藏列表中获取音乐的播放状态
        :param music_name:
        :return: True: 播放中 ， False: 暂停或者没有播放
        """
        # 获取收藏列表listview
        list_view = d(resourceId=self.__pkg_name + ':id/collect_list')
        if list_view.exists:
            exists_flag = list_view.scroll.vert.to(text=music_name, resourceId=self.__pkg_name + ':id/musicName')
            if exists_flag:
                ele = d(text=music_name, resourceId=self.__pkg_name + ':id/musicName')
                return ele.sibling(resourceId=self.__pkg_name + ':id/playStateIcon').exists
            else:
                uit.raise_Exception_info('指定音乐在收藏列表中不存在')
        else:
            uit.raise_Exception_info('收藏列表不存在')

    def get_music_search_ele(self):
        """
        获取音乐列表中的搜索框控件
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/searchContent')


# 创建对象
music = Music()
