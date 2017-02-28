#!/usr/bin/env python
import wx
import os.path
import wx.grid
import sys, glob, cStringIO
from os import listdir


class Delete_model_GUI(wx.Frame):
    def __init__(self, parent, id):
        print 'inside delete model'
        screenSize = wx.DisplaySize()
        screenWidth = screenSize[0]
        screenHeight = screenSize[1]
        
        wx.Frame.__init__(self, parent, id, 'Delete Model',size=wx.DisplaySize(), style=wx.DEFAULT_FRAME_STYLE)

       

        #creating a panel
        self.panel_delete_model = wx.Panel(self, -1)
        self.vsizer_delete_model = wx.BoxSizer(wx.VERTICAL)
        self.top_hbox=wx.BoxSizer(wx.HORIZONTAL)
        self.middle_hbox=wx.BoxSizer(wx.HORIZONTAL)
        self.bottom_hbox=wx.BoxSizer(wx.HORIZONTAL)

        self.grid = wx.grid.Grid(self.panel_delete_model, -1, size=(screenWidth,600))

        
        # (100 rows and 10 columns in this example)
        self.grid.CreateGrid(100, 10)
        self.grid.SetRowSize(0, 60)
        self.grid.SetColSize(0, 60)
        
        self.label_src = wx.StaticText(self.panel_delete_model, label="Choose Model source directory")
        self.txt_src = wx.TextCtrl(self.panel_delete_model, size=(300,-1))
        self.txt_src.Disable()
        self.btn_choose_src = wx.Button(self.panel_delete_model, -1, "Choose")
        self.Bind(wx.EVT_BUTTON, self.OnClick_choose_Src, self.btn_choose_src)
        self.top_hbox.Add(self.label_src)
        self.top_hbox.Add(self.txt_src)
        self.top_hbox.Add(self.btn_choose_src)

        self.middle_hbox.Add(self.grid)

        self.btn_close = wx.Button(self.panel_delete_model, -1, "Close window")
        self.Bind(wx.EVT_BUTTON, self.OnCloseWindow, self.btn_close)
        self.bottom_hbox.Add(self.btn_close)

        #self.label_cnt = wx.StaticText(self.panel_new_model, label="Total no of images: ")


        self.vsizer_delete_model.Add(self.top_hbox)
        self.vsizer_delete_model.AddSpacer(10)
        self.vsizer_delete_model.Add(self.middle_hbox)
        self.vsizer_delete_model.AddSpacer(10)        
        self.vsizer_delete_model.Add(self.bottom_hbox,0, wx.ALIGN_CENTER)
        self.vsizer_delete_model.AddSpacer(10) 
    
    

        #creating vsizer
        self.panel_delete_model.SetSizer(self.vsizer_delete_model)
        self.vsizer_delete_model.Layout()
        self.Layout()
        
    def OnCloseWindow(self, event):
        self.Destroy()

    def OnClick_choose_Src(self, event):
        dialog = wx.DirDialog(None, "Choosethe model directory:",style=wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            path=dialog.GetPath()
            self.txt_src.SetValue(path)
        dialog.Destroy()

   
   


    
print 'All Ok'

        


