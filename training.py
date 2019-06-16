import pandas as pd
import numpy as np
import os
import cv2
from PIL import Image
#import keras

#Save Models Keras
#https://machinelearningmastery.com/save-load-keras-deep-learning-models/


np.random.seed(7)

#import dataset
image = Image.open("Training Data/red1.png")
cv2.imshow('window', image)
model = keras.Sequential()
model.add(keras.layers.Dense(12),activation="relu)
model.add(keras.layers.Dense(24),activation="relu)
model.add(keras.layers.Dense(20),activation="relu")
model.add(keras.layers.Dense(18),activation="relu")

#save to Json
save_results = model.to_json()
