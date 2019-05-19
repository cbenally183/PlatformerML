import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32api

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

#Scan Code                          Hardware Code
NextTrack       = 0xB0              #25
PrevTrack       = 0xB1              #16
PlayPauseMedia  = 0xB3              #34
VolUp           = 0xAF              #48
VolDown         = 0xAE              #49
MuteSound       = 0xAD              #32
UpKey           = 0x26              #72
DownKey         = 0x28              #80
RightKey        = 0x27              #77
LeftKey         = 0x25              #75

#For getting the Hardware Code
hwcode = win32api.MapVirtualKey(LeftKey,0)
print(f'Hardware Code: {hwcode}')


#Just simple interface
def controlMedia(a):
    if a == 'a':
        win32api.keybd_event(PlayPauseMedia, 34)
    if a == 'b':
        win32api.keybd_event(NextTrack, 25)
    if a == 'c':
        win32api.keybd_event(PrevTrack, 16)
    if a == 'd':
        win32api.keybd_event(VolUp, 48)
    if a == 'e':
        win32api.keybd_event(VolDown, 49)
    if a == 'f':
        win32api.keybd_event(MuteSound, 32)
    if a == 'g':
        win32api.keybd_event(UpKey, 72)
    if a == 'h':
        win32api.keybd_event(DownKey, 80)
    if a == 'i':
        win32api.keybd_event(RightKey, 77)
    if a == 'j':
        win32api.keybd_event(LeftKey, 75)
#screen_record()

while True:
    controlMedia('j')

