# -*- coding: utf-8 -*-
"""
Created on 1/6/17
@author: 欧光乾
@email: guangqianou@pateo.com.cn
"""

from behave import when, then
from utils.helpTools import d


@when(u'< 点击图片文件夹')
def step_impl(context):
    """
    点击图片文件夹
    :param context:
    :return:
    """
    # 获取文件夹名称
    folder_name = context.table[0]['folder_name']

    pass


@when(u'< 点击图片文件')
def step_impl(context):
    """
    点击图片文件
    :param context:
    :return:
    """
    # 获取图片文件名
    pic_name = context.table[0]['pic_name']
    pass


@when(u'< 点击下一张图片')
def step_impl(context):
    """
    点击下一张图片
    :param context:
    :return:
    """
    pass


@when(u'< 点击上一张图片')
def step_impl(context):
    """
    点击上一张图片
    :param context:
    :return:
    """
    pass


@when(u'< 点击图片删除按钮')
def step_impl(context):
    """
    点击图片删除按钮
    :param context:
    :return:
    """
    pass


@when(u'< 点击图片放大按钮')
def step_impl(context):
    """
    点击图片放大按钮
    :param context:
    :return:
    """
    pass
