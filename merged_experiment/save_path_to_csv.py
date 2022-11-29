import csv
import os
import pandas as pd
import sys

path_dict = {
    'group_path': '/Users/shufanzhang/Documents/PhD/Arrow_of_time/hcp_movie_eyetracking-main/movs/MomentsInTime/groups/',
    'setting_temp': '/Users/shufanzhang/Documents/PhD/Arrow_of_time/hcp_movie_eyetracking-main/experiment/settings_temp.yml',
    'all_originals': '/Users/shufanzhang/Documents/PhD/Arrow_of_time/hcp_movie_eyetracking-main/movs/MomentsInTime/all_originals/',
    'target_path': '/Users/shufanzhang/Documents/PhD/Arrow_of_time/hcp_movie_eyetracking-main/movs/MomentsInTime/',
}


path_dict2 = {
    'group_path': '/Users/shufanzhang/Documents/PhD/Arrow_of_time/hcp_movie_eyetracking-main/movs/MomentsInTime/groups/',
    'setting_temp': '/Users/shufanzhang/Documents/PhD/Arrow_of_time/hcp_movie_eyetracking-main/experiment/settings_temp.yml',
    'MMT_originals': '/Users/shufanzhang/Documents/PhD/Arrow_of_time/hcp_movie_eyetracking-main/movs/MomentsInTime/all_originals/',
    'TBB_originals': '/Users/shufanzhang/Documents/PhD/Arrow_of_time/hcp_movie_eyetracking-main/movs/YouTubeBB/',
    'target_path': '/Users/shufanzhang/Documents/PhD/Arrow_of_time/hcp_movie_eyetracking-main/movs/MomentsInTime/',
    'MMT_originals_settings': '/Users/shufanzhang/Documents/PhD/Arrow_of_time/hcp_movie_eyetracking-main/movs/MomentsInTime/all_originals/settings.yml',
    'TBB_originals_settings': '/Users/shufanzhang/Documents/PhD/Arrow_of_time/hcp_movie_eyetracking-main/movs/YouTubeBB/settings.yml',
    'GradingsettingsTBB': '/Users/shufanzhang/Documents/PhD/Arrow_of_time/hcp_movie_eyetracking-main/movs/YouTubeBB/Gradingsettings.yml',
}

def save_path_to_csv(path_dict):
    df = pd.DataFrame.from_dict(path_dict, orient='index')
    df.to_csv('path.csv')

if __name__=='__main__':
    save_path_to_csv(path_dict2)







