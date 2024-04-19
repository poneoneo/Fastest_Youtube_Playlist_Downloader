<div align="center">
  <p>
    <a href="#"><img src="image/pile-logos.jpg" width="656" height="300" alt="pytube logo" /></a>
  </p>
  <p align="center">

  </p>
</div>

# 720p Youtube Playlist Downloader
This script was written to allow the downloading of video playlists from Youtube(720p only) in an asynchronous manner which means that the progress of the downloading of each video will be almost simultaneous instead of waiting the end of each videos.That should be more speed. So enjoy your playlist downloading

## Description
YouTube is the most popular video-sharing platform in the world and as a hacker
you may encounter a situation where you want to script something to download not only single video but an entire playlist. For this I present you 720p Playlist Downloader. 

### Installation
This project is based on pytube-async itself written on [pytube](https://pytube.io/en/latest/) which is the reference python library for downloading youtube videos however it did not have an API to write asynchronous programs. For the specific needs of this script I had to fork the original [**pytube-async**](https://github.com/msemple1111/pytube-async) project to add functionality like:

* Save the progress of downloading each video in the playlist so as not to have to start from the beginning if an error occurs

* Display real-time progress of the download of each video in percentage

for the script to work properly you must follow the following instructions

Create virtual env :
```bash
$ python -m venv your_virtualenv_name
```
Activate your virtual env :
```bash
$ your_virtualenv_name\\Scripts\\activate
```
on Linux :
```bash
$ source your_virtualenv_name/bin/activate
```
The install the only one dependency :

```bash
$ python -m pip install git+https://github.com/poneoneo/pytube-async@allow_resume_when_downloading_crash_aiofile_depency_removed#egg=pytube
```
Run the script and enjoy your downloading:
```bash
$ python main.py
```

### Using 720p Youtube Playlist Downloader
To download your playlist with this script just follow instructions bellow: 

* paste your link in the terminal when the script will asking to do it.

* tell the amount of videos that you want to download. so if you only want the two first videos of your playlist you just have to enter "2". If you want to download th entire playlist then just press `Enter`

* By default the script will create a `Youtube_Playlist_Downloader` folder in the current directory but you can change it by setting the `DEFAULT_PLAYLIST_PATH` variable at the top of the script.

**NB:Make sure that your link comming from a playlist if not, the script will raise an error**

