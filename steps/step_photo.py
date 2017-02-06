# -*- coding: utf-8 -*-
"""
Created on 2/3/17
@author: 欧光乾
@email: guangqianou@pateo.com.cn
"""
import time
import re
from behave import when
from behave import then

from utils.helpTools import d, MAP_VAR
from elements.photo import photo
from utils.uiTools import uit


@when(u'< 点击图片文件夹')
def step_impl(context):
    """
    点击图片文件夹 文件夹名称不包含图片数量
    :param context:
    :return:
    """
    # 获取文件夹名称
    folder_name = context.table[0]['folder_name']
    folder_ele = photo.get_photo_folder_by_name(folder_name)

    if folder_ele.wait.exists():
        pos_x, pos_y = uit.get_clickcoord_by_ele(folder_ele)
        d.click(pos_x, pos_y)
    else:
        uit.raise_Exception_info('指定文件夹不存在')


@when(u'< 点击图片文件')
def step_impl(context):
    """
    点击图片文件， 图片文件带有后缀
    :param context:
    :return:
    """
    # 获取图片文件名参数
    photo_name = context.table[0]['photo_name']
    photo_ele = photo.get_photo_by_name(photo_name)

    if photo_ele.wait.exists():
        pos_x, pos_y = uit.get_clickcoord_by_ele(photo_ele)
        d.click(pos_x, pos_y)
    else:
        uit.raise_Exception_info('指定图片文件不存在')


@when(u'< 点击下一张图片')
def step_impl(context):
    """
    点击下一张图片
    :param context:
    :return:
    """
    next_ele = photo.get_photo_preview_next()
    if next_ele.wait.exists():
        next_ele.click()
    else:
        uit.raise_Exception_info('下一张图片按钮不存在')


@when(u'< 点击上一张图片')
def step_impl(context):
    """
    点击上一张图片
    :param context:
    :return:
    """
    prev_ele = photo.get_photo_preview_prev()
    if prev_ele.wait.exists():
        prev_ele.click()
    else:
        uit.raise_Exception_info('上一张图片按钮不存在')


@when(u'< 点击图片删除按钮')
def step_impl(context):
    """
    点击图片删除按钮
    :param context:
    :return:
    """
    # 获取是否删除选项
    choice = context.table[0]['choice'].strip()
    del_ele = photo.get_photo_preview_del()
    if del_ele.wait.exists():
        del_ele.click()
        # 等待2S
        time.sleep(2)
        choice_ele = d(text=choice)
        if choice_ele.wait.exists():
            choice_ele.click()
        else:
            uit.raise_Exception_info('是否删除选项没有找到')


@when(u'< 点击图片全屏按钮')
def step_impl(context):
    """
    点击底部的图片全屏按钮
    :param context:
    :return:
    """
    full_ele = photo.get_photo_preview_fullscreen()
    if full_ele.wait.exists():
        full_ele.click()
    else:
        uit.raise_Exception_info('图片全屏按钮不存在')


@when(u'< 获取当前图片名称')
def step_impl(context):
    """
    获取当前内文件并返回
    :param context:
    :return:
    """
    photo_name = context.table[0]['o_result']
    # 获取图片名称控件
    photo_name_ele = photo.get_photo_preview_name()

    if photo_name_ele.wait.exists():
        MAP_VAR[photo_name] = photo_name_ele.text.strip()
    else:
        uit.raise_Exception_info('图片名称控件不存在')


@then(u'< 验证图片文件夹数量一致')
def step_impl(context):
    """
    验证图片文件夹数量一致
    :param context:
    :return:
    """
    # 获取文件夹名称和期望数量
    folder_name = context.table[0]['folder_name']
    photo_number = context.table[0]['number']

    # 获取指定文件夹控件
    folder_ele = photo.get_photo_folder_by_name(folder_name)
    if folder_ele.wait.exists():
        # 获取数量
        number = re.findall(r"\((\d+)\)$", folder_ele.text.strip())[0]
        if not photo_number == number:
            uit.raise_Exception_info('图片数量比对不一致，期望值为%s, 实际值为%s' % (photo_number, number))
    else:
        uit.raise_Exception_info('指定图片文件夹不存在')


@when(u'< 点击图片退出全屏按钮')
def step_impl(context):
    """
    点击图片退出全屏按钮，回到预览界面
    :param context:
    :return:
    """
    exit_full_ele = photo.get_photo_preview_exit_fullscreen()
    if exit_full_ele.wait.exists():
        exit_full_ele.click()
    else:
        uit.raise_Exception_info('图片退出全屏按钮不存在')


@then(u'< 验证图片全屏')
def step_impl(context):
    """
    验证图片全屏
    等待5s
    1. 图片视图控件存在
    2. 图片全屏控件不存在
    :param context:
    :return:
    """
    # 等待5s 目的为了控件在全屏界面隐藏
    time.sleep(5)
    # 获取图片视图控件
    photo_image_ele = photo.get_photo_preview_image_ele()
    # 获取全屏控件
    photo_full_ele = photo.get_photo_preview_fullscreen()

    if photo_image_ele.wait.exists():
        if photo_full_ele.wait.exists():
            uit.raise_Exception_info('图片不是全屏状态')
    else:
        uit.raise_Exception_info('图片不在图片视图界面')


@then(u'< 验证图片退出全屏')
def step_impl(context):
    """
    验证图片退出全屏
    等待5s
    1. 图片视图控件存在
    2. 图片全屏控件存在
    :param context:
    :return:
    """
    # 等待5s 目的为了控件在全屏界面隐藏
    time.sleep(5)
    # 获取图片视图控件
    photo_image_ele = photo.get_photo_preview_image_ele()
    # 获取全屏控件
    photo_full_ele = photo.get_photo_preview_fullscreen()

    if photo_image_ele.wait.exists():
        if not photo_full_ele.wait.exists():
            uit.raise_Exception_info('图片是全屏状态')
    else:
        uit.raise_Exception_info('图片不在图片视图界面')
