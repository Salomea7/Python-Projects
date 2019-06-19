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
os.chdir('CHANGE TO FOLDER')

#See's if the folder is already created
if not os.path.exists('MP4'):
    os.makedirs('MP4')

#Append's the files to a list that can be iterated through
videoFiles = []
for filename in os.listdir('CAN BE CWD OR THE SAME AS CHDIR ABOVE'):
    if filename.endswith('.LPV'):
        videoFiles.append(filename)

# iterates through the file names in videoFiles, taking off the file endings and adding the correct ending.        
for files in videoFiles:
    try:
        shutil.move('SOURCE FOLDER' + files, 'DESTINATION FOLDER' + files[:-4] + ".MP4")
    except Exception:
        continue
