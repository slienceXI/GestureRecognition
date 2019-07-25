#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:53:01 2019

@author: ueharayou
"""

import os
import cv2
import json
import shutil

class BasicChar:
    fingerCnt = "0"
    orientation = "up"
    #protocol: up down left right
    
memory = BasicChar()

TRAINSET_DIR = './TrainSet/'

img_names = os.listdir(TRAINSET_DIR + 'img/unsorted/')
img_names = img_names.sort()

config_file = open(TRAINSET_DIR + "config/config.json", 'r')
config_dict = json.load(config_file)
config_file.close()

cv2.namedWindow("Preview", cv2.WINDOW_AUTOSIZE)

count = 0;
for img_name in img_names:
    print("File Name: {}".format(TRAINSET_DIR + 'img/' + img_name))
    img = cv2.imread(TRAINSET_DIR + 'img/unsorted/' + img_name)
    cv2.imshow("Preview", img)
    cv2.waitKey(30)
    print("memory: Finger Count: {}, Orientation: {}".format(memory.fingerCnt, memory.orientation))
    mode = input("Input characteristics <leave blank to use memory>:")
    if(len(mode) != 0): #update memory
        list_mode = mode.split()
        memory.fingerCnt = list_mode[0]
        memory.orientation = list_mode[1]
    config_dict['root'].append({"file_name": img_name, "finger_count": memory.fingerCnt, "orientation": memory.orientation})
    cv2.destroyAllWindows()
    shutil.move(TRAINSET_DIR + 'img/unsorted/' + img_name, TRAINSET_DIR + 'img/' + img_name)
    
    count += 1;
    if(count >= 1):
        count = 0;
        config_file = open(TRAINSET_DIR + "config/config.json", 'w')
        #ab = {"root": [{"file_name": "", "finger_count": "", "orientation": ""}]}
        json.dump(config_dict, config_file)
        config_file.close()
        
config_file = open(TRAINSET_DIR + "config/config.json", 'w')
#ab = {"root": [{"file_name": "", "finger_count": "", "orientation": ""}]}
json.dump(config_dict, config_file)
config_file.close()