#!/usr/bin/env python
#-*- coding: utf-8 -*-


import SanJingGua as SJG

#字典：六亲定义
liuqin_Dict = {0:"兄", 1:"父", 2:"官", 3:"子", 4:"财"}
'''
#第一个属性为“我”
#同我者兄弟
tongwo = {("金","金"):0, ("木","木"):0, ("水","水"):0, ("火","火"):0, ("土","土"):0}
#生我者父母
shengwo = {("金","土"):1, ("木","水"):1, ("水","金"):1, ("火","木"):1, ("土","火"):1}
#克我者官鬼
kewo = {("金","火"):2, ("木","金"):2, ("水","土"):2, ("火","水"):2, ("土","木"):2}
#我生者子孙
wosheng = {("金","水"):3, ("木","火"):3, ("水","木"):3, ("火","土"):3, ("土","金"):3}
#我克者妻财
woke = {("金","木"):4, ("木","土"):4, ("水","火"):4, ("火","金"):4, ("土","水"):4}
'''
#字典：六亲歌诀
anliuqin_Dict = {("金","金"):0, ("木","木"):0, ("水","水"):0, ("火","火"):0, ("土","土"):0,
                 ("金","土"):1, ("木","水"):1, ("水","金"):1, ("火","木"):1, ("土","火"):1,
                 ("金","火"):2, ("木","金"):2, ("水","土"):2, ("火","水"):2, ("土","木"):2,
                 ("金","水"):3, ("木","火"):3, ("水","木"):3, ("火","土"):3, ("土","金"):3,
                 ("金","木"):4, ("木","土"):4, ("水","火"):4, ("火","金"):4, ("土","水"):4}

liushisi_Gua = {(1,1):"乾为天", (2,1):"泽天夬", (3,1):"火天大有", (4,1):"雷天大壮", (5,1):"风天小畜", (6,1):"水天需", (7,1):"山天大畜", (8,1):"地天泰",
                (1,2):"天泽履", (2,2):"兑为泽", (3,2):"火泽睽", (4,2):"雷泽归妹", (5,2):"风泽中孚", (6,2):"水泽节", (7,2):"山泽损", (8,2):"地泽临",
                (1,3):"天火同人", (2,3):"泽火革", (3,3):"离为火", (4,3):"雷火丰", (5,3):"风火家人", (6,3):"水火既济", (7,3):"山火贲", (8,3):"地火明夷",
                (1,4):"天雷无妄", (2,4):"泽雷随", (3,4):"火雷噬嗑", (4,4):"震为雷", (5,4):"风雷益", (6,4):"水雷屯", (7,4):"山雷颐", (8,4):"地雷复",
                (1,5):"天风姤", (2,5):"泽风大过", (3,5):"火风鼎", (4,5):"雷风恒", (5,5):"巽为风", (6,5):"水风井", (7,5):"山风蛊", (8,5):"地风升",
                (1,6):"天水讼", (2,6):"泽水困", (3,6):"火水未济", (4,6):"雷水解", (5,6):"风水涣", (6,6):"坎为水", (7,6):"山水蒙", (8,6):"地水师",
                (1,7):"天山遁", (2,7):"泽山咸", (3,7):"火山旅", (4,7):"雷山小过", (5,7):"风山渐", (6,7):"水山蹇", (7,7):"艮为山", (8,7):"地山谦",
                (1,8):"天地否", (2,8):"泽地萃", (3,8):"火地晋", (4,8):"雷地豫", (5,8):"风地观", (6,8):"水地比", (7,8):"山地剥", (8,8):"坤为地"}

yaoPosition = ("","初爻", "二爻", "三爻", "四爻", "五爻", "六爻")
#字典：取用神
#To do:
    #后续加入("金","金"):0, ("木","木"):0, ("水","水"):0, ("火","火"):0, ("土","土"):0,用于只能定用神

quyongshen_Dict = {("金","土"):1, ("木","水"):1, ("水","金"):1, ("火","木"):1, ("土","火"):1,
                 ("金","火"):2, ("木","金"):2, ("水","土"):2, ("火","水"):2, ("土","木"):2,}
yongshen = {1:"原神", 2:"忌神", None:"    "}

#定世应歌诀
def ShiYing_KouJue(shape1,shape2):
    #八纯世在上
    if shape1 == shape2:
        shi = 6
        ying = 3
        return shi, ying
    #地同人同四
    if ((shape1[2] == shape2[2])or(shape1[1] == shape2[1])) and (shape1[0] != shape2[0]):
        shi = 4
        ying = 1
        return shi, ying

    #地人都同五
    if (shape1[2] == shape2[2]) and (shape1[1] == shape2[1]) and (shape1[0] != shape2[0]):
        shi = 5
        ying = 2
        return shi, ying

    #错卦天地三
    if (shape1[2] != shape2[2]) and (shape1[1] != shape2[1]) and (shape1[0] != shape2[0]):
        shi = 3
        ying = 6
        return shi, ying

    if (shape1[2] == shape2[2]) and (shape1[1] != shape2[1]) and (shape1[0] == shape2[0]):
        shi = 3
        ying = 6
        return shi, ying

    #天二天人初
    if (shape1[2] != shape2[2]) and (shape1[1] != shape2[1]) and (shape1[0] == shape2[0]):
        shi = 2
        ying = 5
        return shi, ying

    if (shape1[2] != shape2[2]) and (shape1[1] == shape2[1]) and (shape1[0] == shape2[0]):
        shi = 1
        ying = 4
        return shi, ying

#六十四卦五行歌诀
def DingWuXing(shi,flagup,flagdown,shapeup,shapedown):
    #一二错六外卦宫
    if shi == 1 or shi == 2 or shi == 6:
        return SJG.Bagua_Dict.get(flagup)

    if (shapeup[0] != shapedown[0]) and (shapeup[1] != shapedown[1]) and (shapeup[2] != shapedown[2]):
        return SJG.Bagua_Dict.get(flagup)

    #内卦只有天地同
    if (shapeup[0] == shapedown[0]) and (shapeup[1] != shapedown[1]) and (shapeup[2] == shapedown[2]):
        return SJG.Bagua_Dict.get(flagdown)

    #四五内错是寻宫
    if shi == 4 or shi == 5:
        return SJG.Bagua_Dict.get(SJG.Bagua_Dict.get(flagdown).dongyao((1,1,1)))

#安六亲歌诀
def AnLiuQin(wuxing,baguaUp,baguaDown):
    baguaUp_wuxing = []
    baguaDown_wuxing = []
    liushisiGua = [0, 0, 0, 0, 0, 0]
    dingliuqin = [0, 0, 0, 0, 0, 0]
    #通过（所在卦宫五行，此爻五行）来判断是六亲中的哪一类
    for counters in range(3):
        baguaUp_wuxing.append(baguaUp[counters][-1])#1:
        liushisiGua[counters] = baguaUp_wuxing[counters]
    for counters in range(3):
        baguaDown_wuxing.append(baguaDown[counters][-1])#1:
        liushisiGua[counters+3] = baguaDown_wuxing[counters]

    #安六亲
    for counters in range(6):
        temp_64 = anliuqin_Dict.get((wuxing,liushisiGua[counters]))
        temp_liuqin = liuqin_Dict.get(temp_64)
        dingliuqin[counters] = temp_liuqin

    return dingliuqin


#定世应+安六亲
def ShiYing_DingWuXing(flagup,flagdown,baguaUp,baguaDown):
    tempup = SJG.Bagua_Dict.get(flagup)
    tempdown = SJG.Bagua_Dict.get(flagdown)

    shi_1, ying_1 = ShiYing_KouJue(tempup.shape,tempdown.shape)
    benguagong = DingWuXing(shi_1,flagup,flagdown,tempup.shape,tempdown.shape)
    wuxing = benguagong.wuxing
    liuqin = AnLiuQin(wuxing,baguaUp,baguaDown)
    return shi_1,ying_1,wuxing,liuqin,benguagong

#取用神
def QuYongShen(dizhi,yongPositionUp):
    found = ["", "", "", "", "", ""]

    #初始爻位置判定
    if yongPositionUp == 0:
        return found

    #定用神五行
    wuxing_dizhi = [0, 0, 0, 0, 0, 0]
    for counters in range(6):
        wuxing_dizhi[counters] = dizhi[counters][1:]
    wuxing = wuxing_dizhi[6 - yongPositionUp]

    #找用神原神忌神
    find = [3, 3, 3, 3, 3, 3]
    for counters in range(6):
        find[counters] = quyongshen_Dict.get((wuxing,wuxing_dizhi[counters]))
        found[counters] = yongshen.get(find[counters])
    found[6 - yongPositionUp] = "用神"

    return found