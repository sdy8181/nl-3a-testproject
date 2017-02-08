# -*- coding: utf-8 -*-
"""
Created on 2/8/17
@author: 欧光乾
@email: guangqianou@pateo.com.cn
"""
from behave import when, then
from utils.uiTools import uit
from utils.helpTools import d, MAP_VAR, d_width, d_height, ht
from elements.btphone import btphone


@when(u'< 点击通讯录')
def step_impl(context):
    """
    点击通讯录
    :param context:
    :return:
    """
    contacts_ele = btphone.get_phone_contacts_tab_ele()
    if contacts_ele.wait.exists():
        pos_x, pos_y = uit.get_clickcoord_by_ele(contacts_ele)
        d.click(pos_x, pos_y)
    else:
        uit.raise_Exception_info('通讯录控件不存在')


@when(u'< 点击最近通话')
def step_impl(context):
    """
    点击最近通话
    :param context:
    :return:
    """
    calllog_ele = btphone.get_phone_calllog_tab_ele()
    if calllog_ele.wait.exists():
        pos_x, pos_y = uit.get_clickcoord_by_ele(calllog_ele)
        d.click(pos_x, pos_y)
    else:
        uit.raise_Exception_info('最近通话控件不存在')


@when(u'< 点击拨号键盘')
def step_impl(context):
    """
    点击拨号键盘
    :param context:
    :return:
    """
    dial_ele = btphone.get_phone_dial_tab_ele()
    if dial_ele.wait.exists():
        pos_x, pos_y = uit.get_clickcoord_by_ele(dial_ele)
        d.click(pos_x, pos_y)
    else:
        uit.raise_Exception_info('拨号键盘控件不存在')


@when(u'< 输入要拨打的号码')
def step_impl(context):
    """
    根据提供的号码输入号码
    :param context:
    :return:
    """
    # 获取号码字符串
    phone_number = context.table[0]['phone_number']
    btphone.dial_phone_number(phone_number)


@when(u'< 获取输入框中的号码')
def step_impl(context):
    """
    获取输入框中的号码
    :param context:
    :return:
    """
    o_result = context.table[0]['o_result']
    digit_ele = btphone.get_phone_digits_ele()
    if digit_ele.wait.exists():
        MAP_VAR[o_result] = digit_ele.text.strip()
    else:
        uit.raise_Exception_info('输入框不存在')


@when(u'< 点击电话号码删除按钮')
def step_impl(context):
    """
    点击电话号码删除按钮
    :param context:
    :return:
    """
    del_ele = btphone.get_phone_clear_part_ele()
    if del_ele.wait.exists():
        del_ele.click()
    else:
        uit.raise_Exception_info('键盘上删除按钮不存在')


@when(u'< 点击电话语音按钮')
def step_impl(context):
    """
    点击电话语音按钮
    :param context:
    :return:
    """
    ivoka_ele = btphone.get_phone_ivoka_call_ele()
    if ivoka_ele.wait.exists():
        ivoka_ele.click()
    else:
        uit.raise_Exception_info('拨号语音按钮不存在')


@when(u'< 点击电话拨打按钮')
def step_impl(context):
    """
    点击电话拨打按钮
    :param context:
    :return:
    """
    call_ele = btphone.get_phone_call_ele()
    if call_ele.wait.exists():
        call_ele.click()
    else:
        uit.raise_Exception_info('电话拨打按钮不存在')


@when(u'< 点击电话底部返回按钮')
def step_impl(context):
    """
    点击电话底部返回按钮
    :param context:
    :return:
    """
    back_ele = btphone.get_phone_bottom_back_ele()
    if back_ele.wait.exists():
        back_ele.click()
    else:
        uit.raise_Exception_info('底部返回按钮不存在')


@when(u'< 点击电话底部返回主页按钮')
def step_impl(context):
    """
    点击电话底部返回主页按钮
    :param context:
    :return:
    """
    home_ele = btphone.get_phone_bottom_home_ele()
    if home_ele.wait.exists():
        home_ele.click()
    else:
        uit.raise_Exception_info('底部返回按钮不存在')


@when(u'< 滑动展示通讯录搜索框')
def step_impl(context):
    """
    滑动展示通讯录搜索框
    :param context:
    :return:
    """
    d.swipe(d_width / 2, d_height / 2, d_width / 2, d_height / 6 * 5, 20)


@when(u'< 输入通讯录搜索内容')
def step_impl(context):
    """
    输入通讯录搜索内容
    :param context:
    :return:
    """
    # 获取搜索字符串
    search_txt = context.table[0]['search_txt']

    search_ele = btphone.get_phone_contacts_search_ele()
    if search_ele.wait.exists():
        search_ele.set_text(ht.unicode_input(search_txt))
    else:
        uit.raise_Exception_info('通讯录搜索框不存在')


@when(u'< 点击通讯录中指定联系人')
def step_impl(context):
    """
    点击通讯录中指定联系人
    :param context:
    :return:
    """
    # 获取联系人名称
    name = context.table[0]['contact']
    contact_ele = btphone.get_phone_contact_by_name(name)
    if contact_ele.wait.exists():
        pos_x, pos_y = uit.get_clickcoord_by_ele(contact_ele)
        d.click(pos_x, pos_y)
    else:
        uit.raise_Exception_info('指定联系人在通讯录中不存在')


@when(u'< 点击查看指定联系人详情')
def step_impl(context):
    """
    点击查看指定联系人详情
    :param context:
    :return:
    """
    # 获取联系人名称
    name = context.table[0]['contact']
    contact_ele = btphone.get_phone_contact_by_name(name)
    if contact_ele.wait.exists():
        detail_ele = contact_ele.sibling(resourceId='com.pateo.as.contacts:id/contact_detail')
        if detail_ele.wait.exists():
            detail_ele.click()
        else:
            uit.raise_Exception_info('指定联系人详情按钮不存在')
    else:
        uit.raise_Exception_info('指定联系人在通讯录中不存在')


@when(u'< 点击联系人详情中的拨打按钮')
def step_impl(context):
    """
    点击详情界面中的拨打电话按钮
    :param context:
    :return:
    """
    call_ele = btphone.get_phone_contact_detail_call_ele()
    if call_ele.wait.exists():
        call_ele.click()
    else:
        uit.raise_Exception_info('拨打电话按钮不存在')


@when(u'< 点击通话界面中的拨号按钮')
def step_impl(context):
    """
    点击通话界面中的拨号按钮
    :param context:
    :return:
    """
    dial_ele = btphone.get_phone_dialing_bottombar_dial_ele()
    if dial_ele.wait.exists():
        dial_ele.click()
    else:
        uit.raise_Exception_info('拨号按钮不存在')


@when(u'< 点击通话界面中的通讯录按钮')
def step_impl(context):
    """
    点击通话界面中的通讯录按钮
    :param context:
    :return:
    """
    contact_ele = btphone.get_phone_dialing_bottombar_contact_ele()
    if contact_ele.wait.exists():
        contact_ele.click()
    else:
        uit.raise_Exception_info('通讯录按钮不存在')


@when(u'< 点击挂断电话按钮')
def step_impl(context):
    """
    点击挂断电话按钮
    :param context:
    :return:
    """
    hungup_eles = btphone.get_phone_hungup_ele()
    for he in hungup_eles:
        if he.wait.exists():
            he.click()
            break
    else:
        uit.raise_Exception_info('挂断电话按钮不存在')


@when(u'< 在通话中输入号码')
def step_impl(context):
    """
    在通话过程中输入号码
    :param context:
    :return:
    """
    # 获取要输入的号码
    number = context.table[0]['number']
    btphone.dial_phone_number_by_number_in_calling(number)


@then(u'< 验证通话状态')
def step_impl(context):
    """
    验证蓝牙电话通话状态
    :param context:
    :return:
    """
    status = context.table[0]['status']

    hungup_eles = btphone.get_phone_hungup_ele()
    flag = False
    for he in hungup_eles:
        if he.wait.exists():
            flag = True
            break

    if str(flag).lower() != status.lower():
        uit.raise_Exception_info('通话状态不一致')


@then(u'< 验证联系人详情信息')
def step_impl(context):
    """
    验证联系人详情信息
    :param context:
    :return:
    """
    # 获取联系人的名字和电话号码
    name = context.table[0]['name']
    phone_number = context.table[0]['phone_number']

    name_ele = btphone.get_phone_contact_detail_title_ele()
    if name_ele.wait.exists():
        if name_ele.text.strip() != name:
            uit.raise_Exception_info('联系人姓名不一致')
    else:
        uit.raise_Exception_info('联系人名字控件不存在')

    phone_ele = btphone.get_phone_contact_detail_number_ele()
    if phone_ele.wait.exists():
        if phone_ele.text.strip() != phone_number:
            uit.raise_Exception_info('联系人号码不一致')
    else:
        uit.raise_Exception_info('联系人号码控件不存在')


