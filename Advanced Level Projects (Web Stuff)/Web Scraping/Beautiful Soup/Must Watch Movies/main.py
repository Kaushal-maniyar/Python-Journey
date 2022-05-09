from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
titles = soup.find_all(name="h3", class_="title")
with open("movie_list.txt", "w") as file:
    for title in titles:
        file.write(title.text+"\n")
