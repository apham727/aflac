#!/usr/bin/python
import os
import numpy as np
import glob
from scipy.io import wavfile
from fractions import Fraction
import copy
from scipy import signal
import pandas as pd

"""
This script performs resampling of .wav files to 440Hz. The goal of this resampling was to center spectral content around 440Hz while preserving harmonic spacing unique to each label. This script works concurrently with the provided file top_block_resample.py

"""

os.chdir('/home/duncan/Documents/ML_Project/rice-elec301-f19/301-project.audio_test/LPF_Test_Files_7kHz')

A_440 = 440.0

start_path = '/home/duncan/Documents/ML_Project/rice-elec301-f19/301-project.audio_test/LPF_Test_Files_7kHz/'

end_path = '/home/duncan/Documents/ML_Project/rice-elec301-f19/301-project.audio_test/LPF_Test_Files_7kHz_resamp/'



list_of_files = glob.glob('*.wav')
cnt = 0
out_list = []
for file in list_of_files:
    print file
    print cnt
    cnt += 1
    fs, data = wavfile.read(file)

    spectrum = np.abs(np.fft.fft(data))**2
    spectrum_copy = copy.deepcopy(spectrum)
    #Seems that we may also have a DC offset...
    #Get rid of the DC offset...
    spectrum[0] = 0
    #spectrum[11025:] = 0
    spectrum[8000:] = 0
    #Calculate fundamental linear frequency...
    maximum_idx = np.argmax(spectrum)

    linear_freq = int((fs / 2.0) * (maximum_idx / 22050.0))


    resample_fraction = Fraction(str(A_440 / linear_freq)).limit_denominator()

    #print resample_fraction.numerator
    #print resample_fraction.denominator

    denominator = str(resample_fraction.denominator)
    numerator = str(resample_fraction.numerator)
 
    os.system('/home/duncan/Documents/ML_Project/top_block_resample.py --input-filepath ' + start_path + file + ' --output-filepath ' + end_path + file + ' --frac-dem ' + denominator + ' --frac-num ' + numerator)
    

