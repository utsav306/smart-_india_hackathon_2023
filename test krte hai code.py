
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


from MODULE_TEST import *

print(post_video_stats("https://youtube.com/playlist?list=PLU6SqdYcYsfJV8Lfq4KFA0U8kGeJ2NGWV&si=zq8VtON19aU-aL6g"))

