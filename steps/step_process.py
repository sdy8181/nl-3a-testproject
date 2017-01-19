# -*- coding: utf-8 -*-
"""
Created on 1/9/17
@author: 欧光乾
@email: guangqianou@pateo.com.cn
"""

from behave import when, then
from utils.helpTools import d
from utils.uiTools import uit
from elements.process import process


@when(u'< 点击全部关闭')
def step_impl(context):
    """
    点击全部关闭按钮
    :param context:
    :return:
    """
    close_all = d(text='全部关闭')
    if close_all.wait.exists():
        close_all.click()
    else:
        uit.raise_Exception_info('全部关闭按钮不存在')


@when(u'< 点击关闭指定进程')
def step_impl(context):
    """
    点击关闭指定进程
    :param context:
    :return:
    """
    process_name = context.table[0]['process_name']
    kill_it = process.get_kill_process_btn_by_name(process_name)
    if kill_it.wait.exists():
        kill_it.click()
    else:
        uit.raise_Exception_info('杀掉指定进程控件不存在')


@then(u'< 验证指定进程是否关闭')
def step_impl(context):
    """
    验证指定进程是否关闭
    :param context:
    :return:
    """
    # 获取进程名字和关闭状态
    process_name = context.table[0]['process_name']
    status = context.table[0]['status']

    process_view = process.get_processes_view()

    if str(process_view.scroll.vert.to(text=process_name)).lower() == \
            status.lower():
        uit.raise_Exception_info('指定进程是否关闭验证失败')


@then(u'< 验证全部进程是否关闭')
def step_impl(context):
    """
    验证指定进程是否关闭
    :param context:
    :return:
    """
    status = context.table[0]['status']
    process_ele_list = process.get_process_eles()
    if str(len(process_ele_list) == 0).lower() != status.lower():
        uit.raise_Exception_info('进程是否全部关闭验证失败')
