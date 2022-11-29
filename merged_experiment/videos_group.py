import sys
import os
import numpy as np
import pandas as pd
import random

#traverse the videos in all folder and randomly copy them to n groups
def videosDispatch(n):
    #load path from csv
    group_path =  pd.read_csv('path.csv', header=None, index_col=0).loc['group_path'][1]
    all_originals_path = pd.read_csv('path.csv', header=None, index_col=0).loc['all_originals'][1]
    all_content=os.listdir(all_originals_path)
    print(len(all_content))
    random.shuffle(all_content)
    print(all_content)
    for i in range(n):
        os.mkdir(group_path+'group'+str(i+1))
    
    #uniformly distribute videos to n groups
    for i in range(len(all_content)):
        os.system('cp '+all_originals_path+'/'+all_content[i]+' '+group_path+'group'+str((i%n)+1)+'/')
    


if __name__=='__main__':
    videosDispatch(5)