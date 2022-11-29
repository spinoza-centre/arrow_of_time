import sys
import os
import random
import ffmpeg
import pandas as pd

#traverse the videos in all folder and copy them into all_original folder
def one_folder():
    #load path from csv
    group_path =  pd.read_csv('path.csv', header=None, index_col=0).loc['group_path'][1]
    target_path = pd.read_csv('path.csv', header=None, index_col=0).loc['target_path'][1]
    count_folder=1

    for content in os.listdir(target_path):
        if os.path.isdir(target_path+'/'+content) and content!='all_originals':
            count_folder+=1
            all_sub_content=os.listdir(target_path+'/'+content)
            for sub_content in all_sub_content:
                if sub_content.endswith('.mp4'):
                    #copy videos to all_originals folder
                    os.system('cp '+target_path+'/'+content+'/'+sub_content+' '+target_path+'/all_originals/')



if __name__=='__main__':
    one_folder()


