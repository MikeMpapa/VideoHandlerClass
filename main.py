from VideoHandler import VideoHandler
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
    file_details = []
    for path in sample_paths:
        vid = VideoHandler()
        file_details.append(vid.SetCapture(path))
        frames = vid.getVideoFrames('all')
        data_gray.append(frames[-1])
        data_rgb.append(frames[0])

    for details in file_details:
         print (details)
         # print(video.getVideoDetails())


    pass

