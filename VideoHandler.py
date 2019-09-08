import numpy
import cv2
from os import path

class CustomError(Exception):
    pass

class VideoHandler:

    def __init__(self):
        self.video = cv2.VideoCapture()
        self.supported_formats=['mp4','avi']


    def SetCapture(self,video_input):
        '''
        :param video_input: path to video file OR camera id for live capturing
        :return: 0 if capture OR details as [frameCount,frameWidth,frameHeight,filename] if file
        '''

        if type(video_input) == str:
            if path.exists(video_input) and video_input.split('/')[-1].split('.')[-1] in self.supported_formats:
                self.video = cv2.VideoCapture(video_input)
                info = self.getVideoDetails()
                info.append(video_input.split('/')[-1])
            else:
                print ('\nInvalid Input: Path '+video_input+' does not exist or file format is not supported. Please use one the following formats: ',self.supported_formats)
                raise ValueError
        else:
            info = 0
        return info


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

    def getVideoDetails(self):
        '''
        Return video statistics as a list [frameCount,frameWidth,frameHeight]
        :return:
        '''
        frameCount = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        frameWidth = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        frameHeight = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        return [frameCount,frameWidth,frameHeight]








