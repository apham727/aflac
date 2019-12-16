import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


"""
The following script creates a KNN model using shortened, resampled length 22050 FFTs of all
training files. This file uses SKLearn's implementation of KNN.
"""

#Import the combined training and meta csv
train_data = pd.read_csv(r"E:\Fall2019\ELEC301\ML_Project\ProcessedTrainingAndMeta.csv",index_col = 0)

train_data = train_data.dropna()
train_data = train_data[train_data.manually_verified !=0]


#Import the X_test data
test_data = pd.read_csv(r"E:\Fall2019\ELEC301\ML_Project\Test_File_Work\LPF_Test_Files_Shortened_Resampled\LPF_Test_Files_Shortened_Resampled\FFT_Test_Set.csv",index_col = 0,header=None)


#Separate out into X_train, Y_train and X_train...

X_train = train_data.iloc[:,0:-2]

y_train = train_data['label']

X_test = test_data

#Scale the data
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#Make the KNN model

classifier = KNeighborsClassifier(n_neighbors=15)
classifier.fit(X_train, y_train)


#Predict on the test files using the model
y_pred = classifier.predict(X_test)

y_predictions = pd.Series(y_pred,index=test_data.index)
y_predictions.index.name = 'fname'

y_predictions = y_predictions.to_frame()
y_predictions.columns = ['label']

#Save output predictions to a csv file
y_predictions.to_csv('KNNPredictions.csv')








