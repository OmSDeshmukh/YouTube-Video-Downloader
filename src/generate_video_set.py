# Generates all the video information such as itags, resolution and file size
# to be provided to the user for download

import sys
sys.path.append("/Users/omdeshmukh/Downloads/Python-Automations/YouTube-Video-Downloader")

from utils.process_stream import process_stream

# takes in youtube object as parameter input
def generate_video_set(yt):
    video_set = [] # for the streams that have a resolution(the c)
    temp=[]
    for i in yt.streams.filter(progressive = True):
        properties = process_stream(i)
        temp.append(properties)
        
        try:
            video_set.append([properties['res'],properties['filesize'], properties['itag']])
        except:
            pass
    
    return video_set