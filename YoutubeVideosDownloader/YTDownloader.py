# from pytube import YouTube
#
# # Function to download a video from YouTube
# def download_youtube_video(url, output_path='.'):
#     try:
#         # Create a YouTube object
#         yt = YouTube(url)
#
#         # Get the highest resolution stream
#         stream = yt.streams.get_highest_resolution()
#
#         # Download the video
#         print(f"Downloading '{yt.title}'...")
#         stream.download(output_path)
#         print("Download complete!")
#     except Exception as e:
#         print("An error occurred:", e)


from yt_dlp import YoutubeDL

def download_youtube_video(url, output_path='.'):
    try:
        # Setup download options
        ydl_opts = {
            'format': 'best',  # Select the best quality format
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Output file path
        }

        # Download the video
        with YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from {url}...")
            ydl.download([url])
            print("Download complete!")
    except Exception as e:
        print("An error occurred:", e)

# Example usage
video_url = "https://www.youtube.com/shorts/AnM69iYdWn4"  # Replace with the video URL
download_youtube_video(video_url, output_path='D:\\YouTubeVideos')  # Specify the folder to save the video

# from pytube import YouTube
#
# def download_shorts(url):
#     try:
#         video = YouTube(url)
#         stream = video.streams.filter(file_extension='mp4', only_video=True).first()
#         if stream is not None:
#             stream.download()
#             print("Download complete.")
#         else:
#             print("No compatible video found.")
#     except Exception as e:
#         print("An error occurred during download:", str(e))
#
# # URL of the YouTube Shorts you want to download
# shorts_url = "https://www.youtube.com/shorts/AnM69iYdWn4"
#
# # Call the download function
# download_shorts(shorts_url)