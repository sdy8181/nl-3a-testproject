# -*- coding: UTF-8 -*-
import os
import time

from behave import when, then

from elements.common import Common
from utils.helpTools import ht, MAP_VAR
from utils.uiTools import uit
from utils.helpTools import d, d_height, d_width


@when(u'< 延时')
def step_impl(context):
    # 获取延时时间
    sec = '1'
    tmp = context.table[0]['sleep_time']
    if tmp:
        sec = tmp
        time.sleep(int(sec))


@then(u'< 验证音频通道')
def step_impl(context):
    chk_tinymix = context.table[0]['chk_tinymix']
    # 获取当前的放音通道
    cur_tinymix = ht.get_cur_tinymix()
    if chk_tinymix != cur_tinymix:
        uit.raise_Exception_info('音频通道不一致，期望值为《' + chk_tinymix + '》，实际值为《' + cur_tinymix + '》')


@when(u'< 播放音频文件')
def step_impl(context):
    # 获取参数
    voiceFile = context.table[0]['voice_file']
    ht.play_voice(voiceFile)


@then(u'< 验证当前应用')
def step_impl(context):
    # 获取期望应用名称
    chk_app_name = context.table[0]['app_name']
    # 获取当前应用名称
    cur_app_name = Common().get_current_package_name()
    # 校验
    if chk_app_name != cur_app_name:
        uit.raise_Exception_info('期望应用和当前应用不一致，期望应用为《' + chk_app_name + '》，当前应用为《' + cur_app_name + '》')


@when(u'< 拔出U盘')
def step_impl(context):
    Common().controlPoweroff()


@when(u'< 插上U盘')
def step_impl(context):
    Common().controlPoweron()


@then(u'< 验证对象值')
def step_impl(context):
    # 获取两个对象和一个比较字符
    param1 = context.table[0]['param1']
    param2 = context.table[0]['param2']
    opt = context.table[0]['option']

    if param1.startswith('o_'):
        param1 = MAP_VAR.get(param1)

    if param2.startswith('o_'):
        param2 = MAP_VAR.get(param2)

    if opt == '==':
        flag = param1.lower() == param2.lower()
    elif opt == '!=':
        flag = param1.lower() != param2.lower()
    elif opt == '%':
        flag = param1.lower().__contains__(param2.lower())
    elif opt == ">":
        flag = int(param1.lower()) > int(param2.lower())
    elif opt == "<":
        flag = int(param1.lower()) < int(param2.lower())
    else:
        raise Exception('暂时不支持改操作符，请联系脚本维护人员')

    if not flag:
        uit.raise_Exception_info('比较失败《' + param1 + ' ' + opt + ' ' + param2 + '》')


@then(u'< 验证文本是否存在')
def step_impl(context):
    # 获取入参
    txt = context.table[0]['text']
    exists_flag = context.table[0]['exists_flag']

    ele = d(textContains=txt)

    if not str(ele.wait.exists()).lower() == exists_flag.lower():
        uit.raise_Exception_info('验证文本是否存在失败')


@when(u'< 重启设备')
def step_impl(context):
    device_serial = ht.get_conf_value('deviceSerial')
    os.popen('adb -s ' + device_serial + ' shell reboot')


@when(u'< 下拉进程菜单')
def step_impl(context):
    d.swipe(d_width / 2, 0, d_width / 2, d_height, 20)


@when(u'< 收起进程菜单')
def step_impl(context):
    d.swipe(d_width / 2, d_height, d_width / 2, 0, 20)


@when(u'< 按硬按键')
def step_impl(context):
    # 获取硬按键关键词
    key_word = context.table[0]['key']

    if key_word.lower() == 'home':
        d.press.home()
    elif key_word.lower() == 'back':
        d.press.back()
    elif key_word.lower() == 'v-':
        d.press.volume_down()
    elif key_word.lower() == 'v+':
        d.press.volume_up()
    else:
        uit.raise_Exception_info('无法识别的Key')


@when(u'< 向左滑动屏幕')
def step_impl(context):
    d.swipe(d_width / 6 * 5, d_height / 2, d_width / 6, d_height / 2, 20)


@when(u'< 向右滑动屏幕')
def step_impl(context):
    d.swipe(d_width / 6, d_height / 2, d_width / 6 * 5, d_height / 2, 20)


@when(u'< 点击屏幕中央')
def step_impl(context):
    """
    点击屏幕中央位置，如播放视频界面，图片全屏界面
    :param context:
    :return:
    """
    d.click(d_width / 2, d_height / 2)
