from pytube import YouTube
from pytube import Search
import re
yt = YouTube("https://youtu.be/PjoSqv870b8?si=WZfrbWBjiFTqealJ")

print(yt.title)
print(yt.length)

# print(yt.streams)

pattern = r'(\w+)\s*=\s*"([^"]+)"'

for i in yt.streams:
    i = str(i)
    # Find all matches using the regex pattern
    matches = re.findall(pattern, i)
    
    # Convert the matches to a dictionary
    properties = {key: value for key, value in matches}
    print(properties['res'])
# pytube.StreamQuery.filter()
# print(yt.captions)

# we can download through streams
# stream = yt.streams.get_by_itag(22)
# stream.download()

s = Search('Tokyo Lens')
# print(s.results)
# for i in s.results:
#     print(i.title,i.views)
# print(s.completion_suggestions)