import os
import re
import requests
from urllib.parse import urlsplit


def scrape(url: str = "https://1337.tech", initial=True):
    parts = urlsplit(url)

    base_url = "{0.scheme}://{0.netloc}".format(parts)

    base_dir = parts[1]

    if parts.path:
        relative_path, file_name = parts.path.rsplit("/", 1)
    else:
        relative_path = ""
        file_name = "index.html"

    path = base_dir + relative_path + "/"

    os.makedirs(path, exist_ok=True)

    regex_pattern = r'(href|src|content)\="\/([^#][_\S][\S-]*)"'

    if initial:
        response_content = requests.get(url).content.decode("utf-8")
        paths = [
            p[1].replace("amp;", "")
            for p in re.findall(regex_pattern, response_content)
        ]

        with open(path + file_name, "w") as file:
            file.write(response_content)

        for p in paths:
            u = f"{base_url}/{p}"
            scrape(u, initial=False)

    else:
        response_content = requests.get(url).content
        with open(path + file_name, "wb") as file:
            file.write(response_content)
