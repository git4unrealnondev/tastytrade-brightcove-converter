from bs4 import BeautifulSoup
import sys
import os
from selenium import webdriver

if not len(sys.argv) >= 2:
    sys.exit()

driver = webdriver.Firefox(executable_path='./geckodriver')
url = sys.argv[1]
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

sec = soup.find("div", {"class": "brightcove-react-player-loader"})
b4url= str(sec.find("script", {"charset": "utf-8"}))
a4url = b4url.split('src="')[1]
c4url = a4url.split('/index.min.js')[0]

sec = soup.find("video", {"class": "vjs-tech"})

print("Downloading tastyvid")

url = c4url + "/index.html?videoId=" + sec["data-video-id"]

os.system('youtube-dl ' + url)
