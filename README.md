
#Face Recognition Software

#To run this project, 
--------------------------------------------------------------------------------------------------------
#Step 1: 
Copy / clone my repository in your local machine.
Install below softwares

1. Python 2.7 (http://python.org/ftp/python/2.7.5/python-2.7.5.msi)

2. Numpy      (http://sourceforge.net/projects/numpy/files/NumPy/1.7.1/numpy-1.7.1-win32-superpack-python2.7.exe/download)

3. Matplotlib 

4. OpenCV 3.0    (http://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.4.6/OpenCV-2.4.6.0.exe/download)

5. wxPython 3.0   (https://wxpython.org/download.php)

Note : All softwares should be installed at their default directories.

#Step 2 :
After installing the above softwares we need to do one more thing, since this is a face recognition software we need the face module inside our python
(C:\Python27\Lib\site-packages). For this i have already built the face module (only not all) from binaries using this github(https://github.com/opencv/opencv_contrib).
You can see there is a folder called face inside module folder in opencv contrib github that i have mentioned. So i have already provided a file called cv2.pyd and all necessary .dll files in a folder called "Important files" in my repository.
Go ahead and copy all the files (not folder)(ie, cv2.pyd and .dll files and paste them inside your C:\Python27\Lib\site-packages\ folder or wherever your python software is installed.

PS: If you want to learn how to (cmake) build from binaries, then try this (http://audhootchavancv.blogspot.in/2015/08/how-to-install-opencv-30-and.html).

#Step 3: 
Having performed all the above steps, go ahead and open the main.py file from my downloaded repository folder in Idle or with any other python-compiler attched software like pycharms etc.
Hit F5 in idle if using default python interpreter.

You have successfully run the software.
#Note:
Your python-compiler location must be present in the OS environment variables if you are running the project from directories other than python.

#To set python environment variable 
Please visit here. (http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7)


In case you find any diffilculties in running or installing required softwares kindly comment.



