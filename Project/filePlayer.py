#!/usr/bin/env python3
#@Author: Ethan Benckwitz

from threading import Thread
import cv2, os


class Exracting(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.vidcap = cv2.VideoCapture('clip.mp4')
        self.count =  0

    def run(self):
        #read one frame
        success, image = self.vidcap.read()
        while success and self.count < 72:
            #put frames in queue

            success, image = self.vidcap.read()
            print(f'Reading frame {count}')
            count += 1
        print('Extracting is done!')

class ConvertGray(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.count = 0

    def run(self):
        while True:

            #receive queue frames
            print('Converting frame (self.count}')
            grayscaleFrame = cv2.cvtColor(frame??, cv2.COLOR_BGR2GRAY)
            self.count += 1
        print('Converting to gray done!')

class display(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.count = 0

    def run(self):
        while True:
            print(f'Displaying Frame{self.count}')
            #Display frame in window as 'Video'
            cv2.imshow('Video', frame???)

            #wait for 42ms and check if user wants to quit
            if(cv2.waitKey(42) and 0xFF == ord("q"):
               break

            self.count += 1
        print('Finished with display!')
        #make sure we cleanup the windows!
        cv2.destroyAllWindows()
        
