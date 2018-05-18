#!usr/bin/env python
#-*- coding: utf-8 -*-

import SanJingGua as SJG
import LiuShiSiGua as LSSG
import YueRi as YR

ShiYing_Tuple = ("世","  ","  ","应","  ","  ")


# 卦形返回函数
def returnShape(guaup,guadown):
    gua = [0, 0, 0, 0, 0, 0]
    for counters in range(3):
        gua[counters] = guaup[counters]
    for counters in range(3):
        gua[counters+3] = guadown[counters]

    return gua

# 返回长度为6的世应列表
def shiyingReturn(shi):
    text = [0, 0 ,0 ,0 ,0 ,0]
    for counters in range(6):
        text[(6 - shi + counters)%6] = ShiYing_Tuple[counters]

    return text

# 三经卦预处理
def sanjingPre(data):
    originYao_Up = data[0:3]
    originYao_Down = data[3:6]

    zhiYao_Up = [0, 0, 0]
    zhiYao_Down = [0, 0, 0]

    for counters in range(3):
        if (originYao_Up[counters] == "9") or (originYao_Up[counters] == "1"):
            zhiYao_Up[counters] = "Yang"
        elif (originYao_Up[counters] == "6") or (originYao_Up[counters] == "2"):
            zhiYao_Up[counters] = "Yin"
    for counters in range(3):
        if (originYao_Down[counters] == "9") or (originYao_Down[counters] == "1"):
            zhiYao_Down[counters] = "Yang"
        elif (originYao_Down[counters] == "6") or (originYao_Down[counters] == "2"):
            zhiYao_Down[counters] = "Yin"

    return zhiYao_Up,zhiYao_Down

# 动爻预处理
def dongyaoPre(data):
    originYao_Up = data[0:3]
    originYao_Down = data[3:6]

    activeYao_Up = [0, 0, 0]
    activeYao_Down = [0, 0, 0]

    for counters in range(3):
        if (originYao_Up[counters] == "9")or(originYao_Up[counters] == "6"):
            activeYao_Up[counters] = 1
        elif (originYao_Up[counters] == "1")or(originYao_Up[counters] == "2"):
            activeYao_Up[counters] = 0
    for counters in range(3):
        if (originYao_Down[counters] == "9")or(originYao_Down[counters] == "6"):
            activeYao_Down[counters] = 1
        elif (originYao_Down[counters] == "1")or(originYao_Down[counters] == "2"):
            activeYao_Down[counters] = 0

    return activeYao_Up,activeYao_Down

# 三经卦先天数的查找
def searchSanJing(yinyangGua):
    if yinyangGua == ["Yang","Yang","Yang"]:
        return 1
    if yinyangGua == ["Yin", "Yang", "Yang"]:
        return 2
    if yinyangGua == ["Yang", "Yin", "Yang"]:
        return 3
    if yinyangGua == ["Yin", "Yin", "Yang"]:
        return 4
    if yinyangGua == ["Yang", "Yang", "Yin"]:
        return 5
    if yinyangGua == ["Yin", "Yang", "Yin"]:
        return 6
    if yinyangGua == ["Yang", "Yin", "Yin"]:
        return 7
    if yinyangGua == ["Yin", "Yin", "Yin"]:
        return 8

# 月日判断
def timeDetect(data):
    if ((data[6] == "当前月份")or(data[6] == "")) and ((data[7] =="当前日辰")or(data[7] =="")):
        return data[8],data[9]
    elif((data[6] == "当前月份")or(data[6] == "")) and ((data[7] !="当前日辰")and(data[7] !="")):
        return data[8],data[7]
    elif ((data[6] != "当前月份")and(data[6] != "")) and ((data[7] =="当前日辰")or(data[7] =="")):
        return data[6], data[9]
    elif ((data[6] != "当前月份")and(data[6] != "")) and ((data[7] =="当前日辰")and(data[7] =="")):
        return data[6], data[7]

#数据处理
def dataProcessing(data):
    activeYao = data[0:6]
    outputLog = [["出错", "出错", "出错", "出错", "出错", "出错"], ["出错", "出错", "出错"], ["出错", "出错", "出错"], ["出错", "出错", "出错", "出错", "出错", "出错"],
                 ["出错", "出错", "出错", "出错", "出错", "出错"], "出错", ["出错", "出错", "出错", "出错", "出错", "出错"], ["出错", "出错", "出错", "出错", "出错", "出错"],
                 ["出错", "出错", "出错"],  ["出错", "出错", "出错"],  ["出错", "出错", "出错", "出错", "出错", "出错"],
                 ["出错", "出错", "出错", "出错", "出错", "出错"], "出错", "出错", "出错", "出错", ["出错", "出错"], "出错", "出错", "出错", "出错"]
    flag = "True"
    if (activeYao[0] == '')or(activeYao[1] == '')or(activeYao[2] == '')or(activeYao[3] == '')or(activeYao[4] == '')or(activeYao[5] == ''):
        flag = "False"
        return flag,outputLog[0],outputLog[1],outputLog[2],outputLog[3],outputLog[4],outputLog[5],outputLog[6],outputLog[7],outputLog[8],outputLog[9],outputLog[10],outputLog[11],outputLog[12],outputLog[13],outputLog[14],outputLog[15],outputLog[16],outputLog[17],outputLog[18],outputLog[19],outputLog[20]
    else:
        # 三经卦预处理
        zhiYao_Up, zhiYao_Down = sanjingPre(data)
        # 获取先天数
        num_Up = searchSanJing(zhiYao_Up)
        num_Down = searchSanJing(zhiYao_Down)
        # 获取上下经卦动爻
        activeYao_Up, activeYao_Down = dongyaoPre(data)

        # 所起卦上卦下卦形状
        guaup = SJG.Bagua_Dict.get(num_Up)
        guadown = SJG.Bagua_Dict.get(num_Down)

        # 卦象干支
        activeGanZhi = [0, 0, 0, 0, 0, 0]
        for counters in range(3):
            activeGanZhi[counters] = SJG.BaGuaUp(num_Up)[counters]
        for counters in range(3):
            activeGanZhi[counters + 3] = SJG.BaGuaDown(num_Down)[counters]

        # 卦象世应， 64卦五行， 安六亲, 卦所在宫
        shi, ying, gua64wuxing, liuqin, benguagong = LSSG.ShiYing_DingWuXing(num_Up, num_Down, SJG.BaGuaUp(num_Up),SJG.BaGuaDown(num_Down))

        # 获取世应列表
        shiying = shiyingReturn(shi)

        # 月份日辰的选取
        yuefen,richen = timeDetect(data)

        # 月建月破， 日建日破， 空亡日， 六神
        yuejian, yuepo, rijian, ripo, kongwangri, liushenPosition, month, day = YR.YueRiWuXing(yuefen, richen)



        if yuejian == "输入有误":
            flag = "False"
            return flag,outputLog[0],outputLog[1],outputLog[2],outputLog[3],outputLog[4],outputLog[5],outputLog[6],outputLog[7],outputLog[8],outputLog[9],outputLog[10],outputLog[11],outputLog[12],outputLog[13],outputLog[14],outputLog[15],outputLog[16],outputLog[17],outputLog[18],outputLog[19],outputLog[20]



        # 卦宫形状
        guaGongUp = SJG.Bagua_Dict.get(benguagong.number).shape
        guaGongDown = SJG.Bagua_Dict.get(benguagong.number).shape

        #卦宫六亲, 五行
        liuqin_gong, ganzhi_gong = LSSG.guaGong(gua64wuxing, benguagong)

        #本卦之卦卦名
        benguaName,zhiguaName = LSSG.find_names(num_Up,num_Down,benguagong.number,benguagong.number)

        #之卦动爻六亲五行
        guaBian = LSSG.biangua(activeYao_Up, activeYao_Down,guaup,guadown)

        return flag, shiying, guaup.shape, guadown.shape, liuqin, activeGanZhi, gua64wuxing, guaBian, liushenPosition, guaGongUp, guaGongDown, liuqin_gong, ganzhi_gong, yuejian, yuepo, rijian, ripo, kongwangri, benguaName, zhiguaName, month, day
