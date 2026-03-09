import urllib.request

url = "https://filesamples.com/samples/video/mp4/sample_640x360.mp4"

urllib.request.urlretrieve(url, "test_video.mp4")

print("Video downloaded successfully!")