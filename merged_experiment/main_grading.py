import os.path as op
import os
import argparse
import numpy as np
import scipy.stats as ss
import pandas as pd
from psychopy import logging
from itertools import product
import yaml
from session import HCPMovieELSession,HCPMovieELSessionGrading

#load path from csv
#group_path =  '/Users/shufanzhang/Documents/PhD/Arrow_of_time/hcp_movie_eyetracking-main/movs/MomentsInTime/groups/' 
group_path = pd.read_csv('path.csv', header=None, index_col=0).loc['group_path'][1]
all_group_folders=os.listdir(group_path)
print(all_group_folders)
grading_setting_path_YBB = pd.read_csv('path.csv', header=None, index_col=0).loc['GradingsettingsTBB'][1]
grading_setting_path_MMTs = [op.join(group_path, group_folder, 'Gradingsettings.yml') for group_folder in all_group_folders if os.path.exists(op.join(group_path, group_folder, 'Gradingsettings.yml'))]
print(grading_setting_path_MMTs)


parser = argparse.ArgumentParser()
parser.add_argument('datasetnumber', default=0, nargs='?') #0-4 for MMTs, 5 for YBB
parser.add_argument('eyelink', default=False, nargs='?')



cmd_args = parser.parse_args()
datset_num,eyelink = cmd_args.datasetnumber, cmd_args.eyelink

datset_num = int(input('Please enter the dataset number (0-4 for MMTs, 5 for YBB): '))

if datset_num == 5: 
    setting_path = grading_setting_path_YBB
    output_str = 'YBB'
else:
    setting_path = grading_setting_path_MMTs[datset_num]
    output_str = 'MMT'+str(datset_num)

if eyelink:
    eyetracker_on = True
    logging.warn("Using eyetracker") 
else:
    eyetracker_on = False
    logging.warn("Using NO eyetracker")


session_object = HCPMovieELSessionGrading(output_str=output_str,
                            output_dir= op.join(group_path, 'output'),
                            settings_file=setting_path,
                            eyetracker_on=eyetracker_on)
session_object.create_trials()
logging.warn(f'Writing results to: {op.join(session_object.output_dir, session_object.output_str)}')
session_object.run()
session_object.close()
#session_object.save_results()








