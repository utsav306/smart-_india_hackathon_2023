
###-----------------code for finding the time for the video clicked-------------------------------

# def time_parse(str_time):
#     import re

#     # Extract hours, minutes, and seconds using regular expressions
#     hours = int(re.search(r'(\d+)H', str_time).group(1)) if 'H' in str_time else 0
#     minutes = int(re.search(r'(\d+)M', str_time).group(1)) if 'M' in str_time else 0
#     seconds = int(re.search(r'(\d+)S', str_time).group(1)) if 'S' in str_time else 0


#     # Convert to total minutes
#     # Convert to total minutes and format to 2 decimal places
#     total_minutes = "{:.2f}".format(hours * 60 + minutes + seconds / 60)
#     return total_minutes

# print(time_parse("PT2H1M59S"))

####CHANNEL ID 
# from pytube import *

# cid = YouTube('https://www.youtube.com/watch?v=5qtC-tsQ-wE').channel_id
# print(cid)

import os
from googleapiclient.discovery import build

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


