import numpy as np
from PIL import ImageGrab
import cv2
import time
from keypress import PressKey, ReleaseKey, UP_ARROW, RIGHT_ARROW, DOWN_ARROW, LEFT_ARROW
def screen_record():
    last_time = time.time()
    while(True):
        printscreen = np.array(ImageGrab.grab(bbox=(0,40,1280,720)))
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow('window', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
#screen_record()
time.sleep(4)
PressKey(RIGHT_ARROW)
PressKey(UP_ARROW)
ReleaseKey(UP_ARROW)
time(1)


