import numpy as np
from PIL import ImageGrab
import cv2
import time
import tensorflow
import keras
from keras import layers

#from keypress import PressKey, ReleaseKey, UP_ARROW, RIGHT_ARROW, DOWN_ARROW, LEFT_ARROW
i = 0
printscreen = 0

def screen_record():
    last_time = time.time()
    while i < 1000:
        printscreen = np.array(ImageGrab.grab(bbox=(0,0,800,800)))
        #print(printscreen.shape)
        #print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow('window', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


model_1 = keras.Sequential()

screen_record()

cv2.imshow('window', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))

model_1.add(keras.layers.Dense(12), activation="relu")
model_1.add(keras.layers.Dense(24), activation="relu")
model_1.add(keras.layers.Dense(20), activation="relu")
model_1.add(keras.layers.Dense(18), activation="relu")
