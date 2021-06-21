from pytube import YouTube
import re

# plots
import matplotlib.pyplot as plt
# matplotlib inline

from DownloadAndExtract import DownloadAndExtract


urlList = [
'https://www.youtube.com/watch?v=9jyWd0a09uc&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=26',
'https://www.youtube.com/watch?v=BTVpPVoyYtg&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=28',
'https://www.youtube.com/watch?v=pysW7ucL9l4&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=29',
'https://www.youtube.com/watch?v=sd6ZThy57oI&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=30',
'https://www.youtube.com/watch?v=FN5xh64ePN0&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=31',
'https://www.youtube.com/watch?v=vviYnCWYQC8&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=32',
'https://www.youtube.com/watch?v=uowYG7jeslc&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=33',
'https://www.youtube.com/watch?v=32zA1lW8470&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=34',
'https://www.youtube.com/watch?v=LDHSKe23z_Q&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=35',
'https://www.youtube.com/watch?v=ixrWNlK-AjM&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=42',
'https://www.youtube.com/watch?v=Vkl97dm8uEk&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=41',
'https://www.youtube.com/watch?v=uCyMe8xmCfo&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=40',
'https://www.youtube.com/watch?v=lrCHFGQ-gpo&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=55',
'https://www.youtube.com/watch?v=9dZ4S23blis&list=PLEWa3n9b9vtEm9NnUUnt_oMtzZQdKKPsd&index=56',
'https://www.youtube.com/watch?v=kB-yo6qR5ZI&list=PLC71D73F01848AA9B',
'https://www.youtube.com/watch?v=uKHL8v8-T38',
'https://www.youtube.com/watch?v=OVh4ATKdiIU',
'https://www.youtube.com/watch?v=wykOv_SsD5I&list=PLK9eC7l1q6dJOTRM-BStrdLoMxI-IX1iU',
'https://www.youtube.com/watch?v=WUWZfG3HhSw'
]

uniUrlList = list(set(urlList))
for TARGET_URL in uniUrlList:
    dae = DownloadAndExtract(TARGET_URL)
    dae.printBasicInfo()
    dae.extractFrames(perFrame=24*3)
