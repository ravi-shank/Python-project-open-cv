import wx
import numpy as np
import cv2
import os.path
import sys
import wx.lib.agw.buttonpanel as bp
#Sfrom training_operation import *
from ocr import *
from New_Model import *
from Delete_model import *

if hasattr(sys, "frozen"):
    pathExe = sys.executable
else:
    pathExe = sys.argv[0]

if os.environ["PATH"][-1] != os.pathsep:
    os.environ["PATH"] += os.pathsep

os.environ["PATH"] += os.path.join(os.path.dirname(pathExe), "libraries/opencv/build/x86/mingw/bin")



def do_OnRecog(self, event):
    print 'inside reg'
    
    self.vSizer1 = wx.BoxSizer(wx.VERTICAL)
    self.work_panel.SetSizer(self.vSizer1)

    self.buttonMenu1 = bp.ButtonPanel(self.work_panel, -1)
    self.buttonMenu1_2= bp.ButtonPanel(self.work_panel, -1)
    
    self.face = bp.ButtonInfo(self.buttonMenu1, wx.NewId(), wx.Bitmap(os.path.join(os.path.dirname(pathExe), "images/face_recog.png"), wx.BITMAP_TYPE_ANY), shortHelp = "face recoginition")
    self.buttonMenu1.AddButton(self.face)
    self.Bind(wx.EVT_BUTTON, lambda event:OnFaceButton(event, self), self.face)  # used lambda since OnfaceButton is not a class method
    
    self.buttonMenu1.AddSeparator()

    self.char = bp.ButtonInfo(self.buttonMenu1, wx.NewId(), wx.Bitmap(os.path.join(os.path.dirname(pathExe), "images/char_recog.png"), wx.BITMAP_TYPE_ANY), shortHelp = "character recognition")
    self.buttonMenu1.AddButton(self.char)
    self.Bind(wx.EVT_BUTTON, lambda event:OnCharButton(event, self), self.char)  # used lambda since OnfaceButton is not a class method
    
    
    self.vSizer1.Add(self.buttonMenu1, 0, wx.EXPAND)
    self.vSizer1.Add((130,130))
    self.vSizer1.Add(self.buttonMenu1_2, 0, wx.EXPAND)
    
    
    # Doing layout
    self.buttonMenu1.DoLayout()
    self.buttonMenu1_2.DoLayout()
    self.vSizer1.Layout()
    self.Layout()           # i was missing this.(button menu wasn't getting refreshed when video menu was clicked)
    
    
    
    
    

def do_OnVideo(self,event):
    print 'inside video'
    
    vSizer = wx.BoxSizer(wx.VERTICAL)
    self.work_panel.SetSizer(vSizer)

    buttonMenu = bp.ButtonPanel(self.work_panel, -1)
    
    #openCamera = bp.ButtonInfo(buttonMenu, wx.NewId(), wx.Bitmap(os.path.join(os.path.dirname(pathExe), "images/camera.png"), wx.BITMAP_TYPE_ANY), text="open camera" ,shortHelp = "Open camera")
    #buttonMenu.AddButton(openCamera)
    #buttonMenu.AddSeparator()

    openVideo = bp.ButtonInfo(buttonMenu, wx.NewId(), wx.Bitmap(os.path.join(os.path.dirname(pathExe), "images/video.png"), wx.BITMAP_TYPE_ANY), text="capture video",shortHelp = "Open video")
    buttonMenu.AddButton(openVideo)
    self.Bind(wx.EVT_BUTTON, onVideoRecording, openVideo)
    
    vSizer.Add(buttonMenu,0, wx.EXPAND)
    vSizer.Add((20,20))
    
    # Doing layout
    buttonMenu.DoLayout()
    vSizer.Layout()
    self.Layout()           # i was missing this.(button menu wasn't getting refreshed when video menu wa clicked)


def do_OnImage(self,event):
    print 'inside Image'
    
    vSizer3= wx.BoxSizer(wx.VERTICAL)
    self.work_panel.SetSizer(vSizer3)

    buttonMenu3 = bp.ButtonPanel(self.work_panel, -1)
    
    openCamera = bp.ButtonInfo(buttonMenu3, wx.NewId(), wx.Bitmap(os.path.join(os.path.dirname(pathExe), "images/camera.png"), wx.BITMAP_TYPE_ANY), text="open camera" ,shortHelp = "Open camera")
    buttonMenu3.AddButton(openCamera)
    self.Bind(wx.EVT_BUTTON, onImageCapture, openCamera)
    
    #buttonMenu3.AddSeparator()
    
    vSizer3.Add(buttonMenu3,0, wx.EXPAND)
    vSizer3.Add((20,20))
    
    # Doing layout
    buttonMenu3.DoLayout()
    vSizer3.Layout()
    self.Layout()           # i was missing this.(button menu wasn't getting refreshed when video menu was clicked)


def do_OnTraining(self,event):
    
    
    
    #creating buttons
    self.btn_new_model    = wx.Button(self.training_panel, -1,label="new model")
    self.btn_update_model = wx.Button(self.training_panel, -1, label="update")
    self.btn_delete_model = wx.Button(self.training_panel, -1,label="delete")
    self.btn_view_model   = wx.Button(self.training_panel, -1,label="view")

    #binding buttons to functions
    self.Bind(wx.EVT_BUTTON, lambda event:On_New_Model(event, self), self.btn_new_model)
    self.Bind(wx.EVT_BUTTON, lambda event:On_update_Model(event, self), self.btn_update_model)
    self.Bind(wx.EVT_BUTTON, lambda event:On_Delete_Model(event, self), self.btn_delete_model)
    self.Bind(wx.EVT_BUTTON, lambda event:On_View_Model(event, self), self.btn_view_model)

    #adding buttons to Boxsizer
    self.vbox = wx.BoxSizer(wx.VERTICAL)    
    self.training_panel.SetSizer(self.vbox)
    
    #adding buttons to vertical sizer vbox
    self.vbox.Add(self.btn_new_model,0,wx.ALIGN_CENTER)
    self.vbox.Add(self.btn_update_model,0,wx.ALIGN_CENTER)
    self.vbox.Add(self.btn_delete_model,0,wx.ALIGN_CENTER)
    self.vbox.Add(self.btn_view_model,0,wx.ALIGN_CENTER)

    self.SetAutoLayout(True)
    self.training_panel.SetSizer(self.vbox)
    self.training_panel.Layout()
    
    self.training_panel.Show()
    
    self.Layout()
    
    
    print "xxxx"    


#-----------------------------------------------------Workings Functions for Recognition menu-------------------------------------------------------------------------------------------------#
    
#-----------------------------------------------------Workings Functions for FaceRecog  button -------------------------------------------------------------------------------------------------#


def OnFaceButton(event,self):
    
    print 'hi face'

    self.face.Enable(False)  # Diasbles the face button
    self.char.Enable(True)  # Diasbles the face button

    
    #self.vSizer1.Detach(self.buttonMenu1_2)
    #self.vSizer1.Remove(self.buttonMenu1_2)
    
    self.buttonMenu1_2.Destroy()    # beacause of the options of Onfacebutton were coming when clicked on oncharbuttoon
    
    
    self.buttonMenu1_2= bp.ButtonPanel(self.work_panel, -1)
    
    self.camera_icon = bp.ButtonInfo(self.buttonMenu1_2, wx.NewId(), wx.Bitmap(os.path.join(os.path.dirname(pathExe), "images/camera_icon.png"), wx.BITMAP_TYPE_ANY), text="Open Camera" ,shortHelp = "open camera")
    self.buttonMenu1_2.AddButton(self.camera_icon)
    self.Bind(wx.EVT_BUTTON, FaceRec_From_Camera, self.camera_icon)
    
    self.buttonMenu1_2.AddSeparator()
    #self.buttonMenu1_2.AddSpacer(size=(1,1), proportion=1)

    self.folder_icon = bp.ButtonInfo(self.buttonMenu1_2, wx.NewId(), wx.Bitmap(os.path.join(os.path.dirname(pathExe), "images/folder_icon.png"), wx.BITMAP_TYPE_ANY), text="Open Folder" ,shortHelp = "open folder")
    self.buttonMenu1_2.AddButton(self.folder_icon)
    self.Bind(wx.EVT_BUTTON, FaceRec_From_File, self.folder_icon)
    
    
    self.vSizer1.Add(self.buttonMenu1_2, 0, wx.EXPAND)
    
    
    # Doing layout
    self.buttonMenu1_2.DoLayout()
    self.vSizer1.Layout()
    self.Layout()           # i was missing this.(button menu wasn't getting refreshed when video menu was clicked)
    
    
    

    






def FaceRec_From_Camera( event):
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
    
    cap = cv2.VideoCapture(0)           # capture form camera
    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.5, 5)
        #img = cv2.resize(img,(700,1000))

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'face',(x-w,y-h), font, 2, (0,255,255), 2, cv2.LINE_AA)     #syntax: (img_file, text, box_size, font_name, font_size, font_color, font_width, dont_know)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def FaceRec_From_File(event):
    print 'open from file'
    file_loc=''
    open_File_Dialog = wx.FileDialog(None, "Choose a video file", os.getcwd(),"", "*.avi*", wx.OPEN)
    
    if open_File_Dialog.ShowModal() == wx.ID_OK:
        file_loc = open_File_Dialog.GetPath()
        print file_loc
        do_FaceRec_From_File(file_loc)
    open_File_Dialog.Destroy()
    
    print 'finish'


def do_FaceRec_From_File(file_loc):
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
    
    cap = cv2.VideoCapture(file_loc)         # capturing video from file
    while (cap.isOpened()):
        ret, img = cap.read()
        if ret==True:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            break
        
        faces = face_cascade.detectMultiScale(gray, 1.5, 5)
        #img = cv2.resize(img,(700,1000))

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'face',(x-w,y-h), font, 2, (0,255,255), 2, cv2.LINE_AA)     #syntax: (img_file, text, box_size, font_name, font_size, font_color, font_width, dont_know)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()



#-----------------------------------------------------Workings Functions for CharRecog  button -------------------------------------------------------------------------------------------------#
def OnCharButton(event,self):


    self.char.Enable(False)  # Diasbles the char button
    self.face.Enable(True)  # Diasbles the face button

    
    self.buttonMenu1_2.Destroy()    # beacause of the options of Onfacebutton was coming when clicked on oncharbuttoon

    
    print 'pass face'
    self.buttonMenu1_2= bp.ButtonPanel(self.work_panel, -1)
    
    self.image_icon = bp.ButtonInfo(self.buttonMenu1_2, wx.NewId(), wx.Bitmap(os.path.join(os.path.dirname(pathExe), "images/image_icon.png"), wx.BITMAP_TYPE_ANY), text="Open file" ,shortHelp = "choose image")
    self.buttonMenu1_2.AddButton(self.image_icon)
    self.Bind(wx.EVT_BUTTON, OCR_From_Image, self.image_icon)
    
    self.buttonMenu1_2.AddSeparator()
    #self.buttonMenu1_2.AddSpacer(size=(1,1), proportion=1)

    self.web_icon = bp.ButtonInfo(self.buttonMenu1_2, wx.NewId(), wx.Bitmap(os.path.join(os.path.dirname(pathExe), "images/web_icon.png"), wx.BITMAP_TYPE_ANY), text="Open from web" ,shortHelp = "open image from web")
    self.buttonMenu1_2.AddButton(self.web_icon)
    self.Bind(wx.EVT_BUTTON, OCR_From_Web, self.web_icon)
    
    
    
    
    self.vSizer1.Add(self.buttonMenu1_2, 0, wx.EXPAND)
    
    
    # Doing layout
    self.buttonMenu1_2.DoLayout()
    self.vSizer1.Layout()
    #self.Layout()           # i was missing this.(button menu wasn't getting refreshed when video menu was clicked)
    

def OCR_From_Image(event):
    print 'ocr from file'
    ocr_frame = ocr_gui(None, -1)
    ocr_frame.Show()
    ocr_frame.Update()
    event.Skip()

def OCR_From_Web(event):
    print 'ocr from web'

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------End of OnRecognition menu----------------------------------------------------------------------#

    

#-----------------------------------------------------Workings Functions for OnVideo menu-------------------------------------------------------------------------------------------------#

def onVideoRecording(event):
    dir_dialog = wx.DirDialog(None, "Choose a directory...", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
    file_name_dialog = wx.TextEntryDialog(None,"Enter the name of the file you want to save with...", "Enter file name", "", style=wx.OK|wx.CANCEL)
    warning_dialog = wx.MessageDialog(file_name_dialog, "File name can't be Null", caption="Error",style=wx.OK, pos=wx.DefaultPosition)
    
    if file_name_dialog.ShowModal() == wx.ID_OK:
        file_name = file_name_dialog.GetValue()
        print 'file name=', file_name
        if file_name=="":
            if warning_dialog.ShowModal() == wx.ID_OK:
                warning_dialog.Destroy()
        else:
            if dir_dialog.ShowModal() == wx.ID_OK:
                print 'dir path=',dir_dialog.GetPath()
                dir_loc = dir_dialog.GetPath()
                capture_video(file_name, dir_loc)              # calling video capture function
            
        dir_dialog.Destroy()
    file_name_dialog.Destroy()
    
   

def capture_video(file_name, dir_loc):
    print 'inside vid'
    cap = cv2.VideoCapture(0)                   # capture from camera
    dir_loc= dir_loc+ "\\" + file_name
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc('i','Y','U','V')
    out = cv2.VideoWriter(dir_loc, fourcc, 20.0, (640,480))
    font=cv2.FONT_HERSHEY_SIMPLEX
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            #frame = cv2.flip(frame,0)  # to flip the frame

            out.write(frame)
            cv2.putText(frame,'Press q to quit', (0,20), font, 0.5, (0,255,255), 1, cv2.LINE_AA)
            cv2.imshow('frame',frame)
            if cv2.waitKey(30) & 0xff == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print 'video written'




def onImageCapture(event):
    dir_dialog = wx.DirDialog(None, "Choose a directory...", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
    file_name_dialog = wx.TextEntryDialog(None,"Enter the name of the file you want to save with...", "Enter file name", "", style=wx.OK|wx.CANCEL)
    warning_dialog = wx.MessageDialog(file_name_dialog, "File name can't be Null", caption="Error",style=wx.OK, pos=wx.DefaultPosition)
    
    if file_name_dialog.ShowModal() == wx.ID_OK:
        file_name = file_name_dialog.GetValue()
        print 'file name=', file_name
        if file_name=="":
            if warning_dialog.ShowModal() == wx.ID_OK:
                warning_dialog.Destroy()
        else:
            if dir_dialog.ShowModal() == wx.ID_OK:
                print 'dir path=',dir_dialog.GetPath()
                dir_loc = dir_dialog.GetPath()
                capture_Image(file_name, dir_loc)              # calling video capture function
            
        dir_dialog.Destroy()
    file_name_dialog.Destroy()
    
   

def capture_Image(file_name, dir_loc):
    print 'inside vid'
    cap = cv2.VideoCapture(0)                   # capture from camera
    dir_loc= dir_loc+ "\\" + file_name
    # Define the codec and create VideoWriter object
    font=cv2.FONT_HERSHEY_SIMPLEX
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            cv2.putText(frame,'', (0,20), font, 0.5, (0,255,255), 1, cv2.LINE_AA)
            cv2.imshow('Capture Image',frame)
            k = cv2.waitKey(30) & 0xff
            if k==ord('s'):
                cv2.imwrite(dir_loc,frame)
                break
            elif k==ord('q'):
                cap.release()
                cv2.destroyAllWindows()
            

    # Release everything if job is finished
    cap.release()
    cv2.destroyAllWindows()
    print 'image written'


def On_New_Model(self, event):
    print "inside trng operaiton"
    new_model_frame = New_Model_GUI(None, -1)
    new_model_frame.Show()
    new_model_frame.Update()

def On_Delete_Model(self, event):
    print "inside trng operaiton"
    del_model_frame = Delete_model_GUI(None, -1)
    del_model_frame.Show()
    del_model_frame.Update()
    
    
