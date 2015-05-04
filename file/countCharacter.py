#! /usr/bin/python
# coding=UTF-8

import sys

# 统计字符个数
def wc(file_name):
    fo = open(file_name)
    wc = 0;
    for line in fo:
        wc += len(line.decode("gbk")) #不能utf-8
    print wc, file_name

arg=raw_input("输入文件：")               

wc(arg)
