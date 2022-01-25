from importlib.resources import path
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime   

path='images'
images=[]
person_name=[]
mylist=os.listdir(path)
print(mylist)

for i in mylist:
    curr=cv2.imread(f'{path}/{i}')
    images.append(curr)
    person_name.append(os.path.splitext(i)[0])
print(person_name)


def faceencoding(images):
    en_list=[]
     
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        en_list.append(encode)

    return en_list;


encodelistdone=faceencoding(images)
print("Encodings Done")


cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    faces=cv2.resize(frame,(0,0),None,0.25,0.25)
    faces=cv2.cvtColor(faces,cv2.COLOR_BGR2RGB)

    
    facescurrentframe=face_recognition.face_locations(faces)
    encodescurrentframe=face_recognition.face_encodings(faces,facescurrentframe)

    for encodeface,faceloc in zip(encodescurrentframe,facescurrentframe):
        matches=face_recognition.compare_faces(encodelistdone,encodeface)
        facedist=face_recognition.face_distance(encodelistdone,encodeface)

        



