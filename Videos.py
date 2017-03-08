from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=yKzlitd_G0M")

print(video.get_videos())

videoDownload = video.get('mp4', '720p')
videoDownload.download('/home/raphaelpizzo/Downloads')