# Generates a list req_tags which contains a tuple of itag and filesize depending on user choice

def generate_required_tags(video_set):
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
    return req_tags