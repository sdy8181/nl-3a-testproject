# language: zh-CN
功能: 点击主页应用
  @musicTest
场景: 点击主页应用
当< 滑动主页到指定屏
|number|
|2     |
当< 点击主页应用
  |app_name|
  |音乐 |
当< 延时
  |sleep_time|
  |5        |
当< 点击最爱音乐
当< 点击音乐上一首
那么< 验证音乐从头播放
当< 延时
  |sleep_time|
  |5        |
当< 点击音乐下一首
当< 延时
|sleep_time|
|5         |
当< 点击U盘音乐
那么< 验证文本是否存在
|text|exists_flag|
|请插入U盘|true      |
当< 点击蓝牙音乐
那么< 验证文本是否存在
|text|exists_flag|
|请开启蓝牙|true      |
当< 点击最爱音乐
当< 获取音乐名称
|o_result|
|o_name  |
当< 获取音乐歌手
|o_result|
|o_artist|
那么< 验证对象值
|param1|option|param2|
|o_name|!=    |o_artist|
当< 点击音乐播放或暂停
那么< 验证音乐播放状态
|status|
|false  |
当< 点击音乐播放或暂停
当< 点击歌手列表
当< 点击歌手收藏按钮
|artist_name|option|
|未知歌手       |no    |
当< 点击音乐底部返回按钮
当< 点击专辑列表
当< 点击专辑收藏按钮
|album_name|option|
|   未知专辑|no    |
当< 点击音乐底部返回按钮
当< 点击文件夹列表
当< 点击收藏列表收藏按钮
|collect_name|option|
|送你一份吉利 |no    |
当< 获取音乐收藏列表指定音乐的专辑名
|music_name|o_result|
|送你一份吉利    |o_album_name|
当< 获取音乐收藏列表指定音乐的歌手名
|music_name|o_result|
|送你一份吉利    |o_artist|
那么< 验证音乐是否收藏
|music_name|collected_status|
|送你一份吉利1    |false           |
那么< 验证音乐是否收藏
|music_name|collected_status|
|送你一份吉利    |true           |
当< 点击音乐收藏列表中指定名称
|music_name|
|送你一份吉利    |
当< 点击音乐分享至U盘
当< 延时
|sleep_time|
|    5     |
当< 点击音乐语音按钮
那么< 验证音乐播放状态
|status|
|false  |
当< 延时
|sleep_time|
|    10     |
当< 点击文件夹列表
当< 滑动展示音乐搜索框
当< 输入音乐搜索关键字
|search_word|
|jjz       |
当< 延时
|sleep_time|
|    10     |
当< 清空音乐搜索框
那么< 验证音乐收藏列表播放状态
|music_name|play_status|
|送你一份吉利    |true       |
当< 点击音乐收藏列表中指定名称
|music_name|
|送你一份吉利    |
当< 延时
|sleep_time|
|    10     |
当< 快进音乐
当< 快退音乐
当< 点击音乐收藏按钮
|option|
|no    |
那么< 验证是U盘音乐
|music_name|
|送你一份吉利    |


当< 点击音乐底部主页按钮
@clearTest
场景: 清空
  当< 滑动主页到指定屏
  |number|
  |   2  |
  当< 点击主页应用
  |app_name|
  |音乐|
  当< 延时
  |sleep_time|
  |5         |
  当< 快退音乐


  @processtest
场景: 下拉收起进程栏
    当< 下拉进程菜单
    当< 延时
    |sleep_time|
    |5        |
    当< 收起进程菜单
    当< 延时
    |sleep_time|
    |5        |
#    那么< 验证主页日期天气格式
    那么< 验证主页音乐播放状态
    |status|
    |true  |

@homeTest
场景: 验证主页步骤
  当< 滑动主页到指定屏
  |number|
  |2     |
  当< 点击主页音乐播放暂停
  当< 延时
  |sleep_time|
  |5        |
  当< 点击主页音乐上一首
  当< 延时
  |sleep_time|
  |5        |
  当< 点击主页音乐下一首
  当< 延时
  |sleep_time|
  |5        |
  当< 获取主页音乐名称
  |o_result|
  |o_name  |
  当< 获取主页音乐歌手
  |o_result|
  |o_artist|
  那么< 验证主页音乐播放状态
  |status|
  |true  |
  当< 滑动主页到指定屏
  |number|
  |3     |
  那么< 验证音频通道
  |chk_tinymix|
  |ASP MEDIA Route|
  那么< 验证主页日期天气格式

  @commonTest
  场景: 验证公共步骤
  当< 播放音频文件
  |voice_file|
  |上一首.m4a   |
  那么< 验证当前应用
  |app_name|
  |主页      |
  那么< 验证对象值
  |param1|option|param2|
  |aaa   |!=    |bbb   |
  那么< 验证文本是否存在
  |text|exists_flag|
  |ssss|false      |
    当< 下拉进程菜单
    当< 延时
    |sleep_time|
    |5         |
  当< 按硬按键
    |key|
    |HoMe|

@radioTest
场景:验证播放指定电台
  当< 滑动主页到指定屏
    |number|
    |2     |
当< 点击主页应用
  |app_name|
  |收音机  |

当< 点击电台收藏
当< 点击FM与AM切换
当< 点击收音机下一台
当< 点击收音机上一台
当< 点击自动电台扫描
当< 点击预览电台扫描
当< 点击电台列表
当< 点击电台收藏列表
当< 点击底部控制栏返回按钮
当< 点击底部控制栏Home按钮
当< 滑动收音机节目单到最前
当< 滑动收音机节目单到最尾部

那么< 验证收音机当前状态为播放
当< 点击收音机播放与暂停切换区
那么< 验证收音机当前状态为暂停
那么< 验证收音机节目列表不为空
那么< 验证收音机收藏节目列表不为空
那么< 验证正在预览电台
那么< 验证正在重新搜台
那么< 验证扫描后结果为空

当< 滑动收音机节目列表到指定台
  |radio_station|
  |105.8    |
当< 获取当前播放电台名称
  |o_station_name|
  |o_FM_name     |

那么< 验证两次获取的电台名称是一致的
  |param1|param2|
  |91.4 |o_FM_name|
那么< 验证两次获取的电台名称不一致的
  |param1|param2|
  |91.4 |o_FM_name|














@radioTest2
场景:验证FM与AM
当< 滑动主页到指定屏
    |number|
    |2     |
当< 点击主页应用
  |app_name|
  |收音机  |
当< 点击电台收藏列表
那么< 验证正在预览电台






@radioTest3
场景: 播放与暂停
  当< 滑动主页到指定屏
    |number|
    |2     |
当< 点击主页应用
  |app_name|
  |收音机  |
那么< 验证收音机当前状态为播放
当< 点击收音机播放与暂停切换区
那么< 验证收音机当前状态为暂停


@RadioCollect
场景: 收藏
  当< 滑动主页到指定屏
    |number|
    |2     |
当< 点击主页应用
  |app_name|
  |收音机  |
  当< 获取当前收音机节目收藏状态
  |o_radio_collect_state|
  |o_state1          |
  当< 点击电台收藏
  当< 获取当前收音机节目收藏状态
  |o_radio_collect_state|
  |o_state2          |
  那么< 验证点击收藏按钮后状态响应正确
  |param1|param2|
  |o_state1|o_state2|
















