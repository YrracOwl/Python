#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tkinter as tk
import SanJingGua as SJG
import LiuShiSiGua as LSSG

ShiYing_Tuple = ("世","  ","  ","应","  ","  ")
yao_pos = ("上", "五", "四", "三", "二", "初")


def biangua(waidongyao, neidongyao,waigua,neigua):
    waigua_bian = SJG.BaGuaUp(waigua.dongyao(waidongyao))
    neigua_bian = SJG.BaGuaDown(neigua.dongyao(neidongyao))
    Gua_BIAN = [0, 0, 0, 0, 0, 0]
    for counters in range(3):
        if waidongyao[counters] == 1:
            Gua_BIAN[counters] = "化" + waigua_bian[counters]
        if waidongyao[counters] == 0:
            Gua_BIAN[counters] = " "

    for counters in range(3):
        if neidongyao[counters] == 1:
            Gua_BIAN[counters+3] = "化" + neigua_bian[counters]
        if neidongyao[counters] == 0:
            Gua_BIAN[counters+3] = " "

    return Gua_BIAN

#输出到Scrolledtext
def output_4(scr,biangua,wuxing,waidongyao,neidongyao):
    dongyaoLiuqin = LSSG.AnLiuQin(wuxing,biangua[0:3],biangua[3:6])
    scr.config(state='normal')
    scr.delete('0.0', 'end')
    for counters in range(3):
        if waidongyao[counters] == 1:
            scr.insert('end',biangua[counters] + dongyaoLiuqin[counters] + '\n\n')
    for counters in range(3):
        if neidongyao[counters] == 1:
            scr.insert('end',biangua[counters+3] + dongyaoLiuqin[counters+3] + '\n\n')
    scr.config(state='disabled')

#输出到左侧LabelFrame以及scrolledtext中
def output_1(frames,ganzhi,shiyao,liuqin,waidongyao, neidongyao, liushen, waigua, neigua,yongshen,flag_zhuang,scr,wuxing):
    for counters in range(9):
        tk.Label(frames, text="", font=("Microsoft YaHei", 12)).grid(column=0, row=counters, sticky="W")
    #世应
    for counters in range(6):
        tk.Label(frames, text=ShiYing_Tuple[counters], font=("Microsoft YaHei", 12),anchor="w", width=2).grid(column=0, row=(6 - shiyao + counters)%6, sticky="W")

    #卦象
    for counters in range(3):
        tk.Label(frames, text=waigua.shape[counters], font=("Microsoft YaHei", 12)).grid(column=1, row=counters, sticky="W")

    for counters in range(3):
        tk.Label(frames, text=neigua.shape[counters], font=("Microsoft YaHei", 12)).grid(column=1, row=counters + 3, sticky="W")

    #每一爻的位置
    for counters in range(6):
        tk.Label(frames, text=yao_pos[counters], font=("Microsoft YaHei", 12),anchor="w").grid(column=2, row=counters, sticky="W")

    #用神位置
    if flag_zhuang == 1:
        for counters in range(6):
            tk.Label(frames, text=yongshen[counters], font=("Microsoft YaHei", 12), anchor="w", width=4, fg='blue').grid(column=3, row=counters, sticky="W")
    elif flag_zhuang == 0 :
        for counters in range(6):
            tk.Label(frames, text="", font=("Microsoft YaHei", 12), anchor="w", width=4, fg='blue').grid(column=3, row=counters, sticky="W")
    #六亲
    for counters in range(6):
        tk.Label(frames, text=liuqin[counters], font=("Microsoft YaHei", 12),anchor="w").grid(column=4, row=counters, sticky="W")

    #干支
    for counters in range(6):
        tk.Label(frames, text=ganzhi[counters], font=("Microsoft YaHei", 12),anchor="w").grid(column=5, row=counters, sticky="W")

    #变卦
    BIANGUA = biangua(waidongyao, neidongyao, waigua, neigua)
    for counters in range(6):
        tk.Label(frames, text=BIANGUA[counters], font=("Microsoft YaHei", 12), width=5, anchor="w", fg='red').grid(column=6, row=counters, sticky="W")

    #六神
    for counters in range(6):
        tk.Label(frames, text=liushen[counters], font=("Microsoft YaHei", 12),anchor="w").grid(column=7, row=counters, sticky="W")

    #将动爻输出到scrolledtext中
    output_4(scr, BIANGUA, wuxing, waidongyao, neidongyao)


#输出到右侧LabelFrame
def output_2(frames, yuexiang, rixiang, kongwang, wuxing64, BenGuaGong, yueming, riming):
    #本卦宫卦象
    for counters in range(6):
        tk.Label(frames, text=BenGuaGong.shape[counters % 3], font=("Microsoft YaHei", 12), anchor="w").grid(column=0, row=counters, sticky="W")

    #本卦宫干支五行
    dizhiup = SJG.BaGuaUp(BenGuaGong.number)
    dizhidown = SJG.BaGuaUp(BenGuaGong.number)
    for counters in range(3):
        tk.Label(frames, text=dizhiup[counters], font=("Microsoft YaHei", 12), anchor="w", width=6).grid(column=2, row=counters, sticky="W")
    for counters in range(3):
        tk.Label(frames, text=dizhidown[counters], font=("Microsoft YaHei", 12), anchor="w", width=6).grid(column=2, row=counters+3, sticky="W")
    tk.Label(frames, text="卦宫：" + BenGuaGong.name + "卦", font=("Microsoft YaHei", 12), anchor="center").grid(column=0, row=6, sticky="we")
    tk.Label(frames, text="五行：" + "属" +wuxing64 , font=("Microsoft YaHei", 12)).grid(column=0, row=7, sticky="we")

    # 卦宫六亲
    liuqin = LSSG.AnLiuQin(wuxing64, dizhiup,dizhidown)
    for counters in range(6):
        tk.Label(frames, text=liuqin[counters], font=("Microsoft YaHei", 12), anchor="w").grid(column=1, row=counters, sticky="W")

    #月建月破
    tk.Label(frames, text="月建：" + yueming + yuexiang[0], font=("Microsoft YaHei", 12), anchor="w", width=8).grid(column=3, row=0, sticky="W")
    tk.Label(frames, text="月破：" + yuexiang[1], font=("Microsoft YaHei", 12), anchor="w", width=8).grid(column=3, row=1, sticky="W")
    #日建日冲空亡
    tk.Label(frames, text="日建：" + riming + rixiang[0], font=("Microsoft YaHei", 12), anchor="w", width=8).grid(column=3, row=3, sticky="W")
    tk.Label(frames, text="日冲：" + rixiang[1], font=("Microsoft YaHei", 12), anchor="w", width=8).grid(column=3, row=4, sticky="W")
    tk.Label(frames, text="空亡：" + kongwang[0] + kongwang[1], font=("Microsoft YaHei", 12), anchor="w", width=8).grid(column=3, row=5, sticky="w")

#输出选取的用神
def output_3(frames,yongshen):
    for counters in range(6):
        tk.Label(frames, text=yongshen[counters], font=("Microsoft YaHei", 12), anchor="w", width=3, fg='blue').grid(column=3, row=counters, sticky="W")


#所求卦象的名称
def output_5(frames,flagup,flagdown):
    tk.Label(frames, text=LSSG.liushisi_Gua.get((flagup,flagdown)), font=("Microsoft YaHei", 12), anchor="center",width=6).grid(column=1, row=6, sticky="WE")