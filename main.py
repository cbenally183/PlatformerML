import numpy as np
from PIL import ImageGrab
import cv2
import time
import tensorflow
import keras
from keras import layers

#from keypress import PressKey, ReleaseKey, UP_ARROW, RIGHT_ARROW, DOWN_ARROW, LEFT_ARROW
def screen_record():
    last_time = time.time()
    while(True):
        printscreen = np.array(ImageGrab.grab(bbox=(0,0,600,600)))
        print(printscreen.shape)
        #print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow('window', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


#start recording
screen_record()
model_1 = keras.Sequential()
model_1.add(layers.Dense(64, activation='relu', input_dim=600))
#Hidden Layers
model_1.add(layers.Dense(64, activation='relu'))
model_1.add(layers.Dense(64, activation='relu'))
model_1.add(layers.Dense(64, activation='relu'))
#output for four directions
model_1.add(layers.Dense(4, activation='softmax'))


