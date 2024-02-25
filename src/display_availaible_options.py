# a fucntion to display availaible options for the user to donwload
from tabulate import tabulate

def display_availaible_options(video_set):
    print("Here are the different options available for download")

    # Display options with column headings
    headers = ['Resolution', 'File Size', 'itag']
    print(tabulate(video_set, headers=headers, tablefmt='pretty'))