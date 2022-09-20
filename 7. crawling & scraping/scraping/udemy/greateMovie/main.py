from bs4 import BeautifulSoup
import re
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_web_page = response.text


def get_movie_title(movie_str):
    title = movie_str.split('"__typename":"Image","name":"')[1].split('","')[0]
    return title


soup = BeautifulSoup(empire_web_page, "html.parser")
movies_script = soup.find(name="script", id="__NEXT_DATA__")
movies_str = str(movies_script)

movies_list = []

for movie in re.findall(r'"__typename":"Image","name":".*?"', movies_str):
    title = get_movie_title(movie)
    movies_list.append(title[:-1])

movie_set = set(movies_list)

print(movie_set)
