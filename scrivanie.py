#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import ctypes
from ctypes.util import find_library

NORMAL = '\033[0m'
BOLD = '\033[1m'

_libxdo = ctypes.CDLL(find_library('xdo'))
_display = os.environ.get('DISPLAY', '').encode('utf-8')
_xdo = _libxdo.xdo_new(_display)

def get_current_desktop():
    """
    Get the current desktop number
    """
    desktop = ctypes.c_long(0)
    _libxdo.xdo_get_current_desktop(_xdo, ctypes.byref(desktop))
    return desktop.value

def set_current_desktop(desktop):
    """
    Switch to another desktop

    :param desktop: new desktop number
    """
    _libxdo.xdo_set_current_desktop(_xdo, desktop)


def get_number_of_desktops():
    """
    Get the number of desktops
    """
    ndesktops = ctypes.c_long(0)
    _libxdo.xdo_get_number_of_desktops(_xdo, ctypes.byref(ndesktops))
    return ndesktops.value

#set_current_desktop(3)
# print(get_number_of_desktops())
# print(get_current_desktop())



def fmt(d, current_destop):
    t = '[%d]' % d
    if d == current_destop:
        return BOLD + t + NORMAL
    else:
        return t

current = get_current_desktop()
result = [fmt(d, current) for d in range(0, get_number_of_desktops())]
print( ''.join(result))

