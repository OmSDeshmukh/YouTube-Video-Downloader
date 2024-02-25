# Handles downloading of the files depending on user choice
from pytube import YouTube

import sys
sys.path.append("/Users/omdeshmukh/Downloads/Python-Automations/YouTube-Video-Downloader")

from utils.progress_function import progress_function


def download_handler(link, req_tags):
    yt = YouTube(link,on_progress_callback=lambda chunk, file_handle, bytes_remaining: progress_function( chunk, file_handle, bytes_remaining, filesize=req_tags[0][1] ),use_oauth=True)

    stream = yt.streams.get_by_itag(req_tags[0][0])
    try:
        path_to_saved = stream.download(output_path = "/Users/omdeshmukh/Downloads/Python-Automations/YouTube-Video-Downloader/Downloaded_Videos",filename_prefix = str(int(req_tags[0][1]))+"mb-")
        print("File saved at memory loaction",path_to_saved)
    except:
        print("Error while downloading file")
        sys.exit(1)