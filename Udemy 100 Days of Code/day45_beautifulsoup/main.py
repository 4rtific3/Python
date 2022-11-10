from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

raw_titles_list = soup.find_all("h3", class_="title")
raw_titles_list.reverse()
titles_list = [title.text for title in raw_titles_list]

with open("movies.txt", "w", encoding="utf-8") as df:
    for title in titles_list:
        df.write(f"{title}\n")