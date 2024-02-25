from pytube import YouTube
# from pytube import Search
from tabulate import tabulate

from input_handling import input_handling
from generate_video_set import generate_video_set
from download_handler import download_handler
from display_availaible_options import display_availaible_options
from generate_required_tags import generate_required_tags

# example input
# https://youtu.be/PjoSqv870b8?si=baxyqM22ITkR1-mB


yt, link = input_handling()
video_set = generate_video_set(yt)
display_availaible_options(video_set)
req_tags = generate_required_tags(video_set)
download_handler(link, req_tags)