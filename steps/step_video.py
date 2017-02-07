# -*- coding: utf-8 -*-
"""
Created on 1/6/17
@author: 欧光乾
@email: guangqianou@pateo.com.cn
"""
import time
from behave import when, then
from utils.helpTools import d, MAP_VAR
from utils.uiTools import uit
from elements.video import video


@when(u'< 播放视频文件')
def step_impl(context):
    """
    播放视频文件
    :param context:
    :return:
    """
    # 获取视频文件名字
    video_name = context.table[0]['video_name']
    ele = video.get_video_by_name(video_name)
    if ele.wait.exists():
        ele.click.wait()
        # 等待2s 是否有播放选项弹出
        time.sleep(2)
        replay_ele = d(text='重新开始')
        if replay_ele.exists:
            replay_ele.click()
    else:
        uit.raise_Exception_info('指定视频文件不存在')


@when(u'< 点击暂停播放中视频')
def step_impl(context):
    """
    点击暂停正在播放的视频
    :param context:
    :return:
    """
    pause_btn = video.get_video_play_btn()
    if pause_btn.wait.exists():
        pause_btn.click()
    else:
        uit.raise_Exception_info('暂停或播放按钮不存在')


@when(u'< 点击播放暂停中视频')
def step_impl(context):
    """
    暂停正在播放的视频
    :param context:
    :return:
    """
    context.execute_steps('''
    when < 点击暂停播放中视频
    ''')


@when(u'< 点击下一个视频')
def step_impl(context):
    """
    点击下一个视频
    :param context:
    :return:
    """
    next_btn = video.get_video_next_btn()
    if next_btn.wait.exists():
        next_btn.click()
    else:
        uit.raise_Exception_info('下一个视频按钮不存在')


@when(u'< 点击上一个视频')
def step_impl(context):
    """
    点击上一个视频
    :param context:
    :return:
    """
    prev_btn = video.get_video_prev_btn()
    if prev_btn.wait.exists():
        prev_btn.click()
    else:
        uit.raise_Exception_info('上一个视频按钮不存在')


@when(u'< 获取当前视频名称')
def step_impl(context):
    """
    获取当前视频名称
    :param context:
    :return:
    """
    # 获取出参
    cur_video = context.table[0]['o_result']
    video_name_ele = video.get_video_name_ele()
    if video_name_ele.wait.exists():
        MAP_VAR[cur_video] = video_name_ele.text.strip()
    else:
        uit.raise_Exception_info('视频名称控件不存在')


@then(u'< 验证视频播放状态')
def step_impl(context):
    """
    验证当前视频播放状态
    1. 等待5s界面稳定
    2. 判断是否在视频播放界面
    3. 判断是否存在播放控件--存在：暂停状态，不存在：播放状态

    :param context:
    :return:
    """
    # 获取入参
    status = context.table[0]['status']
    time.sleep(5)
    play_view_ele = video.get_video_play_view_ele()
    play_btn_ele = video.get_video_play_btn()
    if play_view_ele.wait.exists():
        if str(play_btn_ele.wait.exists()).lower() == status.lower():
            uit.raise_Exception_info('视频播放状态和期望值不一致')
    else:
        uit.raise_Exception_info('视频不在播放界面')


@then(u'< 验证视频退出播放')
def step_impl(context):
    """
    验证视频退出播放
    :param context:
    :return:
    """
    play_view_ele = video.get_video_play_view_ele()
    if play_view_ele.wait.exists():
        uit.raise_Exception_info('视频没有退出播放')


@when(u'< 点击视频底部返回按钮')
def step_impl(context):
    """
    点击视频底部返回按钮
    :param context:
    :return:
    """
    back_btn = video.get_video_bottom_back_btn()
    if back_btn.wait.exists():
        back_btn.click()
    else:
        uit.raise_Exception_info('视频底部返回按钮不存在')


@when(u'< 点击视频底部主页按钮')
def step_impl(context):
    """
    点击视频底部主页按钮
    :param context:
    :return:
    """
    home_btn = video.get_video_bottom_home_btn()
    if home_btn.wait.exists():
        home_btn.click()
    else:
        uit.raise_Exception_info('视频底部主页按钮不存在')


@when(u'< 点击视频列表按钮')
def step_impl(context):
    """
    点击视频列表按钮
    :param context:
    :return:
    """
    video_list_btn = video.get_video_list_btn()
    if video_list_btn.wait.exists():
        video_list_btn.click()
    else:
        uit.raise_Exception_info('视频列表按钮不存在')


@when(u'< 点击视频列表中视频')
def step_impl(context):
    """
    点击视频列表中指定的视频名称
    :param context:
    :return:
    """
    context.execute_steps('''
    when < 播放视频文件
    ''')
