import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.io import wavfile

"""
The following script performs a PCA visualization of length 22050 FFTs of all
.wav files in a given directory. In it's current state, the code will create
a pca representation of all test .wav files located in the directory:

    E:\Fall2019\ELEC301\ML_Project\301-project.audio_test\301-project.audio_test

"""

os.chdir(r"E:\Fall2019\ELEC301\ML_Project\301-project.audio_test\301-project.audio_test")

list_of_files = glob.glob('*.wav')

big_lists = []
file_names = []
for file in list_of_files:
    print(file)
    fs, data = wavfile.read(file)
    transform = list(abs(np.fft.fft(data,22050)))
    big_lists.append(transform)
    file_names.append(file)
    
####################################################
#Now do pca on the big_lists
x = StandardScaler().fit_transform(big_lists)

#Plot only in 2-D
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)



z = principalComponents[:,0]
y = principalComponents[:,1]
fig, ax = plt.subplots()
ax.scatter(z,y)

#Label each point with the corresponding file name...
for i, txt in enumerate(file_names):
    ax.annotate(txt, (z[i], y[i]))