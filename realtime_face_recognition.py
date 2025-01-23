# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 00:27:34 2020

@author: Magnus
"""


import cv2
import face_recognition as fr
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

def main(current_frame,record):

    face_locations=[]
    current_frame_s=cv2.resize(current_frame, (0,0), fx=0.25, fy=0.25)
    face_locations=fr.face_locations(current_frame_s, number_of_times_to_upsample=2, model="cnn")
    no_of_faces=len(face_locations)
    face_fens=fr.face_encodings(current_frame_s, face_locations)
    #print(no_of_faces)
    for current_face_location, current_face_encoding in zip(face_locations,face_fens):
        top, right, bottom, left=current_face_location
        top=top*4
        bottom=bottom*4
        left=left*4
        right=right*4
        all_matches=fr.compare_faces(np.array(list(record.values())), current_face_encoding)
        face_name="Unknown"
        if True in all_matches:
            match_index=all_matches.index(True)
            face_name=list(record.keys())[match_index]
        d1=int((right-left)*0.15)
        d2=int((bottom-top)*0.15)
        draw_border(current_frame, (left,top), (right,bottom), (255,255,0), 2, 10, d1,d2)
        font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        cv2.putText(current_frame, face_name, (left,top-25), font, 1.25, (0,0,255),2)
    return current_frame
