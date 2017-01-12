# -*- coding: UTF-8 -*-
'''
Created on 11/28/16
@author: zhiyuanwang
@email: zhiyuanwang@pateo.com.cn
'''

import time

from behave import when,then
from utils.helpTools import MAP_VAR
from elements.radio import radio
from utils.uiTools import uit

@when(u'< 点击收音机播放与暂停切换区')
def step_impl(context):

    ele = radio.get_radio_frequency_id()
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info("点击收音机播放或暂停失败")

@when(u'< 点击收音机下一台')
def step_impl(context):
    try:
        radio.execute_radio_FM_next()
        time.sleep(0.5)
    except:
        uit.raise_Exception_info("点击收音机下一台失败")

@when(u'< 点击收音机上一台')
def step_impl(context):
    try:
        radio.execute_radio_FM_prev()
        time.sleep(0.5)
    except:
        uit.raise_Exception_info("点击收音机上一台失败")


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
        time.sleep(0.5)
    else:
        uit.raise_Exception_info("电台自动扫描AST按钮未找到")


@when(u'< 点击电台列表')
def step_impl(context):
    ele = radio.get_radio_FM_listicon()
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


@when(u'< 点击底部控制栏返回按钮')
def step_impl(context):
    ele = radio.get_radio_back_icon()
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info("未找到底部控制栏Back按钮")


@when(u'< 点击底部控制栏Home按钮')
def step_impl(context):
    ele = radio.get_radio_to_home()
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info("未找到底部控制栏Home按钮")



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
    ele = radio.get_radio_lists_frequency(value.strip())
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info("电台列表实体获取或者滚动失败")


@when(u'< 获取当前播放电台名称')
def step_impl(context):
    #接受一个外部指定的名字作为存储获取当前电台名称KEY
    o_station_name = context.table[0]['o_station_name']

    station_text= radio.get_radio_station_name()
    MAP_VAR[o_station_name]= station_text



@then(u'< 验证收音机当前状态为暂停')
def step_impl(context):
    ele1,ele2 = radio.get_radio_pause_control_status()
    if ele1 == ele2:
        pass
    else:
        uit.raise_Exception_info("当前电台不是暂停，请检查")


@then(u'< 验证收音机当前状态为播放')
def step_impl(context):
    ele1, ele2 = radio.get_radio_pause_control_status()
    if ele1 != ele2:
        pass
    else:
        uit.raise_Exception_info("当前电台不是播放，请检查")



@then(u'< 验证两次获取的电台名称是一致的')
def step_impl(context):
    #接收输入的key参数，从而获取以前保存的value
    name_key1 =context.table[0]['param1']
    name_key2 =context.table[0]['param2']

    if name_key1.startswith('o_') :
        name_key1=MAP_VAR[name_key1]

    if name_key2.startswith('o_'):
        name_key2 = MAP_VAR[name_key2]

    if name_key1 and name_key2:
        if name_key1==name_key2:
            return True
        else:
            uit.raise_Exception_info("两次获取的电台名对比出错")



@then(u'< 验证两次获取的电台名称不一致的')
def step_impl(context):
    #接收输入的key参数，从而获取以前保存的value
    name_key1 =context.table[0]['param1']
    name_key2 =context.table[0]['param2']

    if name_key1.startswith('o_') :
        name_key1=MAP_VAR[name_key1]

    if name_key2.startswith('o_'):
        name_key2 = MAP_VAR[name_key2]

    if name_key1 and name_key2:
        if name_key1!=name_key2:
            return True
        else:
            uit.raise_Exception_info("两次获取的电台名对比出错")




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


@then(u'< 验证扫描后结果为空')
def step_impl(context):
    total =60
    while radio.get_radio_AST_text().wait.exists():
        time.sleep(1)
        total=total-1
        if total < 0:
            uit.raise_Exception_info("搜台无外结束，有异常")
            break
    if radio.get_radio_scanresult_null().wait.exists():
        pass
    else:
        uit.raise_Exception_info("扫描结果不为空或未进行扫描")



@when(u'< 向右滑动收音机界面')
def step_impl(context):

    ele = radio.get_radio_frequency_id()
    if ele.wait.exists():
        ele.swipe.right()
    else:
        uit.raise_Exception_info("收音机向右滑动异常")



@when(u'< 向左滑动收音机界面')
def step_impl(context):

    ele = radio.get_radio_frequency_id()
    if ele.wait.exists():
        ele.swipe.left()
    else:
        uit.raise_Exception_info("收音机向左滑动异常")


@when(u'< 获取当前收音机节目收藏状态')
def step_impl(context):
    # 接受一个外部指定的名字作为存储获取当前电台名称KEY
    o_state = context.table[0]['o_radio_collect_state']
    tmp = radio.get_radio_collect_status()
    MAP_VAR[o_state] = tmp


@then(u'< 验证点击收藏按钮后状态响应正确')
def step_impl(context):
    key1 = context.table[0]['param1']
    key2 = context.table[0]['param2']

    if key1.startswith('o_'):
        key1 = MAP_VAR[key1]
    if key2.startswith('o_'):
        key2 = MAP_VAR[key2]

    if key1 != key2:
        pass
    else:
        uit.raise_Exception_info("收音机收藏状态发生异常")



