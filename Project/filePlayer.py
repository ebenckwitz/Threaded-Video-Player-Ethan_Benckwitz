#!/usr/bin/env python3
#@Author: Ethan Benckwitz

import threading 
import cv2, os, base64, queue
import numpy as np

class QueueThread:
    def __init__(self):
        self.queue = []
        self.full = threading.Semaphore(24)
        self.empty = threading.Semaphore(0)
        self.lock = threading.Lock()

    def enqueue(self, item):
        self.empty.acquire()
        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        self.full.release()

    def dequeue(self):
        self.full.acquire()
        self.lock.acquire()
        frame = queue.pop(0)
        self.lock.release()
        self.empty.release()
    
def exracting(filename, cframes):
    count =  0 #Initialize frame count

    #open video file
    vidcap = cv2.VideoCapture(filename)

    #read first image
    success, image = vidcap.read()
    
    print(f'Reading frame {count} {success}')
    while success and count < 72:
        #put frames in queue
        cframes.enqueue(image)

        success, image = vidcap.read()
        print(f'Reading frame {count}')
        count += 1
        
    print('Extracting is done!')

def convertGray(cframes, gframes):
    count = 0 #Initialize frame count

    #going through color frames
    while not cframes.empty():
        #receive queue frames
        print('Converting frame {count}')

        #get frames
        getFrame = cframes.dequeue()

        #convert to grayscale
        grayscaleFrame = cv2.cvtColor(getFrame, cv2.COLOR_BGR2GRAY)

        #put gray frames in queue
        gframes.enqueue(grayscaleFrame)
        
        count += 1

    print('Converting to gray done!')

def display(gframes):
    count = 0 #Initialize frame count

    #going through gray frames
    while not gframes.empty():
        print(f'Displaying Frame{count}')

        #get next frame
        frame = gframe.dequeue()

        #display image called Video
        cv2.imshow('Video', frame)
        #wait for 42ms before next frame
        if(cv2.waitKey(42) and 0xFF == ord("q"):
           break

        count += 1

    print('Finished with display!')
    #make sure we cleanup the windows!
    cv2.destroyAllWindows()

#filename to load
filename = '../clip.mp4'

#make queues
cframes = QueueThread()
gframes = QueueThread()
'''
make each thread target each def with their parameters as the args 
'''
extractThread = threading.Thread(target = extract, args = (filename, cframes))
convertThread = threading.Thread(target = convertGray, args = (cframes, gframes))
displayThread = threading.Thread(target = display, args = (gframes,))

#start each thread
extractThread.start()
convertThread.start()
displayThread.start()
        
