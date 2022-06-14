% Talent assesment 1337 (Python)

# Simple console application to scrape 1337.tech and save results to disk

The program will download and save all files in a folder inside your current working directory
Example: ~/1337-talent-assesment/1337.tech

Create a virtual environment and install it with:

```
python3 -m venv venv && \
. venv/bin/activate && \
pip install -i https://test.pypi.org/simple/ 1337-talent-assesment-scraper-videvide
```

Install requests:

```
pip install requests
```

Start a python shell and run the program:

```
python
```

```
>>> from scraper.main import scrape
>>> scrape()
```

Now the downloaded files will appear in a folder named: 1337.tech inside the current working directory