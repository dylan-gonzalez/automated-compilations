from TikTokApi import TikTokApi

api = TikTokApi.get_instance()
device_id = api.generate_device_id()
count = 30

tiktoks = api.by_username("americanredcross", count=count)

for count, video in enumerate(tiktoks):
    file = open("video" + str(count) + ".mp4", "wb")
    video_bytes =api.get_video_by_tiktok(tiktoks[count], custom_device_id=device_id) 
    file.write(video_bytes)