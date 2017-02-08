# -*- coding: utf-8 -*-
"""
Created on 2/8/17
@author: 欧光乾
@email: guangqianou@pateo.com.cn
"""
import time

from utils.helpTools import d
from utils.uiTools import uit


class BtPhone:
    """
    蓝牙电话界面元素获取
    """
    def __init__(self):
        """
        初始化蓝牙电话包名
        """
        self.__pkg_name = 'com.pateo.as.btphone'
        self.__pkg_name_contact = 'com.pateo.as.contacts'

    def get_phone_contacts_tab_ele(self):
        """
        获取通讯录tab控件
        :return:
        """
        return d(resourceId=self.__pkg_name_contact + ':id/contacts_text')

    def get_phone_calllog_tab_ele(self):
        """
        获取最近通话tab控件
        :return:
        """
        return d(resourceId=self.__pkg_name_contact + ':id/calllog_text')

    def get_phone_dial_tab_ele(self):
        """
        获取拨号键盘tab
        :return:
        """
        return d(resourceId=self.__pkg_name_contact + ':id/dial_text')

    def dial_phone_number(self, phone_number):
        """
        输入要拨打的号码
        :param phone_number:
        :return:
        """
        time.sleep(2)

        for c in phone_number:
            if c == '1':
                d(resourceId=self.__pkg_name_contact + ':id/one').click()
            elif c == '2':
                d(resourceId=self.__pkg_name_contact + ':id/two').click()
            elif c == '3':
                d(resourceId=self.__pkg_name_contact + ':id/three').click()
            elif c == '4':
                d(resourceId=self.__pkg_name_contact + ':id/four').click()
            elif c == '5':
                d(resourceId=self.__pkg_name_contact + ':id/five').click()
            elif c == '6':
                d(resourceId=self.__pkg_name_contact + ':id/six').click()
            elif c == '7':
                d(resourceId=self.__pkg_name_contact + ':id/seven').click()
            elif c == '8':
                d(resourceId=self.__pkg_name_contact + ':id/eight').click()
            elif c == '9':
                d(resourceId=self.__pkg_name_contact + ':id/nine').click()
            elif c == '0':
                d(resourceId=self.__pkg_name_contact + ':id/zero').click()
            elif c == '*':
                d(resourceId=self.__pkg_name_contact + ':id/star').click()
            elif c == '#':
                d(resourceId=self.__pkg_name_contact + ':id/pound').click()
            else:
                uit.raise_Exception_info('电话号码格式不正确')

    def get_phone_clear_part_ele(self):
        """
        获取拨号键盘中的删除按钮
        :return:
        """
        return d(resourceId=self.__pkg_name_contact + ':id/clear_part')

    def get_phone_digits_ele(self):
        """
        获取输入框中的号码
        :return:
        """
        return d(resourceId=self.__pkg_name_contact + ':id/digits')

    def get_phone_ivoka_call_ele(self):
        """
        获取拨号键盘上的语音按钮
        :return:
        """
        return d(resourceId=self.__pkg_name_contact + ':id/btn_ivoka_call')

    def get_phone_call_ele(self):
        """
        获取拨号键盘上的拨打按钮
        :return:
        """
        return d(resourceId=self.__pkg_name_contact + ':id/btn_call')

    def get_phone_bottom_back_ele(self):
        """
        获取电话底部的返回按钮
        :return:
        """
        return d(resourceId=self.__pkg_name_contact + ':id/as_bar_back_id')

    def get_phone_bottom_home_ele(self):
        """
        获取电话底部的返回主页按钮
        :return:
        """
        return d(resourceId=self.__pkg_name_contact + ':id/as_bar_home_id')

    def get_phone_contacts_search_ele(self):
        """
        获取通讯录搜索框
        :return:
        """
        return d(resourceId=self.__pkg_name_contact + ':id/search_edit')

    def get_phone_contacts_listView_ele(self):
        """
        获取通讯录列表
        :return:
        """
        return d(resourceId=self.__pkg_name_contact + ':id/listview')

    def get_phone_contact_by_name(self, name):
        """
        根据提供的通讯录名字获取联系人
        :param name:
        :return:
        """
        contact_list = self.get_phone_contacts_listView_ele()
        if contact_list.wait.exists():
            flag = contact_list.scroll.vert.to(text=name)
            if flag:
                return d(text=name)
            else:
                uit.raise_Exception_info('指定联系人在通讯录中不存在')
        else:
            uit.raise_Exception_info('通讯录列表不存在')

    def get_phone_contact_detail_call_ele(self):
        """
        获取联系人详情界面的拨打电话按钮
        :return:
        """
        return d(resourceId=self.__pkg_name_contact + ':id/call_btn')

    def get_phone_dialing_bottombar_dial_ele(self):
        """
        获取通话中底部的拨号按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/bottombar_dial_button')

    def get_phone_dialing_bottombar_contact_ele(self):
        """
        获取通话中底部的通讯录按钮
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/bottombar_contact_button')

    def get_phone_hungup_ele(self):
        """
        获取挂断电话按钮
        :return:
        """
        hungup_ele1 = d(resourceId=self.__pkg_name + ':id/call_hungup_button')
        hungup_ele2 = d(resourceId=self.__pkg_name + ':id/dial_hungup_button')
        return [hungup_ele1, hungup_ele2]

    def get_phone_calling_dial_gridview_ele(self):
        """
        获取通过中的拨号键视图控件
        :return:
        """
        return d(resourceId=self.__pkg_name + ':id/dial_gridview')

    def dial_phone_number_by_number_in_calling(self, number):
        """
        在通话过程中
        :param number:
        :return:
        """
        dial_view = self.get_phone_calling_dial_gridview_ele()
        if not dial_view.wait.exists():
            uit.raise_Exception_info('拨号视图不存在')
            return

        for c in number:
            if c == '1':
                d(className='android.widget.RelativeLayout', index=0).click()
            elif c == '2':
                d(className='android.widget.RelativeLayout', index=1).click()
            elif c == '3':
                d(className='android.widget.RelativeLayout', index=2).click()
            elif c == '4':
                d(className='android.widget.RelativeLayout', index=4).click()
            elif c == '5':
                d(className='android.widget.RelativeLayout', index=5).click()
            elif c == '6':
                d(className='android.widget.RelativeLayout', index=6).click()
            elif c == '7':
                d(className='android.widget.RelativeLayout', index=8).click()
            elif c == '8':
                d(className='android.widget.RelativeLayout', index=9).click()
            elif c == '9':
                d(className='android.widget.RelativeLayout', index=10).click()
            elif c == '0':
                d(className='android.widget.RelativeLayout', index=7).click()
            elif c == '*':
                d(className='android.widget.RelativeLayout', index=3).click()
            elif c == '#':
                d(className='android.widget.RelativeLayout', index=11).click()
            else:
                uit.raise_Exception_info('电话号码格式不正确')

    def get_phone_contact_detail_title_ele(self):
        """
        获取联系人详情页面的名字
        :return:
        """
        title_ele = d(resourceId=self.__pkg_name_contact + ':id/title', text='姓名')
        if title_ele.wait.exists():
            return title_ele.sibling(resourceId=self.__pkg_name_contact + ':id/content')
        else:
            uit.raise_Exception_info('联系人姓名内容不存在')

    def get_phone_contact_detail_number_ele(self):
        """
        获取联系人详情页面的名字
        :return:
        """
        title_ele = d(resourceId=self.__pkg_name_contact + ':id/title', text='手机号码')
        if title_ele.wait.exists():
            return title_ele.sibling(resourceId=self.__pkg_name_contact + ':id/content')
        else:
            uit.raise_Exception_info('联系人号码内容不存在')



btphone = BtPhone()