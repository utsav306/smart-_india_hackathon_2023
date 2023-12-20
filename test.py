####CHANNEL ID 
from pytube import *
import os
from googleapiclient.discovery import build

# cid = YouTube('https://www.youtube.com/watch?v=5qtC-tsQ-wE').channel_id
# print(cid)

class YTStats():

    def __init__(self,api_key):
        #eself.channelId = channel_id
        self.apiKey = api_key 
        self.channel_stats = None
    
    
    # def get_channel_stats(self):
        
    #     url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channelId}&key={self.apiKey}'

    #     return url    


    def get_video_stats(self,video_ids):
        url = f"https://www.googleapis.com/youtube/v3/videos?id={video_ids}&key={self.apiKey}&part=snippet,contentDetails,statistics,status"

        return url
    

    def youtube_search_topic(api_key, query, max_results=10):
        # Set up the YouTube Data API
        youtube = build('youtube', 'v3', developerKey=api_key)

        # Call the search.list method to retrieve search results
        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',
            maxResults=max_results
        ).execute()

        # Extract video details from the search results
        videos = []
        for search_result in search_response.get('items', []):
            video = {
                'title': search_result['snippet']['title'],
                'video_id': search_result['id']['videoId'],
                'url': f'https://www.youtube.com/watch?v={search_result["id"]["videoId"]}'
            }
            videos.append(video)

        return videos    

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'AIzaSyAMtysCv1YSFqck6UOtdpZWYuZ1qzGGNWY'
search_query = 'Python programming tutorial'
search_results = youtube_search_topic(api_key, search_query)

# Print the search results
for result in search_results:
    print(f'Title: {result["title"]}')
    print(f'Video ID: {result["video_id"]}')
    print(f'URL: {result["url"]}')
    print('\n')

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
