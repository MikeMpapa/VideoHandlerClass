import VideoHandler
from glob import glob

'''
vid = VideoHandler()

vid.SetCapture("/home/michalis/Documents/TRI_Stress/sample_data/N14_VideoMonologue1_closeup.avi")
vid.playbackVideo()

frames = vid.getVideoFrames(0)

print(frames)
'''


def loadVideosFromDir(path_to_data):
    dirs = glob(path_to_data)
    return dirs



if __name__ == "__main__":
    sample_paths = loadVideosFromDir("/home/michalis/Documents/TRI_Stress/sample_data/*avi")
    print (sample_paths)

    data_gray = []
    data_rgb = []
    videos = []
    for path in sample_paths:
        vid = VideoHandler.VideoHandler()
        vid.setCapture(path)
        vid.getVideoFrames('all')
        data_gray.append(vid.frames[-1])
        data_rgb.append(vid.frames[0])
        videos.append(vid)


    for video in videos:
         print (video.filename,'llllll')
         # print(video.getVideoDetails())

    VideoHandler.createVideo(data_rgb[0],'test_video_part','/home/michalis/Desktop/test_video/vids/',videos[0].frameWidth,videos[0].frameHeight)
    videos[0].saveFramesInDir('/home/michalis/Desktop/test_video/frames/')
    #VideoHandler.playbackFrames(data_rgb[0])

    pass

