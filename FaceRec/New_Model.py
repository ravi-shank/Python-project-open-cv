#!/usr/bin/env python
import wx
import os.path
import wx.lib.agw.buttonpanel as bp
from TrainAndTest import *
import training_operation
import sys, glob, cStringIO
import cv2 
from os import listdir
import time
import numpy as np

class New_Model_GUI(wx.Frame):
    def __init__(self, parent, id):
        print 'inside new model'
        screenSize = wx.DisplaySize()
        screenWidth = screenSize[0]
        screenHeight = screenSize[1]
        
        wx.Frame.__init__(self, parent, id, 'Create New Model',size=wx.DisplaySize(), style=wx.DEFAULT_FRAME_STYLE)

        #creating a panel
        self.panel_new_model = wx.Panel(self, -1)
        self.vsizer_new_model = wx.BoxSizer(wx.VERTICAL)
        self.top_hbox=wx.BoxSizer(wx.HORIZONTAL)
        self.middle_hbox=wx.BoxSizer(wx.HORIZONTAL)
        self.bottom_hbox=wx.BoxSizer(wx.HORIZONTAL)
        
        self.label_src = wx.StaticText(self.panel_new_model, label="Choose Image source directory")
        self.txt_src = wx.TextCtrl(self.panel_new_model, size=(300,-1))
        self.txt_src.Disable()
        self.btn_choose_src = wx.Button(self.panel_new_model, -1, "Choose")
        self.Bind(wx.EVT_BUTTON, self.OnClick_choose_Src, self.btn_choose_src)
        self.top_hbox.Add(self.label_src)
        self.top_hbox.Add(self.txt_src)
        self.top_hbox.Add(self.btn_choose_src)

        self.label_out = wx.StaticText(self.panel_new_model, label="Choose output directory")
        self.txt_out = wx.TextCtrl(self.panel_new_model, size=(300,-1))
        self.txt_out.Disable()
        self.btn_choose_save = wx.Button(self.panel_new_model, -1, "Choose")
        self.Bind(wx.EVT_BUTTON, self.OnClick_choose_Out, self.btn_choose_save)      
        self.middle_hbox.Add(self.label_out)
        self.middle_hbox.Add(self.txt_out)
        self.middle_hbox.Add(self.btn_choose_save)

        self.list_ctrl = wx.ListCtrl(self.panel_new_model, -1,size=(screenWidth,500) ,style=wx.LC_ICON | wx.LC_AUTOARRANGE)
        self.img_list = wx.ImageList(170,170, True)
        self.list_ctrl.AssignImageList(self.img_list, wx.IMAGE_LIST_NORMAL)

        self.label_model = wx.StaticText(self.panel_new_model, label="Choose folder to save model")
        self.txt_model = wx.TextCtrl(self.panel_new_model, size=(300,-1))
        self.txt_model.Disable()
        self.btn_choose_model = wx.Button(self.panel_new_model, -1, "Choose")
        self.Bind(wx.EVT_BUTTON, self.OnClick_choose_Model, self.btn_choose_model)        
        self.bottom_hbox.Add(self.label_model)
        self.bottom_hbox.Add(self.txt_model)
        self.bottom_hbox.Add(self.btn_choose_model)

        self.label_tag = wx.StaticText(self.panel_new_model, label="Tag name")
        self.txt_tag = wx.TextCtrl(self.panel_new_model, size=(300,-1))
        self.bottom_hbox.Add(self.label_tag)
        self.bottom_hbox.Add(self.txt_tag)
        

        #self.label_cnt = wx.StaticText(self.panel_new_model, label="Total no of images: ")

        self.btn_crop_load = wx.Button(self.panel_new_model, -1, "Crop and Load", size=(100,30))
        self.btn_crop_load.Enable(False)
        self.Bind(wx.EVT_BUTTON, self.Oncrop_load, self.btn_crop_load)

        self.btn_create_model = wx.Button(self.panel_new_model, -1, "Create Model", size=(100,30))
        self.btn_create_model.Enable(False)
        self.Bind(wx.EVT_BUTTON, self.createModel, self.btn_create_model)

        self.vsizer_new_model.Add(self.top_hbox)
        self.vsizer_new_model.AddSpacer(10)
        self.vsizer_new_model.Add(self.middle_hbox)
        self.vsizer_new_model.AddSpacer(10)

        self.vsizer_new_model.Add(self.btn_crop_load,0,wx.ALIGN_CENTER)
        self.vsizer_new_model.AddSpacer(10)
        
        self.vsizer_new_model.Add(self.list_ctrl)
        self.vsizer_new_model.AddSpacer(10)
        
        self.vsizer_new_model.Add(self.bottom_hbox)
        self.vsizer_new_model.AddSpacer(10) 
        self.vsizer_new_model.Add(self.btn_create_model,0,wx.ALIGN_CENTER)
    

        #creating vsizer
        self.panel_new_model.SetSizer(self.vsizer_new_model)
        self.vsizer_new_model.Layout()
        self.Layout()
        
        

    def OnClick_choose_Src(self, event):
        dialog = wx.DirDialog(None, "Choose a directory:",style=wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            path=dialog.GetPath()
            self.txt_src.SetValue(path)
        dialog.Destroy()

    def OnClick_choose_Out(self, event):
        dialog = wx.DirDialog(None, "Choose a directory:",style=wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            path=dialog.GetPath()
            self.txt_out.SetValue(path)
            self.btn_crop_load.Enable(True)
        dialog.Destroy()

    def OnClick_choose_Model(self, event):
        dialog = wx.DirDialog(None, "Choose a directory:",style=wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            path=dialog.GetPath()
            print "setting path"
            self.txt_model.SetValue(path)
            self.btn_create_model.Enable(True)
        dialog.Destroy()
        

    def createModel(self,event):
        print "inside create model"
        path=self.txt_model.GetValue()
        model_name=self.txt_tag.GetValue()
        eigen_model, people= train_model(path)
        print 'people'
        print people    # will print only 'ram' for now
        print "back at create model"
        print path
        eigen_model.save(path+"\\"+model_name+".xml")
        wx.MessageBox("Model trained and saved successfully", "Message" ,wx.OK | wx.ICON_INFORMATION) 
        print "model saved"
        

    def Oncrop_load(self, event):
        self.img_list.RemoveAll()
        #print src_path
        # paths to input and output images
        input_path= self.txt_src.GetValue()
        print "Oncrop inp path= ",input_path
        #output_path= "D:\8 sem project\main project Updated\output_images\\"
        output_path=self.txt_out.GetValue()+"\\"
        print "Oncrop out path= ",output_path

        # load pre-trained frontalface cascade classifier
        frontal_face= cv2.CascadeClassifier("haarcascades\haarcascade_frontalface_default.xml")
        input_names= listdir(input_path)

        print("Starting to detect faces in images and save the cropped images to output file...")
        sttime= time.clock()
        i= 1
        for name in input_names:
                print (input_path+ "\\" + name)
                color_img= cv2.imread(input_path+ "\\" + name)
                # converting color image to grayscale image
                gray_img= cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

                # find the bounding boxes around detected faces in images
                bBoxes= frontal_face.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
            
                for box in bBoxes:
                        #print(box)
                        # crop and save the image at specified location
                        cropImage(color_img, box, output_path, name)
                        i+= 1

        print("Successfully completed the task in %.2f Secs." % (time.clock()- sttime))
        displayImages(self) # function to display images inside Img_List
    
def displayImages(self):
    
    #self.img_list = wx.ImageList(170,170, True)
    output_path=self.txt_out.GetValue()+"\*"
    print "display Images path=",output_path
    for name in glob.glob(output_path):
        #print name
        bmp = wx.Bitmap(name, wx.BITMAP_TYPE_ANY)
        bmp=scale_image(bmp,170,170)
        self.img_list.Add(bmp)
        
    cnt=self.img_list.GetImageCount()
    
    #print "cnt=",cnt
    for x in range(0,cnt):
        img = x % (cnt+1)
        self.list_ctrl.InsertImageStringItem(x, "Image %d" % int(x+1), img)

def scale_image(bitmap,width,height):
        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(image)
        return result
    
        
    

def cropImage(img, box, output_path, name):
	[p, q, r, s]= box
	# crop and save the image provided with the co-ordinates of bounding box
	write_img_color= img[q:q+ s, p:p+ r]
	saveCropped(write_img_color, output_path, name)

# save the cropped image at specified location
def saveCropped(img, output_path, name):
	cv2.imwrite(output_path+ name, img)



def get_images(path, size):
    '''
    path: path to a folder which contains subfolders of for each subject/person
        which in turn cotains pictures of subjects/persons.

    size: a tuple to resize images.
        Ex- (256, 256)
    '''
    sub= 0
    images, labels= [], []
    people= []

    for subdir in os.listdir(path):
        for image in os.listdir(path+ "/"+ subdir):
            #print(subdir, images)
            img= cv2.imread(path+os.path.sep+subdir+os.path.sep+image, cv2.IMREAD_GRAYSCALE)
            img= cv2.resize(img, size)

            images.append(np.asarray(img, dtype= np.uint8))
            labels.append(sub)

            #cv2.imshow("win", img)
            #cv2.waitKey(10)

        people.append(subdir)
        sub+= 1

    return [images, labels, people]

def train_model(path):
    '''
    Takes path to images and train a face recognition model
    Returns trained model and people
    '''
    dir_path="D:\8 sem project\main project Updated\output_images\\"
    [images, labels, people]= get_images(dir_path, (256, 256))
    #print([images, labels])

    labels= np.asarray(labels, dtype= np.int32)
    print 'label'
    print labels

    # initializing eigen_model and training
    print("Initializing eigen FaceRecognizer and training...")
    sttime= time.clock()
    #eigen_model= cv2.face.createEigenFaceRecognizer()
    eigen_model= cv2.face.createLBPHFaceRecognizer()
    eigen_model.train(images, labels)
    print("\tSuccessfully completed training in "+ str(time.clock()- sttime)+ " Secs!")

    return [eigen_model, people]
        

    
print 'All Ok'

        


