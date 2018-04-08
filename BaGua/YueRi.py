#!/usr/bin/env python
#-*- coding: utf-8 -*-


#逐日六神表
liushenBiao = {"甲": 0, "乙": 0, "丙": 1, "丁": 1, "戊": 2, "己": 3, "庚": 4, "辛": 4, "壬": 5, "葵": 5}
zhuriJiaYi = ("青龙", "朱雀", "勾陈", "腾蛇", "白虎", "玄武")

#天干
TianGan_Number = {"甲": 1, "乙": 2, "丙": 3, "丁": 4, "戊": 5, "己": 6, "庚": 7, "辛": 8, "壬": 9, "葵": 10}
TianGan_Tuple = ("甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "葵")

#地支
DiZhi_Number = {"子": 1, "丑": 2, "寅": 3, "卯": 4, "辰": 5, "巳": 6, "午": 7, "未": 8, "申": 9, "酉": 10,  "戌": 11,  "亥": 12}
DiZhi_Tuple = ("子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥")
#地支五行
DiZhi_Wuxing = {"子": "水", "丑": "土", "寅": "木", "卯": "木", "辰": "土", "巳": "火",
                "午": "火", "未": "土", "申": "金", "酉": "金",  "戌": "土",  "亥": "水"}
#地支相冲
Dizhi_Chong = {"子": "午", "丑": "未", "寅": "申", "卯": "酉", "辰": "戌", "巳": "亥",
               "午": "子", "未": "丑", "申": "寅", "酉": "卯",  "戌": "辰",  "亥": "巳"}
#地支相合
Dizhi_He = {"子": "丑", "丑": "子", "寅": "亥", "卯": "戌", "辰": "酉", "巳": "申",
            "午": "未", "未": "午", "申": "巳", "酉": "辰",  "戌": "卯",  "亥": "寅"}

#长生十二掌诀



#六神定位
def ZhuRiLiuShen(richen):
    changeYao = liushenBiao.get(richen[:1])
    liushenPosition = [0, 0, 0, 0, 0, 0]
    for counters in range(6):
        liushenPosition[5 - counters] = zhuriJiaYi[(counters + changeYao)%6]

    return liushenPosition

#月建月破与日建空亡
def YueRiWuXing(yuefen,richen):
    #月建日建
    yuejian = DiZhi_Wuxing.get(yuefen[0:1])
    yuepo = Dizhi_Chong.get(yuefen[0:1])
    rijian = DiZhi_Wuxing.get(richen[1:])
    ripo = Dizhi_Chong.get(richen[1:])
    #空亡日
    kw_dizhi = DiZhi_Number.get(richen[1:])
    kw_tiangan = TianGan_Number.get(richen[0:1])
    kongwangri = [DiZhi_Tuple[(10 - kw_tiangan + kw_dizhi) % 12],
                  DiZhi_Tuple[(11 - kw_tiangan + kw_dizhi) % 12]]

    liushenPosition = ZhuRiLiuShen(richen)

    return (yuejian, yuepo), (rijian, ripo), kongwangri, liushenPosition