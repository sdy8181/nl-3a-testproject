# -*- coding: UTF-8 -*-
'''
Created on 11/1/16
@author: 欧光乾
@email: guangqianou@pateo.com.cn
'''

from behave import when
from utils.uiTools import uit
from elements.audio import audio


@when(u'< 打开音乐搜索')
def step_impl(context):
    ele = audio.get_audio_search_ele()
    if ele.wait.exists():
        ele.click.wait()
    else:
        uit.raise_Exception_info('音乐搜索控件不存在')
