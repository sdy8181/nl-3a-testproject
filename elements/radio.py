# -*- coding: UTF-8 -*-
'''
Created on 11/28/16
@author: zhiyuanwang
@email: zhiyuanwang@pateo.com.cn
'''
import os
# os.environ['ANDROID_HOME']='/home/pateo/AndroidSDK/android-sdk-linux/'

from utils.helpTools import d,ht
from utils.uiTools import uit



class Radio:

    def __init__(self):
        pass

    ##获取电台类型的控件
    def get_radio_type_icon(self):
        '''
        FM/AM切换按钮，是个imageView
        :return:
        '''
        return d(resourceId='com.pateo.radio:id/bar_radio_type_id')

    ##获取电台频率控件
    def get_radio_frequency_id(self):
        '''
        获取频率区域
        :return: ID
        '''
        return d(resourceId='com.pateo.radio:id/new_frequency_iv')

    #获取电台预览扫描按钮
    def get_radio_scan_icon(self):
        '''
        获取“Scan”控件对象，可点点击
        :return:
        '''
        return d(resourceId='com.pateo.radio:id/bar_radio_preview_id')

    #获取电台自动扫描存台按钮
    def get_radio_AST_icon(self):
        '''
        获取“AST”按钮，可点击
        :return:
        '''
        return d(className='android.widget.Button',resourceId='com.pateo.radio:id/bar_radio_scan_id')

    #获取电台节目列表元素
    def get_radio_FM_listicon(self):
        '''
        获取“电台列表”控件，可点击
        :return:
        '''
        return d(resourceId='com.pateo.radio:id/bar_radio_list_id')

    #获取电台收藏列表
    def get_radio_FM_favorite(self):
        '''
        获取“电台收藏列表”控件，可点击
        :return:
        '''
        return d(resourceId='com.pateo.radio:id/bar_radio_favorite_id')

    #获取添加到收藏按钮
    def get_radio_FM_add2favorite(self):
        '''
        播放界面上添加界面到收藏列表控件
        :return:
        '''
        return d(resourceId='com.pateo.radio:id/new_radio_collect_id')

    #获取收音机ivoka按钮
    def get_radio_FM_ivoka(self):
        '''
        界面上麦克风语音控件，可点击
        :return:
        '''
        return d(resourceId='com.pateo.radio:id/bar_radio_ivoka_id')

    #通过对比控件数判断播放状态
    def get_radio_pause_control_status(self):
        '''
        收音机暂停控件
        :return: play or pause icon
        '''
        ui_layout = list(d(resourceId='com.pateo.radio:id/ui_main_layout'))
        control = list(d(resourceId='com.pateo.radio:id/radio_control_id'))
        return len(ui_layout),len(control)




    #特殊：点击收音机暂停打开区域
    def execute_radio_FM_playorpause(self):
        '''
        收音机播放与暂停点击坐标的动作，注意使用
        :return: 点击动作完成
        '''
        x,y=uit.get_clickcoord_from_bounds(resourceId='com.pateo.radio:id/new_frequency_iv')
        return d.click(x,y)


    # !!!!!注意：点击收音机下一台，需要开发该resoureId
    def execute_radio_FM_next(self):
        '''
        收音机下一台点击坐标，注意使用
        :return: 点击动作完成
        '''
        # x, y = uit.get_clickcoord_from_bounds(resourceId='com.pateo.radio:id/new_frequency_iv_sub')
        return d.click(1035, 414)
    #!!!!!!!!!!
    def execute_radio_FM_prev(self):
        '''
        收音机下一台点击坐标，注意使用
        :return: 点击动作完成
        '''
        # x, y = uit.get_clickcoord_from_bounds(resourceId='com.pateo.radio:id/new_frequency_iv_sub')
        return d.click(250, 414)



    #获取收音机当前频道值
    def get_radio_station_name(self):
        '''
        分析界面，获取当前收音机播放的电台
        :return: eg：’91.5‘
        '''
        try:
            dic = d(resourceId='com.pateo.radio:id/new_frequency_iv').info
        except:
            uit.raise_Exception_info('未找到当前页面上节目控件')
            return ''
        return dic['text']


    #获取下控制栏返回按钮的控件元素
    def get_radio_back_icon(self):
        '''
        界面左下角back按钮控件，
        :return:
        '''
        return d(className='android.widget.Button',resourceId='com.pateo.radio:id/as_bar_back_id')

    #获取下控制栏回到主界面的控件
    def get_radio_to_home(self):
        '''
        底部控制栏，回到主界面的Home控件
        :return:
        '''
        return d(className='android.widget.Button',resourceId='com.pateo.radio:id/as_bar_home_id')


    ##获取滚动电台列表的list属性（可点击可scroll）
    def get_radio_lists_object(self):
        '''
        获取列表本身的对象，具有滚动属性
        :return:
        '''
        return d(className='android.widget.ListView',resourceId='com.pateo.radio:id/radio_info',scrollable=True)

    ##获取滚动电台列表的list属性到指定电台
    def get_radio_lists_frequency(self,text):
        '''
        在节目单中找到指定频率的节目
        :param text: eg: ‘91.5’
        :return: uiobject of 91.5’
        '''
        return d(className='android.widget.ListView', resourceId='com.pateo.radio:id/radio_info', scrollable=True).\
            child_by_text(text,className='android.widget.TextView',allow_scroll_search=True)


    ##获取电台（和收藏）列表中FM与AM切换控件
    def get_radio_list_FM2AM_switch(self):
        '''
        列表中FM与AM切换的控件，可点击
        :return: 控件
        '''
        return d(resourceId='com.pateo.radio:id/switch_type')


    ##收音机“正在扫描电台频道”判断
    def get_radio_AST_text(self):
        '''
        在当前界面上找扫描台的字符，返回此对象
        :return:
        '''
        return d(text='正在扫描电台频道, 请稍候...',className='android.widget.TextView')


    ##收音机电台预览执行判断
    def get_radio_preview_text(self):
        '''
        在当前界面上找预览台的字符，返回此对象
        :return:
        '''
        return d(text='正在进行电台预览, 请稍候...',className='android.widget.TextView')


    ##收音机天线异常，扫描后电台为空
    def get_radio_scanresult_null(self):

        return d(text='扫描后电台为空',className='android.widget.TextView')


    #判断radio给定的频道是否存在
    def judge_radio_station_name(self,name):
        '''
        :param name: 给定的电台频率eg：91.5
        :return: 存在返回True，或者False
        '''
        return d(text=name).exists

    #获取电台列表中第一个电台的名称
    def get_radio_list_first_name(self):
        '''
        在list中找第一个子元素，获取第一个节目频道
        :return: 列表第一个电台的名字，eg：91.5
        '''
        ele=d(className='android.widget.ListView',resourceId='com.pateo.radio:id/radio_info').child(index=0)
        try:
            dic = ele.child(resourceId='com.pateo.radio:id/radio_list_frequency_name',className='android.widget.TextView').info
        except:
            uit.raise_Exception_info('未找到列表第一列元素')
            return ''
        return dic['text']


    ##获取电台收藏控件标记状态（有未收藏）
    def get_radio_collect_status(self):
        '''
        :return:
        '''
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        diffImages_path = os.path.join(os.path.dirname(cur_dir), 'support', 'diffImages')
        bds = d(resourceId='com.pateo.radio:id/new_radio_collect_id').info['bounds']
        filename = uit.cutting_device_screenshot('collect?.png',bds)
        tmp1 = ht.get_image_diff_data(filename,diffImages_path+'/uncollect.png')
        tmp2 = ht.get_image_diff_data(filename,diffImages_path+'/collected.png')

        if tmp1==0:
            return -1
        elif tmp2 == 0:
            return 1
        else:
            uit.raise_Exception_info('截屏对比收藏节目异常，请查看')




radio = Radio()

