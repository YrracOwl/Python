#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import sys


#test pyinstaller
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)

#搜索万物取象
def searchEverything(text):
    temp = []
    lineList = []
    counters = 0
    with open(resource_path('BaGuaEverything.txt'),'r') as f:
        for eachline in f:
            lineList.append(eachline.rstrip("\n"))
            if text in eachline:
                temp = lineList[counters - 1]
            counters += 1

    if len(temp) == 0:
        temp_f = "未找到"
        return temp_f
    else:
        return temp

#搜索六十四卦周易
def search64Gua(text):
    temp_data = []
    flag_start = 0
    lineList = []
    counters = 0
    with open(resource_path('liushisiGua.txt'),'r') as f:
        for eachline in f:
            lineList.append(eachline.rstrip("\n"))
            if (text in eachline)and(flag_start == 0):
                flag_start = counters + 1
            elif flag_start != 0:
                temp_data.append(lineList[counters - 1])
                if 'end' in eachline:
                    return temp_data
            counters += 1

    return temp_data
    #for counters in len(temp_data):
    #    pass

