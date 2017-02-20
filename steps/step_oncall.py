# -*- coding: UTF-8 -*-
'''
Created on 2/17/2017
@author: zhiyuanwang
@email: zhiyuanwang@pateo.com.cn
'''

import time

from behave import when,then
from utils.helpTools import MAP_VAR
from elements.oncall import oncall
from utils.uiTools import uit



@when(u'< 点击挂断Oncall')
def step_impl(context):
    ele = oncall.get_oncall_endcalling()
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info('未找到挂断oncall控件，请检查')

@when(u'< 点击行车助手底部返回')
def step_impl(context):
    ele = oncall.get_oncall_back()
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info('未找到挂断oncall控件，请检查')


@then(u'< 验证正在OnCall通话中')
def step_impl(context):
    ele = oncall.get_oncall_status()
    if ele.wait.exists():
        pass
    else:
        uit.raise_Exception_info('当前Oncall状态不对，请检查')
