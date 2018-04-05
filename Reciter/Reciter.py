#!/usr/bin/env python
#-*- coding: utf-8 -*-

#系统及第三方包
import os#不添加这个将无法正常打包
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox

#编写的包
import tooltips as tt
import shuishou as ss

class OOP(object):
    
    def __init__(self,num):
        self.num = num
        #Create instance
        self.win = tk.Tk()
        #self.win.iconbitmap(default= r'.\arose.ico')
        #Add a title
        self.win.title("瞎背吧")
        #self.win.geometry("640x640")
        self.createWidgets()
        
    #Modified Button Click Function
    def clickMe(self):
        self.numberChosen2["values"] = ss.stage2nd(self.number1.get())

    def _radCall(self):
        self.radtemp = ss.stage2ndint(self.radVar1.get())
        #for seqs in range(1):
        #    tk.Radiobutton(self.monty2, text='', variable=self.radVar2, value=seqs).grid(column=1,row=seqs+1,sticky="W")        
        for seqs in range(len(self.radtemp)):
            tk.Radiobutton(self.monty2, text=self.radtemp[seqs], variable=self.radVar2, value=seqs,activebackground='yellow').grid(column=1,row=seqs+1,sticky=tk.W)
            
            
    def _monCall(self):
        self.montemp = ss.money2ndint(self.monVar1.get())
        self.numberChosen2["values"] = self.montemp

    def checkMon(self):
        self.num += 1
        if self.num == 40:
            self._finalcaidan()
        if self.num == 9:
            self._remindbox()
        ss.money3rd(self.labelsFrame3,self.monVar2.get())

    def checkThem(self):
        self.num += 1
        if self.num%2000 == 40:
            self._finalcaidan()
        if self.num == 9:
            self._remindbox()            
        ss.stage3rd(self.labelsFrame2,self.radtemp[self.radVar2.get()])
        
    def _msgBox(self):
        mBox.showinfo('<翠玉钥匙>','这是第2个彩蛋：\n这个小程序是我做的第一个……做来练手的……\n泉眼无声惜细流，树阴照水    晴柔。\n小荷才露尖尖角，早有蜻蜓立上头。\n\n')
        
    def _quitBox(self):
        answer = mBox.askyesno("退出窗口","真的想要退出吗？")
        if answer == True:
            self.win.quit()
    
    def _caidanbox(self):
        mBox.showinfo("<黄铜钥匙>","这是第1个彩蛋，你点了它什么也不会发生\n    见青山多妩媚\n\n")

    def _finalcaidan(self):        
        mBox.showinfo("<水晶钥匙>","这是第3个彩蛋                                                                \n\n何为孤寂？\n\n清风，艳日，无笑意。\n\n可否具体?\n\n左拥，右抱，无情欲。\n\n可否再具体？\n\n不得    。\n\n")
    
    def _remindbox(self):
        mBox.showinfo("彩蛋","这个软件有三个彩蛋，找到了记得给作者发个消息~")
    
    #创建框架--------------------------------------------------------------
    def createWidgets(self):
    
        #Tab Control------------------------------------------------------- 
        tabControl = ttk.Notebook(self.win)

        #self.tab1 = ttk.Frame(tabControl)
        #tabControl.add(self.tab1,text="查询")
    
        self.tab2 = tk.Frame(tabControl)
        tabControl.add(self.tab2,text="各种税的计算")
        
        self.tab3 = tk.Frame(tabControl)
        tabControl.add(self.tab3,text="应纳税额计算")
        
        tabControl.pack(expand=1,fill="both")
        #~Tab Control-------------------------------------------------------
    
        #Container frame to hold all other widgets--------------------------
        #self.monty1 = ttk.LabelFrame(self.tab1,text="税收计算公式选择")
        #self.monty1.grid(column=0,row=0,padx=16,pady=8)
    
        self.monty2 = ttk.LabelFrame(self.tab2,text="税收计算公式")
        self.monty2.grid(column=0,row=0,padx=8,pady=8)       

        self.monty3 = ttk.LabelFrame(self.tab3,text="应纳税额计算")
        self.monty3.grid(column=0,row=0,padx=8,pady=8)
        
        '''
        
        #Tab 1 中的内容
        
        #Creating a Combobox
        ttk.Label(self.monty1,text="税收大类").grid(column=0,row=0,sticky="W")
        self.number1 = tk.StringVar()
        self.numberChosen1 = ttk.Combobox(self.monty1,textvariable=self.number1,width=12)
        self.numberChosen1["values"] = ss.taxSorts()
        self.numberChosen1.grid(column=0,row=1,sticky="W")
        self.numberChosen1.current(0)
        
        ttk.Label(self.monty1,text="税收小类").grid(column=1,row=0,sticky="W")
        self.number2 = tk.StringVar()
        self.numberChosen2 = ttk.Combobox(self.monty1,textvariable=self.number2,width=12)
        self.numberChosen2["values"] = ('','')
        self.numberChosen2.grid(column=1,row=1,sticky="W")
        #self.numberChosen2.current(0)
        

        #Adding a Button
        self.action1 = ttk.Button(self.monty1,text="选择何种税收",command=self.clickMe,width=14)
        self.action1.grid(column=0,row=2,sticky="W")
        
        self.action2 = ttk.Button(self.monty1,text="查询公式",command=self.checkThem,width=14)
        self.action2.grid(column=1,row=2,sticky="W")
        
        #Create a container to hold labels
        self.labelsFrame = ttk.LabelFrame(self.monty1,text="税收计算公式如下：",style="Red.TLabelframe")
        self.labelsFrame.grid(column=0,row=8,sticky="NSWE",columnspan=12)
        
        ttk.Label(self.labelsFrame,text="").grid(column=0,row=0)
        ttk.Label(self.labelsFrame,text="").grid(column=0,row=1)
        ttk.Label(self.labelsFrame,text="").grid(column=0,row=2)
        ttk.Label(self.labelsFrame,text="").grid(column=0,row=3)
        
        #Adding A Textbox Entry widgets--------------------------
        #self.name = tk.StringVar()
        #self.nameEntered = ttk.Entry(self.monty1,width=12,textvariable=self.name)
        #self.nameEntered.grid(column=0,row=1,sticky="W")
        '''
        '''
        '''
        #Tab 2 中的内容
        
        self.label2_1 = ttk.Label(self.monty2,text="第一级",foreground='red')
        self.label2_1.grid(column=0,row=0,sticky="W")
        self.label2_2 = ttk.Label(self.monty2,text="第二级",foreground='red')
        self.label2_2.grid(column=1,row=0,sticky="W")
        
        #Radiobuttons
        self.radVar1 = tk.IntVar() 
        for seq in range(6):
            tk.Radiobutton(self.monty2, text=ss.taxsorts[seq], variable=self.radVar1, value=seq, command=self._radCall,activebackground='yellow').grid(column=0,row=seq+1,sticky=tk.W)
        
        self.radVar2 = tk.IntVar()
        for seqs in range(5):
            tk.Radiobutton(self.monty2, text='                          ', variable=self.radVar2, value=seqs, width=14).grid(column=1,row=seqs+1,sticky="WE")
        
        #Create a Button
        self.action3 = ttk.Button(self.monty2,text="查询公式",command=self.checkThem,width=8)
        self.action3.grid(column=5,row=3,sticky="W")       
        
        #Create a container to hold labels
        self.labelsFrame2 = tk.LabelFrame(self.monty2,text="税收计算公式如下：",relief=tk.SUNKEN)
        self.labelsFrame2.grid(column=0,row=8,sticky="WENS",columnspan=12)
        
        for counter in range(8):
            tk.Label(self.labelsFrame2,text="                                                                                      ",width=160,height=2).grid(column=0,row=counter,sticky="WE")

        for child in self.labelsFrame2.winfo_children():
            child.grid_configure(padx=8, pady=4)
        
        
        '''
        self.rad1 = tk.Radiobutton(self.monty2, text=ss.taxsorts[0], variable=self.radVar, value=0, command=self._radCall) 
        self.rad1.grid(column=0, row=1, sticky=tk.W) 
        '''
        
        
        #Tab 3 中的内容
        self.label3_1 = ttk.Label(self.monty3,text="第一级",foreground='red')
        self.label3_1.grid(column=0,row=0,sticky="W")
        self.label3_2 = ttk.Label(self.monty3,text="第二级",foreground='red')
        self.label3_2.grid(column=1,row=0,sticky="W")
        
        self.monVar1 = tk.IntVar()

        for ses in range(len(ss.taxmoney)):
            tk.Radiobutton(self.monty3, text=ss.taxmoney[ses], variable=self.monVar1, value=ses, command=self._monCall,activebackground='yellow').grid(column=0,row=ses+1,sticky=tk.W)
        
        self.monVar2 = tk.StringVar()
        self.numberChosen2 = ttk.Combobox(self.monty3,textvariable=self.monVar2,width=24)
        self.numberChosen2["values"] = ("","")
        self.numberChosen2.grid(column=1,row=1,sticky="W")
        #self.numberChosen2.current(0)
        
        #Create a Button
        self.action4 = ttk.Button(self.monty3,text="查询公式",command=self.checkMon,width=8)
        self.action4.grid(column=1,row=3,sticky="W")
        
        
        
        #Create a container to hold labels
        self.labelsFrame3 = tk.LabelFrame(self.monty3,text="税收计算公式如下：",relief=tk.SUNKEN)
        self.labelsFrame3.grid(column=0,sticky="WENS",columnspan=12)
        
        for counter in range(20):
            tk.Label(self.labelsFrame3,text="                                                                                                                                                                                                                                                                                                                  ",width=160).grid(column=0,row=counter,sticky="WE")

               
        #创建菜单---------------------------------------------------------
        menuBar = Menu(self.win)
        self.win.config(menu=menuBar)
        
        fileMenu = Menu(menuBar,tearoff=0)
        fileMenu.add_command(label="新建一个...什么呢？",command=self._caidanbox)
        fileMenu.add_separator()
        fileMenu.add_command(label="我要退出",command=self._quitBox)
        menuBar.add_cascade(label="【都给我坐下】",menu=fileMenu)

        helpMenu = Menu(menuBar,tearoff=0)
        helpMenu.add_command(label="关于这个软件",command=self._msgBox)
        menuBar.add_cascade(label="【这是基本操作】",menu=helpMenu)
        #~创建菜单---------------------------------------------------------
    #~创建框架-------------------------------------------------------------
    
oop = OOP(0)

tt.creatToolTip(oop.label2_2,'选择了第二级的内容后再点<查询公式>')
tt.creatToolTip(oop.label3_2,'选择了第二级的内容后再点<查询公式>')
tt.creatToolTip(oop.label2_1,'先选择第一级内容，再选择第二级的内容')
tt.creatToolTip(oop.label3_1,'先选择第一级内容，再选择第二级的内容')

oop.win.mainloop()  

#os.system("")