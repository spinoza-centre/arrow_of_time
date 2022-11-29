import sys
import os
import ffmpeg
import pandas as pd

group_path =  pd.read_csv('path.csv', header=None, index_col=0).loc['group_path'][1]
all_group_folders=os.listdir(group_path)


#create final videos from streched videos for one group
def create_final4for1(group_folder):
    streched_path = group_path+group_folder+'/stretched_videos'
    final_path = group_path+group_folder+'/final_videos' 
    #create final_videos folder for one group
    os.mkdir(final_path)
    all_streched_videos = os.listdir(streched_path)
    #create final videos for one group(duplicate each video))   
    for streched_video in all_streched_videos:
        if streched_video.endswith('.mp4'):
            #get final video
            (
                ffmpeg
                .input(streched_path+'/'+streched_video)
                .output(final_path+'/'+'1_'+streched_video)
                .run()
            )
            (
                ffmpeg
                .input(streched_path+'/'+streched_video)
                .output(final_path+'/'+'2_'+streched_video)
                .run()
            )
       
def create_final4forAll():
    for group_folder in all_group_folders:
        if os.path.isdir(group_path+group_folder):
            create_final4for1(group_folder)

if __name__=='__main__':
    create_final4forAll()