# function do be executed on finishing downloading
# but did not use since fucntionality already present in stream.download() API
import os
import shutil

def complete_function(stream, file_path):
    # Path to the current directory
    current_directory = '/Users/omdeshmukh/Downloads/Python-Automations/YouTube-Video-Downloader'

    # Path to the destination directory
    destination_directory = '/Users/omdeshmukh/Downloads/Python-Automations/YouTube-Video-Downloader/Downloaded_Videos'

    # Get a list of all files in the current directory
    files = os.listdir(current_directory)

    # Filter out directories and get the latest file based on its modification time
    latest_file = max([f for f in files if os.path.isfile(os.path.join(current_directory, f))], key=os.path.getmtime)

    # Move the latest file to the destination directory
    shutil.move(os.path.join(current_directory, latest_file), destination_directory)

    print(f"Moved {latest_file} to {destination_directory.split('/')[-1]}")