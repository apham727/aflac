# Instrument Classification:
Problem: Given a dataset of 2700 training files with unverified labels, predict the classification of the test data.

## Solution: CNN with XGBoost Pre-processing:

### XGBoost & Random Forest Classifiers:
In order to be able to classify the wav files in an accurate manner, a two-stage process was taken for this problem. To fix label noise, we started with a Random Forest /  XGBoost classifier to reverify the labels in the training dataset. For the reverification of the data, we created a dataframe using Librosa of the MFCC's, zero-crossing rate, spectral centroids, and other features from the melspectrogram of each wav file. No pre-processing was done on the wav files before creating the melspectrograms. 
train on the verified labels of the training data (roughly 60% of the training data) then predict the real/correct label of the training data with this model. 


