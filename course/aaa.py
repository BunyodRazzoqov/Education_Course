from moviepy.video.io.VideoFileClip import VideoFileClip

video = VideoFileClip("static/course/AENH6395.MP4")
duration = video.duration

print("Duration of the video:", duration, "seconds")
