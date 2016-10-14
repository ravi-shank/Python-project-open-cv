#!/usr/bin/env python
import wx
class ocr_gui(wx.Frame):
    def __init__(self, parent, id):
        print 'inside ocr_gui'
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        self.main_ocr_Panel = wx.Panel(self, -1)
        self.picture_panel = wx.Panel(main_ocr_Panel, -1, pos=(0,0), size=(1400,0))
        self.logtext = wx.TextCtrl(mainPanel, -1, "fss", style=wx.TE_MULTILINE)
        

        
        self.ocr_vsizer = wx.BoxSizer(wx.VERTICAL)                          # creating BoxSizer to fit wo panel picture_panel and logtext
        main_ocr_panel.SetSizer(self.ocr_vsizer)
        
        self.ocr_vsizer.Add(self.picture_panel, 0, wx.EXPAND)
        self.ocr_vsizer.Add(self.logtext, 1, wx.EXPAND | wx.ALL, 5)
        self.ocr_vsizer.Layout()
        
        #self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        

