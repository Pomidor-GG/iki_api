import os, json, re, urllib.request
from pytube import YouTube

api_key = os.environ.get('API_KEY')
channel_id = "UCJymPbg-0_yc-63wqc0WtIQ"
twelve_videos = []
list_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&maxResults=12&order=date&type=video&key={api_key}"

json_url = urllib.request.urlopen(list_url)
data = json.loads(json_url.read())
for i in data['items']:
    twelve_videos.append(i['snippet']['thumbnails']['medium']['url'])
print(twelve_videos)
