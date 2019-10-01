import argparse
import VideoHandler
from glob import glob

'''
vid = VideoHandler()

vid.SetCapture("/home/michalis/Documents/TRI_Stress/sample_data/N14_VideoMonologue1_closeup.avi")
vid.playbackVideo()

frames = vid.getVideoFrames(0)

print(frames)
'''

def ParseInputArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('datapath', type=str,help = 'path to video')
    parser.add_argument('out', type=str,help = 'path to extract frames')
    args = parser.parse_args()
    return args

def loadVideosFromDir(path_to_data):
    dirs = glob(path_to_data)
    return dirs



if __name__ == "__main__":
    args = ParseInputArguments()
    print (args.datapath)
    data_paths = loadVideosFromDir(args.datapath+'/*avi')

    #data_gray = []
    #data_rgb = []
    videos = []
    for path in data_paths:
        vid = VideoHandler.VideoHandler()
        vid.setCapture(path)
        vid.getVideoFrames('all')
        vid.saveFramesInDir(args.out)
        del vid

        #data_gray.append(vid.frames[-1])
        #data_rgb.append(vid.frames[0])
     #   videos.append(vid)


    #for video in videos:
        #video.saveFramesInDir('/home/mpapakos/Desktop/vidsASframes/')
        #print (video.filename,'llllll')
        # print(video.getVideoDetails())

    #VideoHandler.createVideo(data_rgb[0],'test_video_part','/home/mpapakos/Desktop/',videos[0].frameWidth,videos[0].frameHeight)
    #videos[0].saveFramesInDir('/home/mpapakos/Desktop/test_video/frames/')
    #VideoHandler.playbackFrames(data_rgb[0])

    pass

