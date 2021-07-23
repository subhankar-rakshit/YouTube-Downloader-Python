from pytube import YouTube
from pytube.cli import on_progress
from progress.spinner import MoonSpinner
import time

# Progress bar
spinner = MoonSpinner('Loading... ')
FINISHED = False
while not FINISHED:
    for i in range(100):
        time.sleep(0.01)
        spinner.next()
    FINISHED = True
spinner.finish()

# User Inputs
URL = input("Enter URL Here: ")
Download_Path = input("Enter Download path: ")

print("Select Quality:-")
quality_list = {
    '1': '144p',
    '2': '360p',
    '3': '480p',
    '4': '720p',
    '5': 'Audio Only'
}

# Showing options of Resolution
for i, q in quality_list.items():
    print(f"{i}.{q}")

chosen = input("\nEnter the number you've chosen: ")

yt = YouTube(URL, on_progress_callback=on_progress)

print(f"\nTitle: {yt.title}\n")

try:
    if chosen != '5':
        video = yt.streams.filter(mime_type="video/mp4", res=quality_list[choosen], progressive=True).first()
        video.download(output_path=Download_Path)
 
    elif chosen == '5':
        audio = yt.streams.filter(type="audio").first()
        audio.download(output_path=Download_Path)
        
    print("\nDownload Completed!")

except Exception as es:
    print(f"Error due to {es}")
