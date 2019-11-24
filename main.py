import os, json, re, urllib.request
from pytube import YouTube

api_key = os.environ.get('API_KEY')

video_id = "g_PVrBGStBI"  #ZkYOvViSx3E

url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"

json_url = urllib.request.urlopen(url)
data = json.loads(json_url.read())

print(data)
