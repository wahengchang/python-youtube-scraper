# python-youtube-scraper
This is a demo about videos on youtub, batch downloading and extract frames from the videos.


#### Init 
```
#$ pip3 freeze > requirements.txt
$ pip3 install -r requirements.txt
```
#### Config
edit the url that you want to download and extract frames

```py
...
urlList = [
    'https://www.youtube.com/watch?v=9jyWd0a09uc&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=26',
    'https://www.youtube.com/watch?v=BTVpPVoyYtg&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=28'
]
...
```

#### Run
```
$ python3 main.py
```
and the frames are extracted under the folder `./frames`
