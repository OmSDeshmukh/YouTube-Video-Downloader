# to process a stream
import re

def process_stream(i):
    i_filesize = i.filesize
    i = str(i)
    pattern = r'(\w+)\s*=\s*"([^"]+)"'
    matches = re.findall(pattern, i)
    properties = {key: value for key, value in matches}
    properties['filesize'] = i_filesize
    return properties