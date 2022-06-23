import os
import re
import requests
from tqdm import tqdm
from urllib.parse import urlsplit
from concurrent.futures import ThreadPoolExecutor

BASE_DIR = "1337.tech"
REGEX_PATTERN = r'(href|src|content)\="\/([^#][_\S][\S-]*)"'

urls = set()


def generate_path_and_file_name(url):
    parts = urlsplit(url)
    if parts.path:
        if parts.query:
            relative_path = parts.path
            file_name = parts.query
        else:
            relative_path, file_name = parts.path.rsplit("/", 1)
            relative_path += "/"
    else:
        relative_path = "/"
        file_name = "index.html"

    return BASE_DIR + relative_path, file_name


def create_and_save_response(url: str, initial=False):
    response = requests.get(url, stream=True)
    local_path, file_name = generate_path_and_file_name(url)
    os.makedirs(local_path, exist_ok=True)

    with tqdm(total=len(response.content)) as pbar:
        with open(local_path + file_name, "wb") as file:
            for chunk in response.iter_content(16385):
                file.write(chunk)
                pbar.update(len(chunk))

    if initial:
        urls.update(
            f"{url}/{path[1].replace('amp;', '')}"
            for path in re.findall(REGEX_PATTERN, response.content.decode("utf-8"))
        )


if __name__ == "__main__":
    create_and_save_response("https://1337.tech", initial=True)
    with ThreadPoolExecutor() as executor:
        executor.map(create_and_save_response, urls)
