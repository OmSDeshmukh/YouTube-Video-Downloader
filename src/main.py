from pytube import YouTube
from pytube import Search
from tabulate import tabulate

import sys
# Setting up the path to the project's main folder which contains all the packages
sys.path.append("/Users/omdeshmukh/Downloads/Python-Automations/YouTube-Video-Downloader")

from utils.convert_seconds_to_hms import convert_seconds_to_hms
from utils.progress_function import progress_function
from utils.process_stream import process_stream

# example input
# https://youtu.be/PjoSqv870b8?si=baxyqM22ITkR1-mB

link = input("Enter the youtube link you want to download")

try:
    yt = YouTube(link,allow_oauth_cache=True)
except:
    print("Incorrect Link")
    sys.exit(1)

print("Video Title:",yt.title)
hours, minutes, seconds = convert_seconds_to_hms(int(yt.length))

print("Video Length:",f"{hours} hours, {minutes} minutes, {seconds} seconds")

video_set = [] # for the streams that have a rsolution(the c)
temp=[]
for i in yt.streams.filter(progressive = True):
    properties = process_stream(i)
    temp.append(properties)
    
    try:
        video_set.append([properties['res'],properties['filesize'], properties['itag']])
    except:
        pass

print("Here are the different options available for download")

# Display options with column headings
headers = ['Resolution', 'File Size', 'itag']
print(tabulate(video_set, headers=headers, tablefmt='pretty'))

choice = 0
# Get user input
while(True):
    choice = input("Choose the tag number of the resolution you want to download")

    if(choice not in (i[2] for i in video_set)):
        print("itag does not exist")
        print("Please Renter")
    else:
        break
    
req_tags = [(a[2],a[1]) for a in video_set if a[2]==choice]
yt = YouTube(link,on_progress_callback=lambda chunk, file_handle, bytes_remaining: progress_function( chunk, file_handle, bytes_remaining, filesize=req_tags[0][1] ),use_oauth=True)

stream = yt.streams.get_by_itag(req_tags[0][0])
try:
    path_to_saved = stream.download(output_path = "Downloaded_Videos",filename_prefix = str(int(req_tags[0][1]))+"mb-")
    print("File saved at memory loaction",path_to_saved)
except:
    print("Error while downloading file")