# -*- coding: utf-8 -*-
"""
Created on 1/6/17
@author: 欧光乾
@email: guangqianou@pateo.com.cn
"""
from behave import when, then
from utils.helpTools import d, TIME_OUT
from utils.uiTools import uit


@when(u'< 播放视频文件')
def step_impl(context):
    """
    播放视频文件
    :param context:
    :return:
    """
    # 获取视频文件名字
    video_name = context.table[0]['video_name']
    ele = d(text=video_name)
    if ele.wait.exists(timeout=TIME_OUT):
        ele.click.wait()
    else:
        uit.raise_Exception_info('指定视频文件不存在')


@when(u'< 暂停播放中视频')
def step_impl(context):
    """
    暂停正在播放的视频
    :param context:
    :return:
    """
    pass


@when(u'< 播放暂停中视频')
def step_impl(context):
    """
    暂停正在播放的视频
    :param context:
    :return:
    """
    pass


@when(u'< 点击下一个视频')
def step_impl(context):
    """
    点击下一个视频
    :param context:
    :return:
    """
    pass


@when(u'< 点击上一个视频')
def step_impl(context):
    """
    点击上一个视频
    :param context:
    :return:
    """
    pass


@when(u'< 获取当前视频名称')
def step_impl(context):
    """
    获取当前视频名称
    :param context:
    :return:
    """
    # 获取出参
    cur_video = context.table[0]['o_result']
    print(cur_video)
    pass


@then(u'< 验证视频播放状态')
def step_impl(context):
    """
    验证当前视频播放状态
    :param context:
    :return:
    """
    # 获取入参
    status = context.table[0]['status']
    print(status)
    pass


@when(u'< 点击视频底部返回按钮')
def step_impl(context):
    """
    点击视频底部返回按钮
    :param context:
    :return:
    """
    pass


@when(u'< 点击视频底部主页按钮')
def step_impl(context):
    """
    点击视频底部主页按钮
    :param context:
    :return:
    """
    pass


@when(u'< 退出视频播放')
def step_impl(context):
    """
    退出视频播放
    :param context:
    :return:
    """
    pass


@then(u'< 验证视频退出播放')
def step_impl(context):
    """
    验证视频退出播放
    :param context:
    :return:
    """
    pass


@when(u'< 点击视频底部返回按钮')
def step_impl(context):
    """
    点击视频底部返回按钮
    :param context:
    :return:
    """
    pass


@when(u'< 点击视频底部主页按钮')
def step_impl(context):
    """
    点击视频底部主页按钮
    :param context:
    :return:
    """
    pass

