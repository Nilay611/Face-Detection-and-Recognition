# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 01:35:54 2020

@author: Magnus
"""

import cv2
import face_recognition as fr
import pickle
import numpy as np

def draw_border(img,pt1,pt2,color,thickness,r,d1,d2):
    x1,y1=pt1
    x2,y2=pt2
    
    # Top left
    cv2.line(img, (x1 + r, y1), (x1 + r + d1, y1), color, thickness)
    cv2.line(img, (x1, y1 + r), (x1, y1 + r + d2), color, thickness)
    cv2.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thickness)

    # Top right
    cv2.line(img, (x2 - r, y1), (x2 - r - d1, y1), color, thickness)
    cv2.line(img, (x2, y1 + r), (x2, y1 + r + d2), color, thickness)
    cv2.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thickness)

    # Bottom left
    cv2.line(img, (x1 + r, y2), (x1 + r + d1, y2), color, thickness)
    cv2.line(img, (x1, y2 - r), (x1, y2 - r - d2), color, thickness)
    cv2.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thickness)

    # Bottom right
    cv2.line(img, (x2 - r, y2), (x2 - r - d1, y2), color, thickness)
    cv2.line(img, (x2, y2 - r), (x2, y2 - r - d2), color, thickness)
    cv2.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thickness)

def names(name,path):
    name_img=fr.load_image_file(path)
    name_img_fen=fr.face_encodings(name_img)[0]
    record={}
    with open('dataset_faces.dat', 'rb') as f:
        record=pickle.load(f)
    record[name]=name_img_fen
    with open('dataset_faces.dat', 'wb') as f:
        pickle.dump(record, f)

def main(path):
    record={}
    with open('dataset_faces.dat', 'rb') as f:
        record=pickle.load(f)
    known_face_names = list(record.keys())
    known_face_encodings = np.array(list(record.values()))
    image=cv2.imread(str(path))
    height, width, channel = image.shape
    if width>1024:
        image=cv2.resize(image, (0,0), fx=0.25, fy=0.25)
    face_locations=fr.face_locations(image,model="cnn")
    no_of_faces=len(face_locations)
    face_fens=fr.face_encodings(image, face_locations)
    for current_face_location, current_face_encoding in zip(face_locations,face_fens):
        top, right, bottom, left=current_face_location
        all_matches=fr.compare_faces(known_face_encodings, current_face_encoding)
        face_name="Unknown"
        if True in all_matches:
            match_index=all_matches.index(True)
            face_name=known_face_names[match_index]
            
        d1=int((right-left)*0.15)
        d2=int((bottom-top)*0.15)
        draw_border(image, (left,top), (right,bottom), (255,255,0), 2, 10, d1,d2)
        font=cv2.cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        cv2.putText(image, face_name, (left-25,top-25), font, 0.75, (0,0,255),1)
        #cv2.imshow("Final", image)
    return image
