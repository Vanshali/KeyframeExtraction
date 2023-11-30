import csv
import numpy as np
#import cv2
import glob
import matplotlib.pyplot as plt
import re
import os


def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts        

numbers = re.compile(r'(\d+)')
path ='./runs/val/exp98/labels/'+str('**/*.txt')
file_list=sorted(glob.glob(path, recursive=True),key=numericalSort)
#print(file_list)
key_name=['Image','x_center','y_center','width','height','confidence_score','Area','Distance','Score']
with open(str('result.csv'), 'a',newline="") as f:
    wr = csv.writer(f)
    wr.writerow(key_name)

info_list=[]

for file in file_list:
    x=[]
    with open(file,'r+') as f:
        lines=f.read().splitlines()
        for i in range(len(lines)):
            print(lines[i])
        print(lines[0].split()[5])
        a = len(lines[0].split())
        print(a)
        
        info_list.append(os.path.basename(file).rpartition('.')[0])

        for j in range(len(lines)):
            for i in range(1,6):
                if(float(lines[j].split()[5])>0.5):
                    info_list.append(lines[j].split()[i])
            
            if(float(lines[j].split()[5])>0.5): 
                conf=float(lines[j].split()[5])
                width=float(lines[j].split()[3])
                height=float(lines[j].split()[4])
                area = width*height
                x_center = float(lines[j].split()[1])
                y_center = float(lines[j].split()[2])
                dist = np.sqrt(np.square(0.5-x_center)+np.square(0.5-y_center))
                info_list.append(area)
                info_list.append(dist)
                scores = 0.5*conf+0.3*area+0.2*(1-dist)
                info_list.append(scores)
        
        zip(info_list)
        with open(str('case90.csv'), 'a',newline="") as f:
            wr = csv.writer(f)
            wr.writerow(info_list)  
        info_list=[]
        

      



    


