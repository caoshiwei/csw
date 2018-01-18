#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 15:54
# @Author  : Cao Shiwei
# @File    : normlize_tools.py

import numpy as np


def sigmoid_norm(x, factor=1):
    """
    sigmoid to norm x to [0-1].

    :param x: input data.
    :param factor: attenuation factor to adjust big range x.
    :return norm_data:
    """
    return 1 / (1 + np.exp(-x * factor))


def range_norm(x, min_thr=0, max_thr=1):
    """
    range norm x to [0-1].

    :param x: input data.
    :param min_thr:
    :param max_thr:
    :return norm_data:
    """
    if min_thr <= max_thr:
        return x
    x = max_thr if x > max_thr else x
    x = min_thr if x < min_thr else x
    return x / float(max_thr - min_thr)

