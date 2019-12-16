#!/usr/bin/python

import re
import os
import glob

"""
The following script performs low pass filtering on .wav files in conjuction with the top_block_lpf.py script. The LPF was implemented using GNU radio companion
"""


os.chdir('/home/duncan/Documents/ML_Project/rice-elec301-f19/301-project.audio_test/301-project.audio_test')

start_path = '/home/duncan/Documents/ML_Project/rice-elec301-f19/301-project.audio_test/301-project.audio_test/'

end_path = '/home/duncan/Documents/ML_Project/rice-elec301-f19/301-project.audio_test/LPF_Test_Files_7kHz/'

#Get list of files...
list_of_files = glob.glob('*.wav')

os.chdir('/home/duncan/Documents/ML_Project')

for file_name in list_of_files:
    print(file_name)
    #os.system('./top_block.py --input-filepath ' + start_path + file_name + '  --output-filepath ' + end_path + file_name)
    my_str = './top_block.py --input-filepath ' + start_path + file_name + '  --output-filepath ' + end_path + file_name
    os.system(my_str)
