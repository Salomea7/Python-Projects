# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 22:02:33 2019
Script that will convert all files from .LPV to .MP4
@author: salomea7
Needed a script to change 100 GoPro videos into a viewable format
"""

#! python3
import os
import shutil

# changes directory to correct one
os.chdir('CHANGE TO SOURCE FOLDER')
convertFrom = ('LRV')
convertTo = ('MP4')

#See's if the folder is already created
if not os.path.exists(convertTo):
    os.makedirs(convertTo)

#Append's the files to a list that can be iterated through
videoFiles = []
for filename in os.listdir(os.getcwd()):
    if filename.endswith('.' + convertFrom):
        videoFiles.append(filename)

# iterates through the file names in videoFiles, taking off the file endings and adding the correct ending.        
for files in videoFiles:
    try:
        shutil.move(os.getcwd() + '\\\\' + files, os.getcwd() + '\\\\' + convertTo + files[:-4] + "." + convertTo)
    except Exception:
        continue
