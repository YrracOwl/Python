#!/usr/bin/env python
#-*- coding: utf-8 -*-

#系统及第三方包
import os
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

#编写的包
import tooltips as tt
import SanJingGua as SJG
import LiuShiSiGua as LSSG
import YueRi as YR
import  OutToLableFrame as OTLF
import  SearchForAnswer as SFA

class Win(object):

    def __init__(self):
        self.top = tk.Tk()
        self.top.title("八卦")

        # 判断装卦与定用神的先后顺序
        self.flag = 0
        '''
        #动爻的变化不会导致用神原神忌神列的清空
        self.temp_up_a = (0, 0, 0)
        self.temp_up_b = (0, 0, 0)
        self.temp_down_a = (0, 0, 0)
        self.temp_down_b = (0, 0, 0)
        self.flag_out = 0
        '''
        self.createWidgets()

    def m_radCall_up(self):
        pass

    def m_radCall_down(self):
        pass

    def m_radCall_yongshen(self):
        pass

#装卦按钮
    def m_butCall_t1(self):
        data = self.detectData()
        if isinstance(data,str):
            self._errorBox(data)
            return
        elif (self.radVar1.get() != 0)and(self.radVar2.get() != 0)and(isinstance(self.name_t1_1.get(),str))and(isinstance(self.name_t1_2.get(),str)):
            #动爻位置
            activeYaoUp = (self.shangyao.get(),self.wuyao.get(),self.siyao.get())
            activeYaoDown = (self.sanyao.get(),self.eryao.get(),self.chuyao.get())
            #卦象干支
            self.activeGanZhi = [0, 0, 0, 0, 0, 0]
            for counters in range(3):
                self.activeGanZhi[counters] = SJG.BaGuaUp(self.radVar1.get())[counters]
            for counters in range(3):
                self.activeGanZhi[counters + 3] = SJG.BaGuaDown(self.radVar2.get())[counters]
            #卦象世应， 64卦五行， 安六亲, 卦所在宫
            shi, ying, gua64wuxing, liuqin, benguagong = LSSG.ShiYing_DingWuXing(self.radVar1.get(),self.radVar2.get(),
                                                               SJG.BaGuaUp(self.radVar1.get()),SJG.BaGuaDown(self.radVar2.get()))
            #月建月破， 日建日破， 空亡日， 六神
            yuexiang, rixiang, kongwangri, liushenPosition = YR.YueRiWuXing(self.name_t1_1.get(),self.name_t1_2.get())
            #上卦下卦形状
            guaup = SJG.Bagua_Dict.get(self.radVar1.get())
            guadown = SJG.Bagua_Dict.get(self.radVar2.get())

            #月名字及日辰名字
            yueming = self.name_t1_1.get()[1:]
            riming = self.name_t1_2.get()[1:]

            #用神位置
            YongShenPosition = LSSG.QuYongShen(self.activeGanZhi, self.radVar3.get())

            #输出到界面显示
            '''
            self.temp_up_a = activeYaoUp
            self.temp_down_a = activeYaoDown
            if (self.temp_up_a != self.temp_up_b)or(self.temp_down_a != self.temp_down_b):
                self.flag_out = 1
            else:
                self.flag_out = 0
            self.temp_up_b = activeYaoUp
            self.temp_down_b = activeYaoDown
            '''

            OTLF.output_1(self.labelframe_t1_1, self.activeGanZhi, shi, liuqin, activeYaoUp, activeYaoDown, liushenPosition,guaup, guadown, YongShenPosition, self.flag, self.scr_t1_1, gua64wuxing)
            OTLF.output_2(self.labelframe_t1_2, yuexiang, rixiang, kongwangri, gua64wuxing, benguagong, yueming, riming)
            OTLF.output_5(self.labelframe_t1_1, self.radVar1.get(), self.radVar2.get())

            self.flag = 1

#取用神按钮
    def m_butCall_t2(self):
        if self.flag == 0:
            self._errorBox_QYS()
        elif self.flag == 1:
            YongShenPosition = LSSG.QuYongShen(self.activeGanZhi,self.radVar3.get())
            OTLF.output_3(self.labelframe_t1_1,YongShenPosition)

#查询取象按钮
    def m_butCall_t3(self):
        temp = SFA.searchEverything(self.name_t2_1.get())
        #输出到tab 2 中的文本框
        OTLF.output_t2_1(self.scr_t2_1,temp)

#卦象查询按钮
    def m_butCall_t4(self):
        temp = SFA.search64Gua(self.name_t2_2.get())
        OTLF.output_t2_2(self.scr_t2_2, temp)

# message boxes
    def _msgBox(self):
        mBox.showinfo('关于作者', "Author: 小萌新。\nTime::2018/04/05")

    def _quitBox(self):
        answer = mBox.askyesno("退出窗口", "真的想要退出吗？")
        if answer == True:
            self.top.quit()

    def _errorBox(self,data):
        mBox.showerror('输入参数错误', '请输入正确的' + data)

    def _errorBox_riyue(self):
        mBox.showerror('输入参数错误', '请输入正确格式的月份日辰，如：辰月、丙辰日')

    def _errorBox_QYS(self):
        mBox.showerror('输入参数错误', '请  先  装  卦！')

#监测输入数据是否正常
    def detectData(self):
        if self.radVar1.get() == 0:
            return "  < 卦  象 >"
        if self.radVar2.get() == 0:
            return "  < 卦  象 >"
        if self.name_t1_1.get() == '<待输入>':
            return "  < 月  份 >"
        if self.name_t1_2.get() == '<待输入>':
            return "  < 日  辰 >"
        if len(self.name_t1_1.get()) != 1:
            return "月份格式，如：辰月"
        if len(self.name_t1_2.get()) != 2:
            return "日辰格式，如：丙辰日"


    #创建整个框架
    def createWidgets(self):

#创建Tab页面
        tabControl = ttk.Notebook()

        self.tab1 = tk.Frame(tabControl)
        tabControl.add(self.tab1, text="六爻预测")

        self.tab2 = tk.Frame(tabControl)
        tabControl.add(self.tab2, text="寻    卦")

        self.tab3 = tk.Frame(tabControl)
        tabControl.add(self.tab3, text="待    定")

        tabControl.pack(expand=1, fill="both")

        #创建Tab 1 页面中的下一层框架
        self.monty_t1_1 = ttk.LabelFrame(self.tab1, text="本卦外卦")
        self.monty_t1_1.grid(column=0, row=0, padx=8, pady=4, sticky="WN")

        self.monty_t1_2 = ttk.LabelFrame(self.tab1, text="本卦内卦")
        self.monty_t1_2.grid(column=0, row=2, padx=8, pady=4, sticky="WN")

        self.monty_t1_3 = tk.LabelFrame(self.tab1, text="断    卦", bd=3, fg="blue")
        self.monty_t1_3.grid(column=0, row=4, padx=8, pady=4, sticky="WN")

        self.monty_t1_4 = ttk.LabelFrame(self.tab1, text="起卦日期：月份&&日辰")
        self.monty_t1_4.grid(column=9, row=2, padx=8, pady=4, sticky="WN")

        self.monty_t1_5 = ttk.LabelFrame(self.tab1, text="动爻位置")
        self.monty_t1_5.grid(column=9, row=0, padx=8, pady=4, sticky="WN")

        self.monty_t1_6 = tk.LabelFrame(self.tab1, text="所  求  何  事", bd=3, fg="blue")
        self.monty_t1_6.grid(column=9, row=4, padx=8, pady=4, sticky="WN")

        self.monty_t1_7 = ttk.LabelFrame(self.tab1, text="装  卦  结  果")
        self.monty_t1_7.grid(column=0, row=6, padx=8, pady=4, sticky="WNE")

        self.monty_t1_8 = ttk.LabelFrame(self.tab1, text="月  份  日  辰")
        self.monty_t1_8.grid(column=9, row=6, padx=8, pady=4, sticky="WNE")

        # 创建Tab 2 页面中的下一层框架
        self.monty_t2_1 = ttk.LabelFrame(self.tab2, text="万物取象查询：")
        self.monty_t2_1.grid(column=0, row=0, padx=8, pady=4, sticky="WN")

        self.monty_t2_2 = ttk.LabelFrame(self.tab2, text="六十四卦查询：")
        self.monty_t2_2.grid(column=0, row=2, padx=8, pady=4, sticky="WN")

        self.monty_t2_3 = ttk.LabelFrame(self.tab2, text="万 物 取 象 显 示：")
        self.monty_t2_3.grid(column=1, row=0, padx=8, pady=4, sticky="WN")

        self.monty_t2_4 = ttk.LabelFrame(self.tab2, text="卦 象 查 阅 结 果：")
        self.monty_t2_4.grid(column=1, row=2, padx=8, pady=4, sticky="WN")

#Tab 1 内容
        #创建RadioButtons
        self.radVar1 = tk.IntVar()
        for counters in range(8):
            tk.Radiobutton(self.monty_t1_1, text=SJG.sanjinggua[counters+1], variable=self.radVar1, value=counters+1,
                command=self.m_radCall_up, activebackground='yellow').grid(column=counters, row=0, sticky="W")

        self.radVar2 = tk.IntVar()
        for counters in range(8):
            tk.Radiobutton(self.monty_t1_2, text=SJG.sanjinggua[counters+1], variable=self.radVar2, value=counters+1,
                command=self.m_radCall_down, activebackground='yellow').grid(column=counters, row=0, sticky="W")

        self.radVar3 = tk.IntVar()
        for counters in range(6):
            tk.Radiobutton(self.monty_t1_6, text=LSSG.yaoPosition[counters + 1], variable=self.radVar3,
                           value=counters + 1,command=self.m_radCall_yongshen, activebackground='yellow').grid(column=counters, row=1, sticky="W")

        #创建Buttons
        self.action_t1_1 = tk.Button(self.monty_t1_6,text="装    卦",command=self.m_butCall_t1, width=6,
                                     bd=2, activeforeground="red",font=("Microsoft YaHei",12))
        self.action_t1_1.grid(column=5,row=4,sticky="W")

        self.action_t1_2 = tk.Button(self.monty_t1_6, text="定用神", command=self.m_butCall_t2, width=6,
                                     bd=2, activeforeground="red",font=("Microsoft YaHei",12))
        self.action_t1_2.grid(column=5, row=2, sticky="W")

        #创建checkButtons
        self.chuyao = tk.IntVar()
        self.check_t1_1 = tk.Checkbutton(self.monty_t1_5,text="初爻",variable=self.chuyao, activebackground='yellow')
        self.check_t1_1.deselect()
        self.check_t1_1.grid(column=1, row=0, sticky="W")

        self.eryao = tk.IntVar()
        self.check_t1_2 = tk.Checkbutton(self.monty_t1_5, text="二爻", variable=self.eryao, activebackground='yellow')
        self.check_t1_2.deselect()
        self.check_t1_2.grid(column=2, row=0, sticky="W")

        self.sanyao = tk.IntVar()
        self.check_t1_3 = tk.Checkbutton(self.monty_t1_5, text="三爻", variable=self.sanyao, activebackground='yellow')
        self.check_t1_3.deselect()
        self.check_t1_3.grid(column=3, row=0, sticky="W")

        self.siyao = tk.IntVar()
        self.check_t1_4 = tk.Checkbutton(self.monty_t1_5, text="四爻", variable=self.siyao, activebackground='yellow')
        self.check_t1_4.deselect()
        self.check_t1_4.grid(column=4, row=0, sticky="W")

        self.wuyao = tk.IntVar()
        self.check_t1_5 = tk.Checkbutton(self.monty_t1_5, text="五爻", variable=self.wuyao, activebackground='yellow')
        self.check_t1_5.deselect()
        self.check_t1_5.grid(column=5, row=0, sticky="W")

        self.shangyao = tk.IntVar()
        self.check_t1_6 = tk.Checkbutton(self.monty_t1_5, text="上爻", variable=self.shangyao, activebackground='yellow')
        self.check_t1_6.deselect()
        self.check_t1_6.grid(column=6, row=0, sticky="W")

        #创建文本框
        tk.Label(self.monty_t1_4, text="夏历月份：").grid(column=0, row=0, sticky="W")
        tk.Label(self.monty_t1_4, text="夏历日辰：").grid(column=4, row=0, sticky="W")
        tk.Label(self.monty_t1_4, text="月").grid(column=2, row=0, sticky="W")
        tk.Label(self.monty_t1_4, text="日").grid(column=6, row=0, sticky="W")

        #tk.Label(self.monty_t1_6, text="所求何事：").grid(column=0, row=0, sticky="W")
        tk.Label(self.monty_t1_6, text="选取用神：", fg='RoyalBlue').grid(column=0, row=0, sticky="W")
        tk.Label(self.monty_t1_6, text="", fg='RoyalBlue').grid(column=0, row=3, sticky="W")

        self.name_t1_1 = tk.StringVar()
        self.nameEnterd_t1_1 = tk.Entry(self.monty_t1_4, width=12, textvariable=self.name_t1_1, bd=3, justify="right")
        self.nameEnterd_t1_1.insert(0,'<待输入>')
        self.nameEnterd_t1_1.grid(column=1,row=0)

        self.name_t1_2 = tk.StringVar()
        self.nameEnterd_t1_2 = tk.Entry(self.monty_t1_4, width=12, textvariable=self.name_t1_2, bd=3, justify="right")
        self.nameEnterd_t1_2.insert(0, '<待输入>')
        self.nameEnterd_t1_2.grid(column=5, row=0)

        '''
        self.name_t1_3 = tk.StringVar()
        self.nameEnterd_t1_3 = tk.Entry(self.monty_t1_6, width=21, textvariable=self.name_t1_3, bd=3, justify="right", state="disabled")
        self.nameEnterd_t1_3.grid(column=1, row=0)
        '''

        #创建scrolled text
        self.scrolW_t1_1 = 50
        self.scrolH_t1_1 = 12
        self.scr_t1_1 = scrolledtext.ScrolledText(self.monty_t1_3,width=self.scrolW_t1_1,height=self.scrolH_t1_1
                        ,wrap=tk.WORD,font = ("Mircrosoft YaHei",11), fg='red')
        self.scr_t1_1.config(state="disabled")
        self.scr_t1_1.grid(column=0,columnspan=8)

        #创建Combobox


        #创建LabelFrame
        self.labelframe_t1_1 = tk.LabelFrame(self.monty_t1_7,text='结 果 如 下：',relief=tk.SUNKEN)
        self.labelframe_t1_1.grid(column=0,row=0,sticky="WENS",columnspan=12)

        for counters in range(9):
            tk.Label(self.labelframe_t1_1,text="").grid(column=0,row=counters,sticky="WE")

        for child in self.labelframe_t1_1.winfo_children():
            child.grid_configure(padx=2,pady=2)

        self.labelframe_t1_2 = tk.LabelFrame(self.monty_t1_8, text='日月以及此卦所在宫：', relief=tk.SUNKEN)
        self.labelframe_t1_2.grid(column=0, row=0, sticky="WENS", columnspan=12)

        for counters in range(9):
            tk.Label(self.labelframe_t1_2,text="").grid(column=0,row=counters,sticky="WE")

        for child in self.labelframe_t1_2.winfo_children():
            child.grid_configure(padx=2,pady=2)

#Tab 2 内容

        #文本框的创建
        tk.Label(self.monty_t2_1, text="输入想要查询的取象").grid(column=0, row=0, sticky="W")
        self.name_t2_1 = tk.StringVar()
        self.nameEnterd_t2_1 = tk.Entry(self.monty_t2_1, width=30, textvariable=self.name_t2_1, bd=3, justify="right")
        self.nameEnterd_t2_1.insert(0, '< 例如： 圆物>')
        self.nameEnterd_t2_1.grid(column=0, row=1, sticky="W")

        tk.Label(self.monty_t2_2, text="输入想要查询的卦象").grid(column=0, row=0, sticky="W")
        self.name_t2_2 = tk.StringVar()
        self.nameEnterd_t2_2 = tk.Entry(self.monty_t2_2, width=30, textvariable=self.name_t2_2, bd=3, justify="right")
        self.nameEnterd_t2_2.insert(0, '< 例如： 水火既济 >')
        self.nameEnterd_t2_2.grid(column=0, row=1, sticky="W")

        #按钮的创建
        self.action_t2_1 = tk.Button(self.monty_t2_1,text="查询取象",command=self.m_butCall_t3, width=8,
                                     bd=2, activeforeground="red",font=("Microsoft YaHei",12))
        self.action_t2_1.grid(column=0,row=2,sticky="E")

        self.action_t2_2 = tk.Button(self.monty_t2_2,text="卦象查阅",command=self.m_butCall_t4, width=8,
                                     bd=2, activeforeground="red",font=("Microsoft YaHei",12))
        self.action_t2_2.grid(column=0,row=2,sticky="E")

        #创建ScrolledText
        self.scrolW_t2_1 = 64
        self.scrolH_t2_1 = 5
        self.scr_t2_1 = scrolledtext.ScrolledText(self.monty_t2_3,width=self.scrolW_t2_1,height=self.scrolH_t2_1
                        ,wrap=tk.WORD,font = ("Mircrosoft YaHei",12), fg='black')
        self.scr_t2_1.config(state="disabled")
        self.scr_t2_1.grid(column=0,columnspan=8)

        self.scrolW_t2_2 = 64
        self.scrolH_t2_2 = 28
        self.scr_t2_2 = scrolledtext.ScrolledText(self.monty_t2_4,width=self.scrolW_t2_2,height=self.scrolH_t2_2
                        ,wrap=tk.WORD,font = ("Mircrosoft YaHei",12), fg='black')
        self.scr_t2_2.config(state="disabled")
        self.scr_t2_2.grid(column=0,columnspan=8)

# 创建菜单---------------------------------------------------------
        menuBar = Menu(self.top)
        self.top.config(menu=menuBar)

        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="nothing")
        fileMenu.add_separator()
        fileMenu.add_command(label="exit", command=self._quitBox)
        menuBar.add_cascade(label="Just ", menu=fileMenu)

        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="About", command=self._msgBox)
        menuBar.add_cascade(label="for Fun", menu=helpMenu)
# ~创建菜单---------------------------------------------------------



win = Win()

win.top.mainloop()