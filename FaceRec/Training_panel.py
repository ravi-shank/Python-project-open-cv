import wx
import sys
import os.path
#from training_operation import *
from operation import *
class Training_panel(wx.Panel):
    
    def __init__(self,parent):
        
        wx.Panel.__init__(self, parent, pos=(0, 0), size=(1400, 0))
        
        #creating training buttons
        self.new_model_btn = wx.Button(self, label="training")
        self.update_model_btn = wx.Button(self, label="update")
        self.delete_model_btn = wx.Button(self, label="delete")
        self.view_model_btn= wx.Button(self, label="view")

        #binding buttons
        self.new_model_btn.Bind(wx.EVT_BUTTON, self.On_New_Model)
        self.update_model_btn.Bind(wx.EVT_BUTTON, self.On_update_Model)
        self.delete_model_btn.Bind(wx.EVT_BUTTON, self.On_Delete_Model)
        self.view_model_btn.Bind(wx.EVT_BUTTON, self.On_View_Model)

        #adding buttons to Boxsizer
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.new_model_btn,0,wx.ALIGN_CENTER)
        self.vbox.Add(self.update_model_btn,0,wx.ALIGN_CENTER)
        self.vbox.Add(self.delete_model_btn,0,wx.ALIGN_CENTER)
        self.vbox.Add(self.view_model_btn,0,wx.ALIGN_CENTER)
        self.SetSizer(self.vbox)
        #self.Layout()
    
        
    def On_New_Model(self,event):
        print "open traiing dialoag"
        file_name =  os.path.basename(sys.argv[0])
        print file_name
        do_On_New_Model(self,event)
        
        
    def On_update_Model(self,event):
        open_File_Dialog = wx.FileDialog(None, "Choose a video file", os.getcwd(),"", "*.avi*", wx.OPEN)

    def On_Delete_Model(self,event):
        open_File_Dialog = wx.FileDialog(None, "Choose a video file", os.getcwd(),"", "*.avi*", wx.OPEN)

    def On_View_Model(self,event):
        MainUI.OnImage(self, event)
        
         
