# Instrument Classification:
Problem: Given a dataset of 2700 training files with unverified labels, predict the classification of the test data.

## Solution: CNN with XGBoost Pre-processing:

### XGBoost & Random Forest Classifiers:
In order to be able to classify the wav files in an accurate manner, a two-stage process was taken for this problem. To fix label noise, we started with a Random Forest /  XGBoost classifier to reverify the labels in the training dataset. For the reverification of the data, we created a dataframe using Librosa of the MFCC's, zero-crossing rate, spectral centroids, and other features from the melspectrogram of each wav file. No pre-processing was done on the wav files before creating the melspectrograms. We then trained on the verified labels of the training data (roughly 60% of the training data) and predicted the real/correct label of the training data with each model. We obtained 75.3% accuracy with the Random Forest Classifier and 80.1% with the XGBoost model which increased our confidence in the unverified labels (the given accuracy of the unverified labels was 60-70% correct). 

### CNN:
After reverifying the labels from training set, we created melspectrograms for each wav file in the training and testing data sets. These were then passed through a CNN with the reverified labels. For the CNN, typical network architecture was created at first and then parameters were optimized through trial and error. The network architecture cna be seen in the model below. 

### Results:
With the combination of reverification of labels of the training set with a simple classifier and then predictions on testing with the CNN we were able to achieve 90% accuracy on test data. 

