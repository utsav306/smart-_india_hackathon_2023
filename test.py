####CHANNEL ID 
from pytube import *

# cid = YouTube('https://www.youtube.com/watch?v=5qtC-tsQ-wE').channel_id
# print(cid)

class YTStats():

    def __init__(self,api_key):
        #self.channelId = channel_id
        self.apiKey = api_key 
        self.channel_stats = None
    
    
    # def get_channel_stats(self):
        
    #     url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channelId}&key={self.apiKey}'

    #     return url    


    def get_video_stats(self,video_ids):
        url = f"https://www.googleapis.com/youtube/v3/videos?id={video_ids}&key={self.apiKey}&part=snippet,contentDetails,statistics,status"

        return url



'''getting video ids of of urls'''


# URL_PLAYLIST = input("Enter Playlist Url")

# # Retrieve URLs of videos from playlist
# playlist = Playlist(URL_PLAYLIST)
# print("Number Of Videos In playlist:",len(playlist.video_urls))

# urls = []
# for url in playlist:
#     urls.append(url)

# for i in urls:
#     vId = extract.video_id(i)
#     print(vId)
