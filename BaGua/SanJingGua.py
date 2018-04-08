#!/usr/bin/env python
#-*- coding: utf-8 -*-


#乾1
class Qian(object):
    def __init__(self,flagup=0,flagdown=0):
        self.name = "乾"
        self.number = 1
        self.shape = ("█████████","█████████","█████████")
        self.wuxing = "金"
        self.yaobian = {(0, 0, 0): 1, (1, 0, 0): 2, (0, 1, 0): 3, (0, 0, 1): 5, (1, 1, 0): 4, (1, 0, 1): 6,
                        (0, 1, 1): 7, (1, 1, 1): 8}

        self.dizhi = ("", "", "")
        self.flagup = flagup == 1
        self.flagdown = flagdown == 1

        if self.flagup:
            self.dizhi = ("戌土", "申金", "午火")
        if self.flagdown:
            self.dizhi = ("辰土", "寅木", "子水")

    #返回由动爻所变化得到的三经卦序列号
    def dongyao(self,position):
        return self.yaobian.get(position)

#兑2
class Dui(object):
    def __init__(self,flagup=0,flagdown=0):
        self.name = "兑"
        self.number = 2
        self.shape = ("████  ████", "█████████", "█████████")
        self.wuxing = "金"
        self.yaobian = {(0, 0, 0): 2, (1, 0, 0): 1, (0, 1, 0): 4, (0, 0, 1): 6, (1, 1, 0): 3, (1, 0, 1): 5,
                        (0, 1, 1): 8, (1, 1, 1): 7}
        self.dizhi = ("", "", "")
        self.flagup = flagup == 2
        self.flagdown = flagdown == 2

        if self.flagup:
            self.dizhi = ("未土", "酉金", "亥水")
        if self.flagdown:
            self.dizhi = ("丑土", "卯木", "巳火")

    #返回由动爻所变化得到的三经卦序列号
    def dongyao(self,position):
        return self.yaobian.get(position)

#离3
class Li(object):
    def __init__(self,flagup=0,flagdown=0):
        self.name = "离"
        self.number = 3
        self.shape = ("█████████", "████  ████", "█████████")
        self.wuxing = "火"
        self.yaobian = {(0, 0, 0): 3, (1, 0, 0): 4, (0, 1, 0): 1, (0, 0, 1): 7, (1, 1, 0): 2, (1, 0, 1): 8,
                        (0, 1, 1): 5, (1, 1, 1): 6}
        self.dizhi = ("", "", "")
        self.flagup = flagup == 3
        self.flagdown = flagdown == 3

        if self.flagup:
            self.dizhi = ("巳火", "未土", "酉金")
        if self.flagdown:
            self.dizhi = ("亥水", "丑土", "卯木")

    # 返回由动爻所变化得到的三经卦序列号
    def dongyao(self,position):
        return self.yaobian.get(position)

#震4
class Zhen(object):
    def __init__(self,flagup=0,flagdown=0):
        self.name = "震"
        self.number = 4
        self.shape = ("████  ████", "████  ████", "█████████")
        self.wuxing = "木"
        self.yaobian = {(0, 0, 0): 4, (1, 0, 0): 3, (0, 1, 0): 2, (0, 0, 1): 8, (1, 1, 0): 1, (1, 0, 1): 7,
                        (0, 1, 1): 6, (1, 1, 1): 5}

        self.dizhi = ("", "", "")
        self.flagup = flagup == 4
        self.flagdown = flagdown == 4

        if self.flagup:
            self.dizhi = ("戌土", "申金", "午火")
        if self.flagdown:
            self.dizhi = ("辰土", "寅木", "子水")

    # 返回由动爻所变化得到的三经卦序列号
    def dongyao(self,position):
        return self.yaobian.get(position)

#巽5
class Xun(object):
    def __init__(self,flagup=0,flagdown=0):
        self.name = "巽"
        self.number = 5
        self.shape = ("█████████", "█████████", "████  ████")
        self.wuxing = "木"
        self.yaobian = {(0, 0, 0): 5, (1, 0, 0): 6, (0, 1, 0): 7, (0, 0, 1): 1, (1, 1, 0): 8, (1, 0, 1): 2,
                        (0, 1, 1): 3, (1, 1, 1): 4}

        self.dizhi = ("", "", "")
        self.flagup = flagup == 5
        self.flagdown = flagdown == 5

        if self.flagup:
            self.dizhi = ("卯木", "巳火", "未土")
        if self.flagdown:
            self.dizhi = ("酉金", "亥水", "丑土")

    # 返回由动爻所变化得到的三经卦序列号
    def dongyao(self,position):
        return self.yaobian.get(position)

#坎6
class Kan(object):
    def __init__(self,flagup=0,flagdown=0):
        self.name = "坎"
        self.number = 6
        self.shape = ("████  ████", "█████████", "████  ████")
        self.wuxing = "水"
        self.yaobian = {(0, 0, 0): 6, (1, 0, 0): 5, (0, 1, 0): 8, (0, 0, 1): 2, (1, 1, 0): 7, (1, 0, 1): 1,
                        (0, 1, 1): 4, (1, 1, 1): 3}

        self.dizhi = ("", "", "")
        self.flagup = flagup == 6
        self.flagdown = flagdown == 6

        if self.flagup:
            self.dizhi = ("子水", "戌土", "申金")
        if self.flagdown:
            self.dizhi = ("午火", "辰土", "寅木")

    # 返回由动爻所变化得到的三经卦序列号
    def dongyao(self,position):
        return self.yaobian.get(position)

#艮7
class Gen(object):
    def __init__(self,flagup=0,flagdown=0):
        self.name = "艮"
        self.number = 7
        self.shape = ("█████████", "████  ████", "████  ████")
        self.wuxing = "土"
        self.yaobian = {(0, 0, 0): 7, (1, 0, 0): 8, (0, 1, 0): 5, (0, 0, 1): 3, (1, 1, 0): 6, (1, 0, 1): 4,
                        (0, 1, 1): 1, (1, 1, 1): 2}

        self.dizhi = ("", "", "")
        self.flagup = flagup == 7
        self.flagdown = flagdown == 7

        if self.flagup:
            self.dizhi = ("寅木", "子水", "戌土")
        if self.flagdown:
            self.dizhi = ("申金", "午火", "辰土")

    # 返回由动爻所变化得到的三经卦序列号
    def dongyao(self,position):
        return self.yaobian.get(position)

#坤8
class Kun(object):
    def __init__(self,flagup=0,flagdown=0):
        self.name = "坤"
        self.number = 8
        self.shape = ("████  ████", "████  ████", "████  ████")
        self.wuxing = "土"
        self.yaobian = {(0, 0, 0): 8, (1, 0, 0): 7, (0, 1, 0): 6, (0, 0, 1): 4, (1, 1, 0): 5, (1, 0, 1): 3,
                        (0, 1, 1): 2, (1, 1, 1): 1}

        self.dizhi = ("", "", "")
        self.flagup = flagup == 8
        self.flagdown = flagdown == 8

        if self.flagup:
            self.dizhi = ("酉金", "亥水", "丑土")
        if self.flagdown:
            self.dizhi = ("卯木", "巳火", "未土")

    # 返回由动爻所变化得到的三经卦序列号
    def dongyao(self, position):
        return self.yaobian.get(position)


#装干支
def BaGuaUp(flag_up):
    if flag_up == 1:
        return Qian(flag_up,0).dizhi

    if flag_up == 2:
        return Dui(flag_up,0).dizhi

    if flag_up == 3:
        return Li(flag_up,0).dizhi

    if flag_up == 4:
        return Zhen(flag_up,0).dizhi

    if flag_up == 5:
        return Xun(flag_up,0).dizhi

    if flag_up == 6:
        return Kan(flag_up,0).dizhi

    if flag_up == 7:
        return Gen(flag_up,0).dizhi

    if flag_up == 8:
        return Kun(flag_up,0).dizhi

def BaGuaDown(flag_down):
    if flag_down == 1:
        return Qian(0,flag_down).dizhi

    if flag_down == 2:
        return Dui(0,flag_down).dizhi

    if flag_down == 3:
        return Li(0,flag_down).dizhi

    if flag_down == 4:
        return Zhen(0,flag_down).dizhi

    if flag_down == 5:
        return Xun(0,flag_down).dizhi

    if flag_down == 6:
        return Kan(0,flag_down).dizhi

    if flag_down == 7:
        return Gen(0,flag_down).dizhi

    if flag_down == 8:
        return Kun(0,flag_down).dizhi

#三经卦
sanjinggua = ("","乾", "兑", "离", "震", "巽", "坎", "艮", "坤")
#sanjinggua_Represent = ("", "天", "泽", "火", "雷", "风", "水", "山", "地")
#先天八卦之数
Bagua_Dict = {1:Qian(), 2:Dui(), 3:Li(), 4:Zhen(), 5:Xun(), 6:Kan(), 7:Gen(), 8:Kun()}
#五行相生相克
wuxing_Ke = {"金":"木", "木":"土", "土":"水", "水":"火", "火":"金"}
wuxing_Sheng = {"金":"水", "水":"木", "木":"火", "火":"土", "土":"金"}