#!/usr/bin/env python
# -*- coding: utf-8 -*-
#work well with python2.7

import pythoncom
import pyHook
import time


def onMouseEvent(event):
    # print('-' * 20 + 'MouseEvent Begin' + '-' * 20 + '')
    # print("Current Time:%s" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
    # print("MessageName:%s" % str(event.MessageName))
    # print("Message:%d" % event.Message)
    # print("Time_sec:%d" % event.Time)
    # print("Window:%s" % str(event.Window))
    # print("WindowName:%s" % str(event.WindowName))
    # print("Position:%s" % str(event.Position))
    # print('-' * 20 + 'MouseEvent End' + '-' * 20 + '')
    return True


def onKeyboardEvent(event):
    # print('-' * 20 + 'Keyboard Begin' + '-' * 20 + '')
    # print("Current Time:%s" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
    print("MessageName:%s" % str(event.MessageName))
    print("Message:%d" % event.Message)
    print("Time:%d" % event.Time)
    print("Window:%s" % str(event.Window))
    print("WindowName:%s" % str(event.WindowName))
    print("Ascii_code: %d" % event.Ascii)
    print("Ascii_char:%s" % chr(event.Ascii))
    print("Key:%s" % str(event.Key))
    # print('-' * 20 + 'Keyboard End' + '-' * 20 + '')
    return False


if __name__ == "__main__":
    '''
    Function:操作SQLITE3数据库函数
    Input：NONE
    Output: NONE
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-03-1
    '''

    hm = pyHook.HookManager()

    hm.KeyAll = onKeyboardEvent
    hm.HookKeyboard()

    hm.MouseAll = onMouseEvent
    hm.HookMouse()

    pythoncom.PumpMessages()
