import numpy
import cv2

class VideoHandler:

    def __init__(self):
        self.video = cv2.VideoCapture()

    def SetCapture(self,video_input):
        '''
        :param video_input: path to video file OR camera id for live capturing
        :return:
        '''
        self.video = cv2.VideoCapture(video_input)
        return 0


    def getVideoFrames(self,flag='all'):
        '''
        :param flag: Which set of frames to return - 0:All (Default), 1:RGB, 2:Grayscale
        :return: list of lists cointaing the sequence of RGB frames --> frames[0] and Gray frames-->frames[1]==frames[-1]
        '''
        frames = []
        if  flag=='all':frames = [[],[]]
        count = 0
        while (self.video.isOpened()):
            ret, frame = self.video.read()
            count+=1
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if flag=='all' or flag=='gray':
                frames[-1].append(gray)
            if flag == 'all' or flag == 'rgb':
                frames[0].append(frame)
            if count==10:
                break
        self.video.release()
        return frames


    def playbackVideo(self,):
        '''
        playback a VideoHandler Object
        :return:
        '''
        while (self.video.isOpened()):
            ret, frame = self.video.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.release()
        cv2.destroyAllWindows()
        return 0








