from functools import wraps
from aiohttp import ClientConnectorError, ClientOSError, ClientPayloadError, ClientSession, ServerDisconnectedError
from pytube import Playlist
import asyncio
from pathlib import Path


def retry_if_error(retries=5):
    def wrapper(func):
        @wraps(func, )
        async def wrapped(*args, **kwargs):
            attemps = 0
            error = True
            while error:
                try:
                    func_var = func(*args, **kwargs)
                    task = asyncio.create_task(func_var)
                    return await task
                except ServerDisconnectedError as e:
                    print(f"Une erreur est survenue : {e} \n Nous allons reesayer le telechargement")
                    if e is None or e == "":
                        print("Serveur deconnecte")
                    continue
                except ClientPayloadError as e:
                    print(f"Une erreur est survenue : {e} \n Nous allons reesayer le telechargement")
                    if e is None or e == "":
                        print("Payload error")
                    continue
                except ClientConnectorError as e:
                    print(f"Une erreur est survenue : {e} \n Nous allons reesayer le telechargement")
                    if e is None or e == "":
                        print("Connector error")
                    continue
                except ClientOSError as e:
                    print(f"Une erreur est survenue : {e} \n Nous allons reesayer le telechargement")
                    if e is None or e == "":
                        print("Client OSError")
                    continue
                except asyncio.TimeoutError as e:
                    print(f"Une erreur est survenue : {e} \n Nous allons reesayer le telechargement")
                    if e is None or e == "":
                        print("Asyncio Timeout Error")
                    continue
                else:
                    error = False

        return wrapped

    return wrapper

async def get_playlist_path(playlist_object:Playlist, default_path:str):
        playlist_title: str = await playlist_object.title #type:ignore
        parent_path:Path = Path(default_path)
        (parent_path / Path(f"{'_'.join(playlist_title.split())}")).mkdir(exist_ok=True)# remplace les espaces dans le nom de dossier par '_'
        playlist_path:Path= parent_path/Path(f"{'_'.join(playlist_title.split())}/")
        return playlist_path