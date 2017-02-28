#!/usr/bin/env python
import wx
import operation
#import training_operation


class MainUI(wx.Frame):
    def __init__(self, parent, id):
        print 'inside gui'
        wx.Frame.__init__(self, parent, id, 'Face Rec', size=wx.DisplaySize())

        #creating menu_panel
        self.menu_panel = wx.Panel(self, -1, pos=(0, 0), size=(100, 0))
        self.menu_panel.SetBackgroundColour("maroon")

        #creating work_panel
        self.work_panel = wx.Panel(self, -1, pos=(0, 0), size=(1400, 0))
        
        #creating training panel
        self.training_panel = wx.Panel(self, -1, pos=(0, 0), size=(1400, 0))
        self.training_panel.SetBackgroundColour("green")
        #self.training_panel.Hide()
        
        
        # creating status bar
        self.work_statusbar = self.CreateStatusBar()  

        # creating BoxSizer to fit work_panel and menu_panel 
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.sizer.Add(self.menu_panel, 0, wx.EXPAND)
        self.sizer.Add(self.work_panel, 0, wx.EXPAND)
        self.sizer.Add(self.training_panel, 0, wx.EXPAND)
        self.SetSizer(self.sizer)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        # Initiate work here                
        self.createMenuBar()
        self.createButtonBar(self.menu_panel)
        # ----------------------------------------------------------------------------------------------------------------------------------

    def menuData(self):
        return (
            ("&File",
             ("&Open\tCtrl-O", "Open in status bar", self.OnOpen),
             ("&Quit\tCtrl-Z", "Quit", self.OnCloseWindow)),
            ("&Edit",
             ("&Copy", "Copy", self.OnCopy),
             ("C&ut", "Cut", self.OnCut),
             ("&Paste", "Paste", self.OnPaste),
             ("", "", ""),
             ("&Options...", "DisplayOptions", self.OnOptions)),
            ("&Help",
             ("&About\tCtrl-A", "About", self.OnAbout))
        )

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1:]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)

    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachLabel, eachStatus, eachHandler in menuData:
            if not eachLabel:
                menu.AppendSeparator()
                continue
            menuItem = menu.Append(-1, eachLabel, eachStatus)
            self.Bind(wx.EVT_MENU, eachHandler, menuItem)
        return menu

    '''----------------------------------------------------------------------------------------------------------------------------------'''

    def buttonData(self):
        return (("Recognition", self.OnRecog),
                ("Image", self.OnImage),
                ("Video", self.OnVideo),
                ("Training", self.OnTraining))

    def createButtonBar(self, panel, yPos=10):
        xPos = 0
        for eachLabel, eachHandler in self.buttonData():
            pos = (xPos, yPos)
            button = self.buildOneButton(panel, eachLabel, eachHandler, pos)
            yPos += button.GetSize().width + 60

    def buildOneButton(self, parent, label, handler, pos=(0, 0)):
        button = wx.Button(parent, -1, label, pos)
        self.Bind(wx.EVT_BUTTON, handler, button)
        return button

    # -----------------------------------------Operating functions-----------------------------------------------------------------------------------------

    def OnRecog(self, event):
        self.work_panel.Show()
        self.work_panel.DestroyChildren()  # to destroy previous buttonmenu
        operation.do_OnRecog(self, event)  # function is defined in operation.py
        event.Skip()

    def OnVideo(self, event):
        self.work_panel.Show()
        self.work_panel.DestroyChildren()  # to destroy previous buttonmenu
        operation.do_OnVideo(self, event)  # function is defined in operation.py
        event.Skip()

    def OnImage(self, event):
        self.work_panel.Show()
        self.work_panel.DestroyChildren()  # to destroy previous buttonmenu
        operation.do_OnImage(self, event)  # function is defined in operation.py
        event.Skip()

    def OnTraining(self, event):
        self.work_panel.DestroyChildren()  # to destroy previous buttonmenu
        self.work_panel.Hide()
        operation.do_OnTraining(self, event)  # function is defined in operation.py
        event.Skip()

    def OnOpen(self, event):
        pass

    def OnCopy(self, event):
        pass

    def OnCut(self, event):
        pass

    def OnPaste(self, event):
        pass

    def OnOptions(self, event):
        pass

    def OnCloseWindow(self, event):
        self.Destroy()

    def OnAbout(self, event):
        wx.MessageBox("This software uses OpenCV and wxPython for Face recognition.\n\n\n"
                      "Copyright (C) 2016 Ravi\n\n"
                      "This application is not afree software; you can't redistribute it and/or\n"
                      "modify it under the terms of the GNU Lesser General Public\n"
                      "Below are the packages/libraries needed to intalled befor running this software\n\n"
                      "1. Python 2.7 or higher\n"
                      "2. Numpy\n"
                      "3. OpenCV 3.0 or higher\n"
                      "===============================================\n\n"
                      "To run this software you need to copy the files in C:\Python27\ directory(default)\n"
                      "or set the environment variable for python interpreter\n"
                      " and open the main.py file with idle and press F5\n"
                      "===============================================\n\n",
                      "FaceRec - version 1.0", wx.OK | wx.ICON_INFORMATION)
