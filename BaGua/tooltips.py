#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tkinter as tk

class ToolTip(object):
    def __init__(self,widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        
    def showtip(self,text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        x,y,_cx,cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 8
        y += cy + self.widget.winfo_rooty() + 2
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d"%(x,y))
        
        lab1 = tk.Label(tw,text=self.text,justify=tk.LEFT,background="#ffffe0",relief=tk.SOLID,borderwidth=1,font=("Microsoft YaHei",10,"normal"))
        lab1.pack(ipadx=1)
        
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
            
def creatToolTip(widget,text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>',enter)
    widget.bind('<Leave>',leave)