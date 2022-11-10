from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")


raw_articles_list = soup.select(".titleline")
articles = [titleline.find("a").text for titleline in raw_articles_list]
links = [article.find("a").get("href") for article in raw_articles_list]

raw_scores_list = soup.select(".score")
scores = [int(score.text.split()[0]) for score in raw_scores_list]

max_score_index = scores.index(max(scores))
print(articles[max_score_index], links[max_score_index], scores[max_score_index])