import os.path as op
import os
import argparse
import numpy as np
import scipy.stats as ss
import pandas as pd
from psychopy import logging
from itertools import product
import yaml
from session import HCPMovieELSession

#load path from csv
#group_path =  '/Users/shufanzhang/Documents/PhD/Arrow_of_time/hcp_movie_eyetracking-main/movs/MomentsInTime/groups/' 
group_path = pd.read_csv('path.csv', header=None, index_col=0).loc['group_path'][1]
#folder should not be output
all_group_folders= [folder for folder in os.listdir(group_path) if folder != 'output' and folder != '.DS_Store']
print(all_group_folders)


parser = argparse.ArgumentParser()
parser.add_argument('subject', default=None, nargs='?')
parser.add_argument('run', default=None, nargs='?')
parser.add_argument('eyelink', default=False, nargs='?')

cmd_args = parser.parse_args()
subject, run, eyelink = cmd_args.subject, cmd_args.run, cmd_args.eyelink


if subject is None:
    subject = input('Subject? (5): ')
    subject = 5 if subject == '' else subject

if run is None:
    run = input('Run? (10): ')
    run = 10 if run == '' else run
elif run == '10':
    run = 10


if eyelink:
    eyetracker_on = True
    logging.warn("Using eyetracker")
else:
    eyetracker_on = False
    logging.warn("Using NO eyetracker")

group_number = subject
session_number = run


output_str = f'sub-{subject}_run-{run}_task-movie'
#load settings from the yaml file accourding to the group number and session number
setting_path = group_path+all_group_folders[int(group_number)-1]+'/settings'+str(session_number)+'.yml'

session_object = HCPMovieELSession(output_str=output_str,
                        output_dir=None,
                        settings_file=setting_path,
                        eyetracker_on=eyetracker_on)
session_object.create_trials()
logging.warn(f'Writing results to: {op.join(session_object.output_dir, session_object.output_str)}')
session_object.run()
session_object.close()





