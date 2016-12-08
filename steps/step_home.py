# -*- coding: utf-8 -*-
'''
Created on 11/28/16
@author: 欧光乾
@email: guangqianou@pateo.com.cn
'''
import time
from datetime import datetime
from behave import when, then
from elements.home import home
from utils.helpTools import d_width, d_height, d, MAP_VAR, ht
from utils.uiTools import uit


@when(u'< 点击主页应用')
def step_impl(context):
    # 获取应用名称
    app_name = context.table[0]['app_name']
    print(app_name)

    if app_name == '导航':
        x_coordinate, y_coordinate = uit.get_clickcoord_from_bounds(textContains=app_name)
        d.click(x_coordinate, y_coordinate)
    else:
        x_coordinate, y_coordinate = uit.get_clickcoord_from_bounds(text=app_name)
        d.click(x_coordinate, y_coordinate)


@when(u'< 点击主页音乐播放暂停')
def step_impl(context):
    ele = home.get_music_play_pause_btn()

    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info('主页音乐播放暂停按钮不存在')


@when(u'< 点击主页音乐下一首')
def step_impl(context):
    ele = home.get_music_next_btn()

    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info('主页音乐播放下一首按钮不存在')


@when(u'< 点击主页音乐上一首')
def step_impl(context):
    ele = home.get_music_prev_btn()

    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info('主页音乐播放上一首按钮不存在')


@when(u'< 获取主页音乐名称')
def step_impl(context):
    # 获取接收参数
    music_name = context.table[0]['o_result']
    ele = home.get_music_info_ele()

    if ele.wait.exists():
        album_info = ele.text.strip()
        MAP_VAR[music_name] = album_info.split()[0]
    else:
        uit.raise_Exception_info('主页音乐名称信息获取失败')


@when(u'< 获取主页音乐歌手')
def step_impl(context):
    # 获取接收参数
    artist = context.table[0]['o_result']
    ele = home.get_music_info_ele()

    if ele.wait.exists():
        album_info = ele.text.strip()
        info_list = album_info.split()
        if len(info_list) > 1:
            MAP_VAR[artist] = info_list[1]
        else:
            uit.raise_Exception_info('主页音乐歌手信息获取失败')
    else:
        uit.raise_Exception_info('主页音乐名称信息获取失败')


@then(u'< 验证主页日期天气格式')
def step_impl(context):
    # 获取日期控件
    date_ele = home.get_home_date_ele()
    # 获取当前日期
    now_date = datetime.now().strftime('%m月%d日')

    if date_ele.wait.exists():
        if now_date != date_ele.text.strip():
            uit.raise_Exception_info('日期比对失败')
    else:
        uit.raise_Exception_info('日期元素未找到')

    # 获取星期控件
    week_ele = home.get_home_week_ele()
    if not week_ele.exists:
        uit.raise_Exception_info('星期元素未找到')
    # 获取当前周的第几天
    weekday = datetime.now().strftime('%w')
    except_weekday = '星期'
    if weekday == '0':
        except_weekday += '日'
    elif weekday == '1':
        except_weekday += '一'
    elif weekday == '2':
        except_weekday += '二'
    elif weekday == '3':
        except_weekday += '三'
    elif weekday == '4':
        except_weekday += '四'
    elif weekday == '5':
        except_weekday += '五'
    else:
        except_weekday += '六'

    if week_ele.text.strip() != except_weekday:
        uit.raise_Exception_info('星期比对失败')


@then(u'< 验证主页音乐播放状态')
def step_impl(context):
    # 获取期望播放状态信息
    play_status = context.table[0]['status']
    ele = home.get_home_multimediaLayout_ele()

    if ele.wait.exists():
        time.sleep(5)
        bounds = ele.info['bounds']
        png1 = uit.cutting_device_screenshot('a.png', bounds)
        time.sleep(5)
        png2 = uit.cutting_device_screenshot('b.png', bounds)

        ret = ht.get_image_diff_data(png1, png2)
        print(ret)
        print(ret == 0.0)

        if str((ret == 0.0)).lower() == play_status.lower():
            uit.raise_Exception_info('主页音乐播放状态不一致')
    else:
        uit.raise_Exception_info('主页音乐播放布局不存在')


@when(u'< 滑动主页到指定屏')
def step_impl(context):
    screen_num = int(context.table[0]['number'])
    # 判断是否在第一屏
    while not d(textContains='导航').exists:
        d.swipe(0, d_height / 2, d_width, d_height / 2, 20)

    for i in range(screen_num - 1):
        d.swipe(d_width, d_height / 2, 0, d_height / 2, 20)

    time.sleep(2)
