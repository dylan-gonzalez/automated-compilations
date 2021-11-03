from TikTokApi import TikTokApi
import random

# SEE https://github.com/davidteather/TikTok-Api/issues/311#issuecomment-721164493

# Starts TikTokApi
api = TikTokApi.get_instance()

# This is generating the tt_webid_v2 cookie
# need to pass it to methods you want to download
device_id = api.generate_device_id()

tiktoks = api.by_trending(custom_device_id=device_id, count = 10)
# tiktoks = api.by_hashtag("funny", count = 10, custom_device_id = device_id)

# Below is if the method used if you have the full tiktok object
# video_bytes = api.get_video_by_tiktok(trending[0], custom_device_id=device_id)

# with open("video.mp4", "wb") as out:
#     out.write(video_bytes)
for count, video in enumerate(tiktoks):
    file = open("video" + str(count) + ".mp4", "wb")
    video_bytes =api.get_video_by_tiktok(tiktoks[count], custom_device_id=device_id) 
    file.write(video_bytes)