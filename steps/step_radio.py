# -*- coding: UTF-8 -*-
'''
Created on 11/28/16
@author: zhiyuanwang
@email: zhiyuanwang@pateo.com.cn
'''

import time

from behave import when,then

from elements.radio import radio
from utils.uiTools import uit

@when(u'< 点击收音机播放与暂停切换区')
def step_impl(context):
    try:
        radio.execute_radio_FM_playorpause()

    except:
        uit.raise_Exception_info("点击收音机播放或暂停失败")

@when(u'< 点击收音机下一台')
def step_impl(context):
    try:
        radio.execute_radio_FM_next()
    except:
        uit.raise_Exception_info("点击收音机下一台失败")

@when(u'< 点击电台收藏')
def step_impl(context):
    ele = radio.get_radio_FM_add2favorite()
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info("收藏按钮控件未找到")

@when(u'< 点击FM与AM切换')
def step_impl(context):
    ele = radio.get_radio_type_icon()
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info("FM与AM切换按钮未找到")

@when(u'< 点击预览电台扫描')
def step_impl(context):
    ele = radio.get_radio_scan_icon()
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info("电台预览SCAN按钮未找到")


@when(u'< 点击自动电台扫描')
def step_impl(context):
    ele = radio.get_radio_AST_icon()
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info("电台自动扫描AST按钮未找到")


@when(u'< 点击电台列表')
def step_impl(context):
    ele = radio.get_radio_FM_list()
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info("电台列表按钮未找到")


@when(u'< 点击电台收藏列表')
def step_impl(context):
    ele = radio.get_radio_FM_favorite()
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info("电台收藏列表按钮未找到")

@when(u'< 滑动收音机节目单到最前')
def step_impl(context):
    ele = radio.get_radio_lists_object()
    if ele.wait.exists():
        ele.fling.vert.backward()
    else:
        uit.raise_Exception_info("电台列表实体获取或者滚动失败")


@when(u'< 滑动收音机节目单到最尾部')
def step_impl(context):
    ele = radio.get_radio_lists_object()
    if ele.wait.exists():
        ele.fling.vert.forward()
    else:
        uit.raise_Exception_info("电台列表实体获取或者滚动失败")

@when(u'< 滑动收音机节目列表到指定台')
def step_impl(context):
    value = context.table[0]['radio_station']
    ele = radio.get_radio_lists_frequency(value)
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info("电台列表实体获取或者滚动失败")


@when(u'< 获取当前播放电台名称')
def step_impl(context):
    name= radio.get_radio_station_name()



@then(u'< 验证收音机节目列表不为空')
def step_impl(context):
    text = radio.get_radio_list_first_name()
    if text != '':
        pass
    else:
        uit.raise_Exception_info("电台列表为空")


@then(u'< 验证收音机收藏节目列表不为空')
def step_impl(context):
    text = radio.get_radio_list_first_name()
    if text != '':
        pass
    else:
        uit.raise_Exception_info("收藏电台列表为空")


@then(u'< 验证正在预览电台')
def step_impl(context):
    if radio.get_radio_preview_text().wait.exists():
        pass
    else:
        uit.raise_Exception_info("预览电台出现异常")


@then(u'< 验证正在重新搜台')
def step_impl(context):
    if radio.get_radio_AST_text().wait.exists():
        pass
    else:
        uit.raise_Exception_info("正在重新搜台出现异常")


@then(u'< 验证搜台结果为网络不可用')
def step_impl(context):
    total =20
    while not radio.get_radio_AST_text().wait.exists():
        time.sleep(1)
        total=total-1
        if total < 0:
            uit.raise_Exception_info("正在重新搜台出现异常")
            break


