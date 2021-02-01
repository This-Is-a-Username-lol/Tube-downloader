# Tube-downloader
![Screenshot](https://github.com/This-Is-a-Username-lol/Tube-downloader/blob/main/Screenshot.png)

A lightweight GUI application for downloading Youtube videos with fast speed and high quality, It requires ffmpeg to work.
I made this for learning porpuses and have loads of ideas to improve it :).

# Libraries used
- wxPython
- Pytube
# How to install
This application requires [ffmpeg](https://www.ffmpeg.org/download.html) to work so make sure you have it installed.

**Linux:**

- Grab the latest build from the [Release](https://github.com/This-Is-a-Username-lol/Tube-downloader/releases) page.
- Extract it where you want
- ```cd``` into where you extracted it
- ```./tube-downloader```

**Windows:**

I'm currently working on adding windows support.

# How this tool works
It downloads the audio and video separately with pytube and then it uses ffmpeg to combine them and creat one video file.
