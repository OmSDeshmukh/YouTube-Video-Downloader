# handles the input from the user
from pytube import YouTube

import sys
sys.path.append("/Users/omdeshmukh/Downloads/Python-Automations/YouTube-Video-Downloader")

from utils.convert_seconds_to_hms import convert_seconds_to_hms


def input_handling():
    link = input("Enter the youtube link you want to download")

    try:
        yt = YouTube(link,allow_oauth_cache=True)
    except:
        print("Incorrect Link")
        sys.exit(1)
    print("Video Title:",yt.title)
    hours, minutes, seconds = convert_seconds_to_hms(int(yt.length))

    print("Video Length:",f"{hours} hours, {minutes} minutes, {seconds} seconds")
    return yt, link