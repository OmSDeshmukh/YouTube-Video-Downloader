from pytube import YouTube
from pytube import Search
from utils.complete_function import complete_function
from utils.progress_function import progress_function
from utils.convert_seconds_to_hms import convert_seconds_to_hms
import re
import sys


pattern = r'(\w+)\s*=\s*"([^"]+)"'



link = input("Enter the youtube link you want to download")

yt = YouTube(link,on_progress_callback = progress_function,on_complete_callback = complete_function,use_oauth=True)

print("Title",yt.title)
hours, minutes, seconds = convert_seconds_to_hms(int(yt.length))

print("Length:")
print(f"{hours} hours, {minutes} minutes, {seconds} seconds")


print("Here are the different options available for download")
res_set = []
temp=[]
for i in yt.streams.filter(progressive=True):
    i_filesize = i.filesize
    i = str(i)
    
    # Find all matches using the regex pattern
    matches = re.findall(pattern, i)
    
    # Convert the matches to a dictionary
    properties = {key: value for key, value in matches}
    properties['filesize'] = i_filesize
    # print(properties.keys())
    temp.append(properties)
    
    try:
        res_set.append(properties['res'])
    except:
        pass

print(type(temp[0]))
print(set(res_set))
res = input("Enter the resolution you want to download in")


req_tags = [(props['itag'],props['filesize']) for props in temp if props['res'] == res]
# print(req_tags)
# req_tags = ['22']
yt = YouTube(link,on_progress_callback=lambda chunk, file_handle, bytes_remaining: progress_function( chunk, file_handle, bytes_remaining, req_tags[0][1] ),on_complete_callback = complete_function,use_oauth=True)

stream = yt.streams.get_by_itag(req_tags[0][0])
# global filesize;
# = stream.filesize
stream.download()


# first implement progressive(audio and video) donwload
# Then implement the not progressive ones where audio and video downloaded separately and joint together
# all this since progressive ones are allowed only <=720p

# Then comes quering the required resolution

# also have to work on authentication