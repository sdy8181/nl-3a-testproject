# -*- coding: UTF-8 -*-
'''
Created on 11/1/16
@author: 欧光乾
@email: guangqianou@pateo.com.cn
'''
import time
from behave import when, then

from utils.helpTools import MAP_VAR, d, d_height, d_width, ht
from utils.uiTools import uit
from elements.music import music


@when(u'< 点击U盘音乐')
def step_impl(context):
    ele = music.get_music_usb_btn()
    if ele.wait.exists():
        x_coordinate, y_coordinate = uit.get_clickcoord_by_ele(ele)
        d.click(x_coordinate, y_coordinate)
    else:
        uit.raise_Exception_info('U盘音乐按钮不存在')


@when(u'< 点击蓝牙音乐')
def step_impl(context):
    ele = music.get_music_bt_btn()
    if ele.wait.exists():
        x_coordinate, y_coordinate = uit.get_clickcoord_by_ele(ele)
        d.click(x_coordinate, y_coordinate)
    else:
        uit.raise_Exception_info('蓝牙音乐按钮不存在')


@when(u'< 点击最爱音乐')
def step_impl(context):
    ele = music.get_music_mylove_btn()
    if ele.wait.exists():
        x_coordinate, y_coordinate = uit.get_clickcoord_by_ele(ele)
        d.click(x_coordinate, y_coordinate)
    else:
        uit.raise_Exception_info('最爱音乐按钮不存在')


@when(u'< 获取音乐名称')
def step_impl(context):
    # 获取接收参数
    music_name = context.table[0]['o_result']

    ele = music.get_music_name_ele()
    if ele.wait.exists():
        MAP_VAR[music_name] = ele.text.strip()
    else:
        uit.raise_Exception_info('音乐名称元素不存在')


@when(u'< 获取音乐歌手')
def step_impl(context):
    # 获取接收参数
    artist_name = context.table[0]['o_result']

    ele = music.get_music_artist_name_ele()
    if ele.wait.exists():
        MAP_VAR[artist_name] = ele.text.strip()
    else:
        uit.raise_Exception_info('音乐歌手元素不存在')


@when(u'< 点击音乐播放或暂停')
def step_impl(context):
    x_coordinate, y_coordinate = music.get_music_play_pause_coordinate()
    d.click(x_coordinate, y_coordinate)


@when(u'< 点击歌手列表')
def step_impl(context):
    ele = music.get_music_artists_list_btn()
    if ele.wait.exists():
        ele.click.wait()
    else:
        uit.raise_Exception_info('歌手列表按钮不存在')


@when(u'< 点击专辑列表')
def step_impl(context):
    ele = music.get_music_album_list_btn()
    if ele.wait.exists():
        ele.click.wait()
    else:
        uit.raise_Exception_info('专辑列表按钮不存在')


@when(u'< 点击文件夹列表')
def step_impl(context):
    ele = music.get_music_folder_list_btn()
    if ele.wait.exists():
        ele.click.wait()
    else:
        uit.raise_Exception_info('文件夹列表按钮不存在')


@when(u'< 点击音乐语音按钮')
def step_impl(context):
    ele = music.get_music_ivoka_btn()
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info('音乐语音按钮不存在')


@when(u'< 点击音乐底部返回按钮')
def step_impl(context):
    ele = music.get_music_bottom_back_btn()
    if ele.wait.exists():
        ele.click.wait()
    else:
        uit.raise_Exception_info('音乐底部返回按钮不存在')


@when(u'< 点击音乐底部主页按钮')
def step_impl(context):
    ele = music.get_music_bottom_home_btn()
    if ele.wait.exists():
        ele.click.wait()
    else:
        uit.raise_Exception_info('音乐底部主页按钮不存在')


@when(u'< 点击音乐上一首')
def step_impl(context):
    ele = music.get_music_prev_btn()
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info('音乐上一首按钮不存在')


@when(u'< 点击音乐下一首')
def step_impl(context):
    ele = music.get_music_next_btn()
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info('音乐下一首按钮不存在')


@when(u'< 快进音乐')
def step_impl(context):
    ele = music.get_music_next_btn()
    cur_time = music.get_music_cur_time_ele()
    cur_music_name = music.get_music_name_ele()
    if ele.wait.exists():
        # 获取当前时间秒数
        before_time = cur_time.text.strip().split(':')
        before_seconds = int(before_time[0]) * 60 + int(before_time[1])

        before_music_name = cur_music_name.text.strip()

        bounds = ele.info['bounds']
        x = (bounds['left'] + bounds['right']) / 2
        y = (bounds['bottom'] + bounds['top']) / 2
        # 长按下一首按钮
        d.swipe(x, y, x, y, 50)

        #获取快进后的时间
        time_ele = music.get_music_cur_time_ele()
        music_name_ele = music.get_music_name_ele()
        after_time = time_ele.text.strip().split(':')
        after_seconds = int(after_time[0]) * 60 + int(after_time[1])

        after_music_name = music_name_ele.text.strip()

        if after_seconds - before_seconds > 10 and before_music_name == after_music_name:
            pass
        else:
            uit.raise_Exception_info('快进异常')


    else:
        uit.raise_Exception_info('快进按钮不存在')


@when(u'< 快退音乐')
def step_impl(context):
    ele = music.get_music_prev_btn()
    cur_time = music.get_music_cur_time_ele()
    cur_music_name = music.get_music_name_ele()
    if ele.wait.exists():
        # 获取当前时间秒数
        before_time = cur_time.text.strip().split(':')
        before_seconds = int(before_time[0]) * 60 + int(before_time[1])

        before_music_name = cur_music_name.text.strip()

        bounds = ele.info['bounds']
        x = (bounds['left'] + bounds['right']) / 2
        y = (bounds['bottom'] + bounds['top']) / 2
        # 长按上一首按钮
        d.swipe(x, y, x, y, 50)

        #获取快进后的时间
        time_ele = music.get_music_cur_time_ele()
        music_name_ele = music.get_music_name_ele()
        after_time = time_ele.text.strip().split(':')
        after_seconds = int(after_time[0]) * 60 + int(after_time[1])

        after_music_name = music_name_ele.text.strip()

        if before_seconds - after_seconds > 5 and before_music_name == after_music_name:
            pass
        else:
            uit.raise_Exception_info('快退异常')

    else:
        uit.raise_Exception_info('快退按钮不存在')


@when(u'< 点击音乐收藏按钮')
def step_impl(context):
    # 获取入参确定选项
    yes_or_no = context.table[0]['option']
    ele = music.get_music_collect_btn()
    if ele.wait.exists():
        ele.click()
        if yes_or_no.lower() == 'yes':
            choice = d(text='是')
            if choice.wait.exists():
                choice.click()
            else:
                uit.raise_Exception_info('收藏弹出框不存在')
        elif yes_or_no.lower() == 'no':
            choice = d(text='否')
            if choice.wait.exists():
                choice.click()
            else:
                uit.raise_Exception_info('收藏弹出框不存在')
        else:
            pass
    else:
        uit.raise_Exception_info('收藏按钮不存在')


@when(u'< 点击歌手收藏按钮')
def step_impl(context):
    # 获取要收藏或者取消收藏的歌手名字
    artist_name = context.table[0]['artist_name']
    yes_or_no = context.table[0]['option']
    ele = music.get_music_collect_btn_by_artist(artist_name)

    if ele.wait.exists():
        ele.click()
        if yes_or_no.lower() == 'yes':
            choice = d(text='是')
            if choice.wait.exists():
                choice.click()
            else:
                uit.raise_Exception_info('收藏弹出框不存在')
        elif yes_or_no.lower() == 'no':
            choice = d(text='否')
            if choice.wait.exists():
                choice.click()
            else:
                uit.raise_Exception_info('收藏弹出框不存在')
        else:
            pass
    else:
        uit.raise_Exception_info('收藏按钮不存在')


@when(u'< 点击专辑收藏按钮')
def step_impl(context):
    # 获取要收藏或者取消收藏的专辑名字
    album_name = context.table[0]['album_name']
    yes_or_no = context.table[0]['option']
    ele = music.get_music_collect_btn_by_album(album_name)
    if ele.wait.exists():
        ele.click()
        if yes_or_no.lower() == 'yes':
            choice = d(text='是')
            if choice.wait.exists():
                choice.click()
            else:
                uit.raise_Exception_info('收藏弹出框不存在')
        elif yes_or_no.lower() == 'no':
            choice = d(text='否')
            if choice.wait.exists():
                choice.click()
            else:
                uit.raise_Exception_info('收藏弹出框不存在')
        else:
            pass
    else:
        uit.raise_Exception_info('收藏按钮不存在')


@when(u'< 点击收藏列表收藏按钮')
def step_impl(context):
    # 获取要收藏或者取消收藏的收藏标题
    collect_name = context.table[0]['collect_name']
    yes_or_no = context.table[0]['option']

    ele = music.get_music_collect_btn_by_collect(collect_name)
    if ele.wait.exists():
        ele.click()
        if yes_or_no.lower() == 'yes':
            choice = d(text='是')
            if choice.wait.exists():
                choice.click()
            else:
                uit.raise_Exception_info('收藏弹出框不存在')
        elif yes_or_no.lower() == 'no':
            choice = d(text='否')
            if choice.wait.exists():
                choice.click()
            else:
                uit.raise_Exception_info('收藏弹出框不存在')
        else:
            pass
    else:
        uit.raise_Exception_info('收藏按钮不存在')


@when(u'< 点击音乐收藏列表中指定名称')
def step_impl(context):
    # 获取音乐名称
    music_name = context.table[0]['music_name']

    ele = music.get_music_from_collect_list_by_music_name(music_name)
    if ele.wait.exists():
        x_coordinate, y_coordinate = uit.get_clickcoord_by_ele(ele)
        d.click(x_coordinate, y_coordinate)
    else:
        uit.raise_Exception_info('指定音乐不存在')


@when(u'< 点击专辑收藏列表中指定专辑')
def step_impl(context):
    # 获取专辑名称
    album_name = context.table[0]['album_name']

    ele = music.get_album_from_album_list_by_album_name(album_name)
    if ele.wait.exists():
        x_coordinate, y_coordinate = uit.get_clickcoord_by_ele(ele)
        d.click(x_coordinate, y_coordinate)
    else:
        uit.raise_Exception_info('指定专辑不存在')


@when(u'< 点击歌手收藏列表中指定歌手')
def step_impl(context):
    # 获取专辑名称
    artist_name = context.table[0]['artist_name']

    ele = music.get_artist_from_artist_list_by_artist_name(artist_name)
    if ele.wait.exists():
        x_coordinate, y_coordinate = uit.get_clickcoord_by_ele(ele)
        d.click(x_coordinate, y_coordinate)
    else:
        uit.raise_Exception_info('指定歌手不存在')


@when(u'< 获取音乐收藏列表指定音乐的专辑名')
def step_impl(context):
    # 获取音乐名称和接收参数
    music_name = context.table[0]['music_name']
    album_name = context.table[0]['o_result']

    ele = music.get_music_album_from_collect_list_by_music_name(music_name)
    if ele.wait.exists():
        MAP_VAR[album_name] = ele.text.strip()
    else:
        uit.raise_Exception_info('指定音乐不存在')


@when(u'< 获取音乐收藏列表指定音乐的歌手名')
def step_impl(context):
    # 获取音乐名称和接收参数
    music_name = context.table[0]['music_name']
    artist_name = context.table[0]['o_result']

    ele = music.get_music_artist_from_collect_list_by_music_name(music_name)
    if ele.wait.exists():
        MAP_VAR[artist_name] = ele.text.strip()
    else:
        uit.raise_Exception_info('指定音乐不存在')


@when(u'< 点击音乐分享至U盘')
def step_impl(context):
    ele = music.get_music_share_btn()
    if ele.wait.exists():
        ele.click()
    else:
        uit.raise_Exception_info('音乐分享按钮不存在')


@then(u'< 验证音乐播放状态')
def step_impl(context):
    # 获取音乐期望播放状态
    status = context.table[0]['status']
    time.sleep(1.5)

    # 获取音乐播放按钮和音乐当前播放时间
    play_ele = music.get_music_play_btn()
    before_time = music.get_music_cur_time_ele()
    before_time_txt = before_time.text.strip() if before_time.wait.exists() else None

    time.sleep(4)

    after_time = music.get_music_cur_time_ele()
    after_time_txt = after_time.text.strip() if after_time.wait.exists() else None

    if play_ele.exists:
        #判断如果是蓝牙音乐的情况
        if before_time.wait.exists():
            if before_time_txt == after_time_txt:
                if status.lower() != 'false':
                    uit.raise_Exception_info('播放状态验证失败，期望状态为播放，实际状态为暂停')
            else:
                uit.raise_Exception_info('播放状态暂停，时间进度还在继续')
        else:
            if status.lower() != 'false':
                    uit.raise_Exception_info('播放状态验证失败，期望状态为播放，实际状态为暂停')

    else:
        if before_time.wait.exists():
            if before_time_txt == after_time_txt:
                uit.raise_Exception_info('播放状态为播放，时间进度为暂停')
            else:
                if status.lower() != 'true':
                    uit.raise_Exception_info('播放状态验证失败，期望状态为暂停，实际状态为播放')
        else:
            if status.lower() != 'true':
                    uit.raise_Exception_info('播放状态验证失败，期望状态为暂停，实际状态为播放')


@then(u'< 验证是U盘音乐')
def step_impl(context):
    # 获取音乐名称
    music_name = context.table[0]['music_name']
    # 获取usb歌曲列表
    usb_music_tuple = ht.get_usb_music()
    if music_name not in usb_music_tuple:
        uit.raise_Exception_info('指定音乐名称《' + music_name + '》不是U盘音乐')


@then(u'< 验证音乐是否收藏')
def step_impl(context):
    # 获取音乐名称和期望收藏状态
    music_name = context.table[0]['music_name']
    collected_status = context.table[0]['collected_status']

    flag = music.get_music_collect_status_from_collect_list_by_name(music_name)
    if collected_status.lower() != str(flag).lower():
        uit.raise_Exception_info('指定音乐《' + music_name + '》收藏状态不一致')


@then(u'< 验证歌手是否收藏')
def step_impl(context):
    # 获取歌手名称和期望收藏状态
    artist_name = context.table[0]['artist_name']
    collected_status = context.table[0]['collected_status']

    flag = music.get_artist_collect_status_from_artist_list_by_name(artist_name)
    if collected_status.lower() != str(flag).lower():
        uit.raise_Exception_info('指定歌手《' + artist_name + '》收藏状态不一致')


@then(u'< 验证专辑是否收藏')
def step_impl(context):
    # 获取专辑名称和期望收藏状态
    album_name = context.table[0]['album_name']
    collected_status = context.table[0]['collected_status']

    flag = music.get_album_collect_status_from_album_list_by_name(album_name)
    if collected_status.lower() != str(flag).lower():
        uit.raise_Exception_info('指定专辑《' + album_name + '》收藏状态不一致')


@then(u'< 验证音乐从头播放')
def step_impl(context):
    # 获取音乐播放时间，验证音乐播放时间小于5s
    cur_time_ele = music.get_music_cur_time_ele()
    if cur_time_ele.wait.exists():
        cur_time = cur_time_ele.text.strip()
        if cur_time.split(':')[0] == '00' and int(cur_time.split(':')[1]) < 5:
            pass
        else:
            uit.raise_Exception_info('音乐从头播放失败')
    else:
        uit.raise_Exception_info('当前播放时间元素不存在')


@when(u'< 滑动展示音乐搜索框')
def step_impl(context):
    d.swipe(d_width / 2, 100, d_width / 2, d_height / 2, 10)


@when(u'< 输入音乐搜索关键字')
def step_impl(context):
    # 获取关键字内容
    search_word = context.table[0]['search_word']

    ele = music.get_music_search_ele()
    if ele.wait.exists():
        ele.clear_text()
        ele.set_text(ht.unicode_input(search_word))
    else:
        uit.raise_Exception_info('搜索框不存在')


@when(u'< 清空音乐搜索框')
def step_impl(context):
    ele = music.get_music_search_ele()
    if ele.wait.exists():
        ele.long_click.topleft()
        d(text='剪切').click()
    else:
        uit.raise_Exception_info('搜索框不存在')




