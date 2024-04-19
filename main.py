# from async_property.cached import AsyncCachedPropertyDescriptor
from pytube import YouTube, Playlist, Stream, StreamQuery
from pytube.extract import playlist_id
from utils import retry_if_error, get_playlist_path
from typing import List, Optional,Any
import asyncio
import aiohttp
import time
import os
import argparse

DEFAULT_PLAYLIST_PATH:str= "Youtube_Playlist_Downloader/"

# permet de suivre l'avancement du telechargement en pourcentage(%)
async def see_percentage_downloaded(stream: Stream, chunk: bytes,
                                    bytes_remaining: int):
    # print(chunk)
    """This function will display the current progression of each stream as soon as he write 
        a chunk on disk. 

    :param stream: an instance of stream chosen ( 720p by default)
    :type stream: Stream
    :param chunk: amount of bytes already wrote on the disk 
    :type chunk: bytes
    :param bytes_remaining: amount of bytes remainning to download
    :type bytes_remaining: int
    """
    stream_size = await stream.filesize # type: ignore
    total_downloaded = bytes_remaining
    percentage_downloaded = total_downloaded / stream_size * 100
    os.system('cls')
    print(
        f"{stream.title} telechargee a {int(percentage_downloaded)} %  {int(total_downloaded / 2 ** 20)}Mb/{int(stream_size / 2 ** 20)}Mb")


# Telecharge une video avec une resolution de 720p
@retry_if_error()
async def download_video(stms: StreamQuery, pl: Playlist, video: YouTube):
    """ 
        Selectionne et telecharge un flux progressif(contenant des codec audio et video)
        avec une resolution de 720p
        cree un dossier avec le nom de la playlist
        
        : param StreamQuery stms:
            Liste de flux media disponible pour cette video
        :param Playlist pl:
            Une instance de la classe :class: Playlist `<Playlist>`
        :param Youtube video:
            Une instance de la classe :class: Youtube `<Youtube>`

    """
    # enregistre la fonction qui doit indiquer le niveau de progression de chaque video de la playlist
    video.register_on_progress_callback(see_percentage_downloaded)  # type: ignore
    choosen_stream: Optional[Stream] = stms.filter(progressive=True, res="720p").first()
    print(choosen_stream)
    if choosen_stream is not None:
        playlist_path = await get_playlist_path(pl,DEFAULT_PLAYLIST_PATH)
        video_title:str = await video.title # type: ignore
        file_path:str = await choosen_stream.download(str(playlist_path.resolve()), max_retries=256, skip_existing=True)
        print(f"{video_title} a ete telecharge dans le dossier {file_path}")
    print("You most to choose 720p resolution")


@retry_if_error()
async def create_youtube_list(pl: Playlist, session:aiohttp.ClientSession,*args, **kwargs):
    """"
        Creee une liste d'instance d'objet Youtube.
        @param pl: Playlist
        @param stop_at: int limite de video a ajouter  dans la liste
        @return: List[Youtube]
    """
    print("Construction de la youtube list")
    final_list:List[YouTube] = []
    counter = 0
    if args and args[0] != None:
        stop_at = args[0]
        async for url in  pl.video_urls():   # type: ignore
            final_list.append(YouTube(url,session=session ))
            counter += 1
            if counter == stop_at:
                break
        print("Construction Terminee")
        return final_list
    else:
        async for url in  pl.video_urls():  # type: ignore
            final_list.append(YouTube(url, ))
        print("Construction Terminee")
        return final_list
        


@retry_if_error()
async def create_task_container(yt_list: List[YouTube], pl: Playlist):
    """"
        Construit une liste d'instance de la classe Task a partir de la couroutine `download_video()` .
        @param yt_list: List[YouTube]
        @param pl: Playlist
        @return: List[asyncio.Tasks]
    """
    print("Construction de la liste des taches a partir de la youtubeList ")
    downloader_tasks_list: List[asyncio.Task] = []
    for video in yt_list:
        streams: StreamQuery = await video.streams # type: ignore
        downloader_tasks_list.append(asyncio.create_task(download_video(streams, pl, video)))
    return downloader_tasks_list


# async def amount_of_videos_in_playlist(pl:Playlist):
#     amount = 0 
#     async for url in pl.video_urls():  # type: ignore
#         amount+=1
#     return amount
    
async def main(url:str, stop_at:int|None = None):
    """Get playlist url to download from and the amount of videos to select in this playlist

    :param url: playlist url 
    :type url: str
    :param stop_at: how many videos the script should select in playlist
    :type stop_at: int
    """
    # create playlist objects 
    pl = Playlist(f"{url}", )
    print(await pl.title)  # type: ignore
    print(f"{await pl.length} Videos", )  # type: ignore
    # amount = await amount_of_videos_in_playlist(pl)
    async with aiohttp.ClientSession() as session:
        youtube_list = await create_youtube_list(pl,session,[stop_at])
        # youtube_list = await youtube_list_task
        tasks_list = await create_task_container(youtube_list, pl)
        dt = asyncio.gather(*tasks_list, return_exceptions=False)
        await dt
        if dt.done():
            dt.cancel()
    # tasks_list = await tasks_list_container_task
    # done,pending = await  asyncio.wait(tasks_list)
 
def check_arguments():
    try :
        playlist_url :str  = input("Paste your playlist url:")
        playlist_id(playlist_url)
        stop_at: int = int(input("How many videos did you want to download from your playlist:"))
    except ValueError as e :
        print(f"\n You should enter an Integer Value:{e}".upper())
        return None
    except KeyError as e:
        print(f"Your url must to be an valid playlist url try again".upper())
        return None
    return playlist_url,stop_at


if __name__ == '__main__': 
    result = check_arguments()
    if result is not None:
        start = time.perf_counter()
        asyncio.run(main(url=result[0],stop_at=result[1]))
        print(f"all those videos took : {time.perf_counter() - start} s".upper())

