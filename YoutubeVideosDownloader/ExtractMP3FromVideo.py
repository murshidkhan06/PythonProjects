import moviepy.editor
video = moviepy.editor.VideoFileClip("DemystifyingMicroservices.mp4")# Put your file path in here
# Convert video to audio
audio = video.audio
audio.write_audiofile('DemystifyingMicroservices.mp3')