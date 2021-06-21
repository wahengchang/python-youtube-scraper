from pytube import YouTube
import re

# plots
import matplotlib.pyplot as plt
# matplotlib inline

from modules.DownloadAndExtract import DownloadAndExtract

urlList = [
    'https://www.youtube.com/watch?v=9jyWd0a09uc&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=26',
    'https://www.youtube.com/watch?v=BTVpPVoyYtg&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=28'
]

uniUrlList = list(set(urlList))
for TARGET_URL in uniUrlList:
    dae = DownloadAndExtract(TARGET_URL)
    dae.printBasicInfo()
    dae.extractFrames(perFrame=24*3)
