import requests
from tqdm import tqdm
import time

# r = requests.get(
#     "https://1337.tech/_next/static/videos/clients-digital-10ef4faa5fee026cc2a99d4c3ce6a294.mp4",
#     stream=True,
# )

# with tqdm(total=len(r.content)) as pbar:
#     with open("TEEEEESSSSTTTTTT.html", "wb") as file:
#         for chunk in r.iter_content(1024):
#             file.write(chunk)
#             pbar.update(len(chunk))

with requests.get(
    "https://www.python.org/ftp/python/3.10.5/Python-3.10.5.tgz", stream=True
) as response:
    with tqdm(total=int(response.headers.get("content-length"))) as pbar:
        for chunk in response.iter_content(1024):
            pbar.update(len(chunk))
