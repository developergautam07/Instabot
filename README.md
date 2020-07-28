# Instabot
Instabot is a made for instagram which could like, comment posts and follow pages on instagram

## Requirments
Download Mozilla Firfox Version >= 47

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the requirments from the requirements.txt file.

```bash
pip install -r requirements.txt
```

###For Windows Users:
1. Downoad [Microsoft Visual Studio redistributable runtime](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads) (specially for 64bit users) because sometimes windows defender blocks Mozilla Driver for the binary run.

2. Unzip the geckodriver according to the configuration of your pc 32/64 bit,
And Then Add geckodriver_path:

```python
bot = InstaPy(username="Your username", password="Your Password", geckodriver_path=r"path/geckodriver.exe")
```

## Usage
Watch the full [tutorial](https://youtu.be/aaDBsGIPG4M) on our youtube channel to know the complete setup. 
YT Channel: [Developer Gautam](https://www.youtube.com/channel/UCHc8grk1qQ_LjEODq0clKqA)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
