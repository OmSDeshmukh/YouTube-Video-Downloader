# to process a stream into a dictionary
import re

def process_stream(i):
    i_filesize = i.filesize_mb
    i = str(i)
    pattern = r'(\w+)\s*=\s*"([^"]+)"'
    matches = re.findall(pattern, i)
    properties = {key: value for key, value in matches}
    properties['filesize'] = i_filesize
    return properties