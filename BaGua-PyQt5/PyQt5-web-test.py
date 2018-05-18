#!usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import os

from PyQt5.QtWidgets import QApplication,QWidget,QDesktopWidget

from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWebChannel import QWebChannel

from PyQt5.QtCore import QUrl,QObject,pyqtSlot,pyqtSignal

from PyQt5.QtGui import QIcon

import dataProcessor as DP


#test pyinstaller
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)

# 用于本地python与html中的js脚本交互
# str 代表有参数
# int 代表无参数
class CallHandler(QObject):
    trigger = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.guaXiang = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.shiying = 0
        self.guaup = 0
        self.guadown = 0
        self.liuqin = 0
        self.activeGanZhi = 0
        self.gua64wuxing = 0
        self.guaBian = 0
        self.liushenPosition = 0
        self.guaGongUp = 0
        self.guaGongDown = 0
        self.liuqin_gong = 0
        self.ganzhi_gong = 0
        self.yuejian = 0
        self.yuepo = 0
        self.rijian = 0
        self.ripo = 0
        self.kongwangri = [0, 0]
        self.benguaName = 0
        self.zhiguaName = 0
        self.month = 0
        self.day = 0

        self.orignShape = 0
        self.gongShape = 0

        self.flag = "False"

#test
    @pyqtSlot()
    def test(self):
        print('test_first!')

    @pyqtSlot()
    def test_yo(self):
        print('test_second!')

#获取liuyaoyuce的数据并进行处理
    @pyqtSlot(str,result=str)
    def times_1(self,s):
        self.guaXiang[5] = s

    @pyqtSlot(str,result=str)
    def times_2(self,s):
        self.guaXiang[4] = s

    @pyqtSlot(str,result=str)
    def times_3(self,s):
        self.guaXiang[3] = s

    @pyqtSlot(str,result=str)
    def times_4(self,s):
        self.guaXiang[2] = s

    @pyqtSlot(str,result=str)
    def times_5(self,s):
        self.guaXiang[1] = s

    @pyqtSlot(str,result=str)
    def times_6(self,s):
        self.guaXiang[0] = s

    @pyqtSlot(str,result=str)
    def times_m(self,s):
        self.guaXiang[6] = s

    @pyqtSlot(str,result=str)
    def times_d(self,s):
        self.guaXiang[7] = s

    @pyqtSlot(str,result=str)
    def times_m_today(self,s):
        self.guaXiang[8] = s

    @pyqtSlot(str,result=str)
    def times_d_today(self,s):
        self.guaXiang[9] = s

    @pyqtSlot()
    def dealWithIt(self):
        self.flag, self.shiying, self.guaup, self.guadown, self.liuqin, self.activeGanZhi, self.gua64wuxing, self.guaBian, self.liushenPosition, self.guaGongUp, self.guaGongDown, self.liuqin_gong, self.ganzhi_gong, self.yuejian, self.yuepo, self.rijian, self.ripo, self.kongwangri, self.benguaName, self.zhiguaName, self.month, self.day = DP.dataProcessing(self.guaXiang)
        print(self.flag, self.shiying, self.guaup, self.guadown, self.liuqin, self.activeGanZhi, self.gua64wuxing, self.guaBian, self.liushenPosition, self.guaGongUp, self.guaGongDown, self.liuqin_gong, self.ganzhi_gong, self.yuejian, self.yuepo, self.rijian, self.ripo, self.kongwangri, self.benguaName, self.zhiguaName, self.month, self.day)

#将六爻预测的数据传入第二个网页
    @pyqtSlot(result=str)
    def grapData(self):
        return self.flag

    @pyqtSlot(result=list)
    def shiying(self):
        return self.shiying

    @pyqtSlot(result=list)
    def orignShape(self):
        self.orignShape = DP.returnShape(self.guaup, self.guadown)
        return self.orignShape

    @pyqtSlot(result=list)
    def liuqin(self):
        return self.liuqin

    @pyqtSlot(result=list)
    def activeGanZhi(self):
        return self.activeGanZhi

    @pyqtSlot(result=str)
    def gua64wuxing(self):
        return self.gua64wuxing

    @pyqtSlot(result=list)
    def guaBian(self):
        return self.guaBian

    @pyqtSlot(result=list)
    def liushenPosition(self):
        return self.liushenPosition

    @pyqtSlot(result=list)
    def guaGong(self):
        self.gongShape = DP.returnShape(self.guaGongUp, self.guaGongDown)
        return self.gongShape

    @pyqtSlot(result=list)
    def liuqinGong(self):
        return self.liuqin_gong

    @pyqtSlot(result=list)
    def ganzhiGong(self):
        return self.ganzhi_gong

    @pyqtSlot(result=str)
    def riyue(self):
        str_list = ["月建：",self.yuejian,"， 月破：",self.yuepo,"， 日建：",self.rijian,"， 日破：",self.ripo,"， 空亡日：",self.kongwangri[0],self.kongwangri[1]]
        a = ''
        return a.join(str_list)

    @pyqtSlot(result=str)
    def guaName(self):
        str_list = ["本卦名：",self.benguaName, "， 卦宫名：", self.zhiguaName]
        a = ''
        return a.join(str_list)

    @pyqtSlot(result=str)
    def month_day(self):
        str_list = ["月份：", self.month, "， 日辰：", self.day]
        a = ''
        return a.join(str_list)



class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.win_width = 1080
        self.win_height = 720
        self.setWindowIcon(QIcon(resource_path('YinYang.ico')))
        self.initUI()


    def initUI(self):
        size_init = QDesktopWidget().screenGeometry(-1)
        self.view = QWebEngineView()
        self.view.setGeometry(size_init.width()/2-self.win_width/2, size_init.height()/2-self.win_height/2,self.win_width, self.win_height)
        self.view.setFixedSize(self.win_width, self.win_height)
        self.view.setWindowTitle("阴阳两界说余梦")
        self.view.load(QUrl().fromLocalFile(resource_path('cover.html')))



        # 用于本地python与html中的js脚本交互
        self.channel = QWebChannel()
        self.handler = CallHandler()

        self.channel.registerObject('handler',self.handler)
        self.view.page().setWebChannel(self.channel)

        self.view.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Win()
    sys.exit(app.exec_())
