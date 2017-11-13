#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:14:31 2017

@author: abhilashsk
"""

from tkinter import *
from first import *
import datetime
class Application(Frame):
    
    """ GUI application """

    def __init__(self, master):
        """ Initialize the frame. """
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()
        self.dataset=readData()
        #self.dataset=cleanData(self.dataset)
        
    def create_widgets(self):
        Label(self,text="Please enter the data.",width=30).grid(row=0,column=0,sticky=W)
        Label(self,text="   ",width=25).grid(row=0,column=1,sticky=W)
        Label(self,text="   ",width=25).grid(row=0,column=2,sticky=W)
        Label(self,text="   ",width=25).grid(row=0,column=3,sticky=W)
        Label(self,text="   ",width=25).grid(row=0,column=4,sticky=W)
        
        Label(self,text="From (YYYY-MM-DD) :").grid(row=1,column=0,sticky=W)
        self.frm=Entry(self)
        self.frm.grid(row=1,column=1,sticky=W)
        
        Label(self,text="To (YYYY-MM-DD) :").grid(row=2,column=0,sticky=W)
        self.to=Entry(self)
        self.to.grid(row=2,column=1,sticky=W)
        
        Label(self,text="Select Columns: ").grid(row=3,column=0,sticky=W)
        self.operator=BooleanVar()
        Checkbutton(self,text="OPERATOR",variable=self.operator).grid(row=3,column=1,sticky=W)
        self.route=BooleanVar()
        Checkbutton(self,text="ROUTE",variable=self.route).grid(row=3,column=3,sticky=W)
        self.flight=BooleanVar()
        Checkbutton(self,text="FLIGHT",variable=self.flight).grid(row=3,column=2,sticky=W)
        self.regis=BooleanVar()
        Checkbutton(self,text="REGISTRATION",variable=self.regis).grid(row=4,column=1,sticky=W)
        self.aboard=BooleanVar()
        Checkbutton(self,text="ABOARD",variable=self.aboard).grid(row=4,column=2,sticky=W)
        self.fatal=BooleanVar()
        Checkbutton(self,text="FATALITIES",variable=self.fatal).grid(row=4,column=3,sticky=W)
        
        Label(self,text="Start Index:").grid(row=5,column=0,sticky=W)
        self.rowStart=Entry(self)
        self.rowStart.grid(row=5,column=1,sticky=W)
        Label(self,text="End Index:").grid(row=5,column=2,sticky=W)
        self.rowEnd=Entry(self)
        self.rowEnd.grid(row=5,column=3,sticky=W)
        
        self.btn=Button(self,text="SUBMIT",command=self.test)
        self.btn.grid(row=6,column=2,columnspan=2,sticky=W)
        
    def test(self):
        msg={}
        col=0
        r=7
        change=0
        if self.frm.get() and self.frm.get():
            frm=datetime.datetime.strptime(str(self.frm.get()), "%Y-%m-%d").date()
            to=datetime.datetime.strptime(str(self.to.get()), "%Y-%m-%d").date()
        rowStart=int(self.rowStart.get())
        rowEnd=int(self.rowEnd.get())
        
        if self.operator.get():
            msg['OPERATOR']=self.dataset['Operator'].iloc[rowStart:rowEnd].to_string(index=False)
        if self.route.get():
            msg['ROUTE']=self.dataset['Route'].iloc[rowStart:rowEnd].to_string(index=False)
        if self.flight.get():
            msg['FLIGHT NUMBER']=self.dataset['Flight #'].iloc[rowStart:rowEnd].to_string(index=False)
        if self.regis.get():
            msg['REGISTRATION']=self.dataset['Registration'].iloc[rowStart:rowEnd].to_string(index=False)
        if self.aboard.get():
            msg['ABOARD']=self.dataset['Aboard'].iloc[rowStart:rowEnd].to_string(index=False)
        if self.fatal.get():
            msg['FATALITIES']=self.dataset['Fatalities'].iloc[rowStart:rowEnd].to_string(index=False)
        for x in msg.keys():
            Label(self,text=x).grid(row=r,column=col,sticky=W)
            self.t=Text(self,width=45-change,height=rowEnd-rowStart,wrap=WORD)
            self.t.grid(row=r+2,column=col,rowspan=2,sticky=W)
            self.t.delete(0.0,END)
            self.t.insert(0.0,msg[x])
            self.t.config(state=DISABLED)
            self.t.tag_config('justified',justify=RIGHT)
            col+=1
            change+=5
        
    
        

root=Tk()
root.title("Data analysis of Aircrash Dataset")
root.geometry("2000x2000")
app=Application(root)
root.mainloop()