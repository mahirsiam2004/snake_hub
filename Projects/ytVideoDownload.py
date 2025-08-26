from pytube import YouTube

# Paste your YouTube video link here
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

yt = YouTube(url)

stream = yt.streams.get_highest_resolution()


stream.download(output_path="downloads", filename="my_video.mp4")

print("✅ Download completed!")
