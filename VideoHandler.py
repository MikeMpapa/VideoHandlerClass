import cv2
from os import path,makedirs
from tqdm import tqdm
global supported_formats
supported_formats = ['mp4','avi']

class VideoHandler:

    def __init__(self):
        self.video = cv2.VideoCapture()
        self.video_input = None
        self.frameCount = None
        self.frameWidth = None
        self.frameHeight = None
        self.filename = None
        self.frames = []


    def setCapture(self,video_input):
        '''
        Set video input, load video and retrieve video details
        :param video_input: path to video file OR camera id for live capturing
        :return:
        '''
        if type(video_input) == str:
            if path.exists(video_input) and video_input.split('/')[-1].split('.')[-1] in supported_formats:
                self.video = cv2.VideoCapture(video_input)
                self.getVideoDetails()
                self.filename = video_input.split('/')[-1]
            else:
                print ('\nInvalid Input: Path '+video_input+' does not exist or file format is not supported. Please use one the following formats: ',supported_formats)
                raise ValueError
        else:
            info = 0
        self.video_input = video_input
        return


    def getVideoFrames(self,toExtract='all'):
        '''
        Extract frames from video and store as: self.frames[rgb_frmes,gray_frame]
        :param toExtract: Which set of frames to return - 0:All (Default), 1:RGB, 2:Grayscale
        :return:
        '''

        toExtract = toExtract.lower()
        frames = [[],[]]

        while (self.video.isOpened()):
            ret, frame = self.video.read()
            if frame is None:
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if toExtract=='all' or toExtract=='gray':
                frames[-1].append(gray)
            if toExtract == 'all' or toExtract == 'rgb':
                frames[0].append(frame)
        if not frames[0]: frames == frames[-1]
        if not frames[-1]: frames == frames[0]
        self.video.release()
        self.frames = frames
        print("Video information have been updated to its accurate value")
        self.getVideoDetails()
        return



    def playbackVideo(self,):
        '''
        Playback a VideoHandler Object
        :return:
        '''
        while (self.video.isOpened()):
            ret, frame = self.video.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.release()
        cv2.destroyAllWindows()
        return


    def getVideoDetails(self):
        '''
        Retrieve Video Statistics
        :return:
        '''
        if not self.frames:
            self.frameCount = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        else:
            self.frameCount = max(len(self.frames[0]),len(self.frames[-1]))
        self.frameWidth = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frameHeight = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        return


    def saveFramesInDir(self,save_path,toExtract='all'):
        '''
        Saves video frames into a given dit
        :param save_path: path to save frames
        :param toExtract: Which set of frames to return - 0:All (Default), 1:RGB, 2:Grayscale
        :return:
        '''

        toExtract = toExtract.lower()
        if not self.frames:
            self.getVideoFrames(toExtract)
        print ('Extract Frames for',self.filename,'Total number of frames:',self.frameCount)
        if toExtract=='all' or toExtract=='gray':
            if not path.exists(save_path+'/gray/'):
                makedirs(save_path+'/gray/')
            for idx,im in tqdm(enumerate(self.frames[-1])):
                cv2.imwrite(save_path+'/gray/'+str(idx)+'.png',im)
        if toExtract=='all' or toExtract=='rgb':
            if not path.exists(save_path + '/rgb/'):
                makedirs(save_path+'/rgb/')
            for idx,im in tqdm(enumerate(self.frames[0])):
                cv2.imwrite(save_path+'/rgb/'+str(idx)+'.png',im)
        return




def createVideo(data,filename,save_path,width,height,format='mp4',fps=30):
        '''
        Creates and stores a video from a list of images

        :param data: list of images
        :param filename: output file name
        :param save_path: dir to save the file
        :param width: frame width
        :param height: frame height
        :param format: avi Or mp4 (Default--> mp4)
        :param fps: frames per second (Default--> 25)
        :return:
        '''
        codecs=['mp4v','XVID']
        full_path=save_path+filename+'.'+format
        if not path.exists(save_path):
            makedirs(save_path)

        try:
            is_codec = codecs[supported_formats.index(format)]
            print (is_codec)
            codec = cv2.VideoWriter_fourcc(*is_codec)
        except:
            print('Invalis Video Format. Choose one from:',supported_formats)

        video = cv2.VideoWriter(full_path, codec, fps, (width, height))
        for image in data:
            video.write(image)
        return


def playbackFrames(data):
        '''
        Playback a list of frames
        :return:
        '''
        for image in data:
            cv2.imshow('frame', image)
            cv2.waitKey(0.5)
        return




