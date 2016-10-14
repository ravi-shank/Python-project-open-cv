#!/usr/bin/env python
import wx
import gui


class App(wx.App):
    def OnInit(self):
        self.frame = gui.MainUI(parent=None, id=-1)
        #self.frame.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)    # to show frame in full screen
        self.frame.Show()
        self.frame.Refresh()
        return True

def main():
    app= App()
    app.MainLoop()
        
if __name__ == '__main__':
    main()
    '''app = wx.PySimpleApp()
    frame = MainUI(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
    '''


