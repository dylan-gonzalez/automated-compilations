# Import everything needed to edit video clips
from moviepy.editor import *

clips = []
count = 0
while True:
    print(count)
    try:
        video = VideoFileClip("video" + str(count) + ".mp4").subclip(0,10) 
        clips.append(video)
    except:
        break

    count += 1

# Overlay the text clip on the first video clip
# video = CompositeVideoClip(clips)

final_video = concatenate_videoclips(clips)
final_video.write_videofile("compilation.webm")