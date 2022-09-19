# 웹사이트에 접속하기

import webbrowser

url = "https://www.google.co.kr"
# webbrowser.open(url)

# html 파일을 읽어오기
import requests

html = requests.get(url).text
# print(html[0:100])

# html 파일을 파싱하기
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
# print(soup.find("a"))

# 이미지 다운 받기
import cssutils
import os


def download_image(img_folder, img_url):
    if img_url != None:
        html_image = requests.get(img_url)
        imageFile = open(os.path.join(img_folder, os.path.basename(img_url)), "wb")

        chunk_size = 1000000
        for chunk in html_image.iter_content(chunk_size):
            imageFile.write(chunk)
            imageFile.close()

        print("Downloaded: " + img_url)
    else:
        print("None")


url = "https://www.reshot.com/free-svg-icons/animal/"
folder = "images/"

html_reshot = requests.get(url).text
soup_reshot = BeautifulSoup(html_reshot, "html.parser")
reshot_image_elements = soup_reshot.select("a > div")

for _ in reshot_image_elements:
    image_sytle = cssutils.parseStyle(_.get("style"))
    image_url_tag = image_sytle["--image"]
    image_url = image_url_tag[4 : len(image_url_tag) - 1]
    download_image(folder, image_url)
