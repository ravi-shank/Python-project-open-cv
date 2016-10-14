#!/usr/bin/env python
import wx
import os.path
import wx.lib.agw.buttonpanel as bp
from TrainAndTest import *


class ocr_gui(wx.Frame):
    def __init__(self, parent, id):
        print 'inside ocr_gui'
        
        wx.Frame.__init__(self, parent, id, 'OCR_GUI',size=wx.DisplaySize(), style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)
        
        self.main_ocr_panel = wx.Panel(self, -1)
        self.picture_panel = wx.Panel(self.main_ocr_panel, -1, pos=(0,0), size=(1400,400))
        
        self.pictext = wx.TextCtrl(self.main_ocr_panel, -1,style=wx.TE_MULTILINE)
        self.choose_button = wx.Button(self.main_ocr_panel, -1, "choose image", pos=(50, 20))
        self.Bind(wx.EVT_BUTTON, self.OnClick_choose, self.choose_button)
        

        
        self.ocr_vsizer = wx.BoxSizer(wx.VERTICAL)                          # creating BoxSizer to fit wo panel picture_panel and logtext
        self.main_ocr_panel.SetSizer(self.ocr_vsizer)

        self.ocr_vsizer.Add(self.choose_button)
        self.ocr_vsizer.Add(self.picture_panel, 0, wx.EXPAND)
        self.ocr_vsizer.Add(self.pictext, 1, wx.EXPAND | wx.ALL, 5)
        self.ocr_vsizer.Layout()
        
        #self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnClick_choose(self, event):
        self.picture_panel.DestroyChildren() 
        open_ocr_Dialog = wx.FileDialog(self, "Choose a picture file", os.getcwd(),"", "*.*", wx.OPEN | wx.STAY_ON_TOP)
        if open_ocr_Dialog.ShowModal() == wx.ID_OK:
            ocr_loc = open_ocr_Dialog.GetPath()
            print ocr_loc
            img = wx.Image(ocr_loc, wx.BITMAP_TYPE_ANY)
            img2 = wx.StaticBitmap(self.picture_panel, wx.ID_ANY, wx.BitmapFromImage(img))
            self.pictext.Clear()            
            self.textans = do_ocr_rec(self, ocr_loc)
            print 'ret val=',self.textans
            self.pictext.WriteText(self.textans)
            #elf.pictext.AppendText(str(textans))

            self.pictext.Refresh()  
            self.ocr_vsizer.Layout()
        open_ocr_Dialog.Destroy()
    
    print 'finish'

        


