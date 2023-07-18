

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:58:33 2020

@author: Neethu Venugopal
"""
import tkinter
from tkinter import filedialog
import cv2
import os


refPt = []
cropping = False
frame = []
clone = []
flag = 0


# mouse event handling function
def click_and_crop(event,x,y,flags,param):
    
    global refPt, cropping, frame, clone, flag
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if flag == 0:
            refPt = [(x,y)]
            cropping = True
        
    elif event == cv2.EVENT_LBUTTONUP:
        if flag == 0:
            refPt.append((x,y))
            cropping = False
            flag = 1
        
        
        
    if cropping == True:
        frame = clone.copy()    
        cv2.rectangle(frame, refPt[0], (x,y) , (0,255,0), 2)
        cv2.imshow("image", frame)
        
    elif (cropping == False and len(refPt) == 2):
        frame = clone.copy()    
        cv2.rectangle(frame, refPt[0], refPt[1] , (0,255,0), 2)
        cv2.imshow("image", frame)

#cropping window setting function
def getPoints(clone):
    global refPt, frame, flag
    
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    
    while True:
        
        cv2.imshow("image",frame)
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord("r"): # press 'r' to reset selection
            frame = clone.copy()
            refPt = []
            flag = 0
            
        elif key == ord("c"):  # press 'c' to confirm window and continue cropping
            cv2.destroyAllWindows()
            break
    return refPt

# crop and save video
def cropVideo(cap,clone,filename):
    
    outFile = os.path.splitext(filename)[0] + 'out.m4v'
    w = refPt[1][0] - refPt[0][0]
    h = refPt[1][1] - refPt[0][1]
    fps  = float(cap.get((cv2.CAP_PROP_FPS))) 
    out = cv2.VideoWriter(outFile,cv2.VideoWriter_fourcc('m','p','4','v'),fps,(w,h))# may need to change fourcc codec based on system
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    out.write(roi)
    while True:
        ret,frame = cap.read()
        if frame is not None:
            clone = frame.copy()
            roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
            out.write(roi)
            cv2.imshow("ROI", roi)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
        else:
            break
    out.release()
    cv2.destroyAllWindows()
    
# main function to read and process video    
if __name__ == "__main__":
    root = tkinter.Tk()
    file = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    if file != None:
        cap = cv2.VideoCapture(file.name)
        root.withdraw()
        
        if (cap.isOpened() == False):
            print("Error opening video stream or file")
            
        else:    
            ret,frame = cap.read()
            if ret == True:
                clone = frame.copy()
                cropPnts = getPoints(clone) #function to select crop window
                if len(refPt) == 2:
                    cropVideo(cap,clone,file.name) # function to crop frame
                    cap.release()
    else:
        root.withdraw()
                
                
    
    