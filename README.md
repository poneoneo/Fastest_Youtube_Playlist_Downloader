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
Pytube requires an installation of python 3.6 or greater, as well as pip.
Pip is typically bundled with python installations, and you can find options for how to install python at https://python.org.


To install from source with pip:

```bash
$ python -m pip install git+https://github.com/poneoneo/pytube-async@allow_resume_when_downloading_crash_aiofile_depency_removed#egg=pytube
```

on windows, open cmd.exe and run:
```bash
py -m pip install git+https://github.com/poneoneo/pytube-async@allow_resume_when_downloading_crash_aiofile_depency_removed#egg=pytube
```

### Using 720p Youtube Playlist Downloader
To download your playlist with this script just follow instructions bellow: 

* paste your link in the terminal when the script will asking to do it.

* tell the amount of videos that you want to download. so if you only want the two first videos of your playlist you just have to enter "2".

* By default the script will create a `Youtube_Playlist_Downloader` folder in the current directory but you can change it by setting the `DEFAULT_PLAYLIST_PATH` variable at the top of the script.

**NB:Make sure that your link comming from a playlist if not, the script will raise an error**

