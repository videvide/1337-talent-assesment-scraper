from src.scraper.main import generate_path_and_file_name


def test_generate_path_and_filename():
    url = "https://1337.tech"

    assert generate_path_and_file_name(url) == "1337.tech/index.html"
