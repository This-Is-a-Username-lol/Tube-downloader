# Tube-downloader
![Screenshot](https://github.com/This-Is-a-Username-lol/Tube-downloader/blob/main/Screenshot.png)

A lightweight GUI application for downloading Youtube videos with fast speed and high quality, It requires ffmpeg to work.
I made this for learning porpuses and have loads of ideas to improve it :).

**Note:** this is a test repo for me to get familiar with github and get some feedback on the app, I might delete it soon, Make a new repo and change the name of the app, Feel free to open an issue or anything.
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

# How to build
**requierments:**
- [Python3](https://www.python.org/)
- [wxPython](https://www.wxpython.org/pages/downloads/)
- [Pytube](https://pypi.org/project/pytube/)
- [cx_Freeze](https://pypi.org/project/cx-Freeze/)

**build**

- ```git clone https://github.com/This-Is-a-Username-lol/Tube-downloader.git```
- ```cd Tube-downloader```
- Configure setup.py if you know what you're doing, If not go to the next step
- ```python3 setup.py build```

# How this tool works
It downloads the audio and video separately with pytube and then it uses ffmpeg to combine them and creat one video file.
