import pandas as pd
import numpy as np
import os
import cv2
from PIL import Image
from scipy import misc
#import keras
import glob
import random
#Save Models Keras
#https://machinelearningmastery.com/save-load-keras-deep-learning-models/


#np.random.seed(7)

#import dataset
path = 1
print("Test")
image = misc.imread("Training Data/red1.png")
print(image)
print(image.shape)
print(image.dtype)
#model = keras.Sequential()
#model.add(keras.layers.Dense(12),activation="relu)
#model.add(keras.layers.Dense(24),activation="relu)
#model.add(keras.layers.Dense(20),activation="relu")
#model.add(keras.layers.Dense(18),activation="relu")

#save to Json
#save_results = model.to_json()