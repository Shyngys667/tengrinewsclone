from .models import Article
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bs4 import BeautifulSoup
import requests

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
}
DOMEN = "http://tengrinews.kz"
URL = "https://tengrinews.kz/tag/алматы/"

def get_article(url_def, headers_def=HEADERS):
    articles = requests.get(url=url_def, headers=headers_def) 
    if articles.status_code == 200:  
        content = articles.content
        return content
    else:
        return f"bad articles {articles.status_code}"

def get_soup(articles):
    soup = BeautifulSoup(articles, 'html.parser')
    all_news = soup.find_all("div", class_="content_main_item")
    for item in all_news:
        slug = str(item.find("a").get("href").split("/")[-2])
        title = item.find("span", class_="content_main_item_title").find("a").text
        description = item.find("span", class_="content_main_item_announce").text
        try:
            image = DOMEN + item.find("a").find("img").get("src")
        except Exception: 
            image = DOMEN + item.find("a").find("img").get("src")

        new_article = Article(slug=slug, title=title, description=description, image=image)
        new_article.save()


def parser(request):
    articles = get_article(url_def=URL)
    get_soup(articles)
    return render(request, "parser.html", context={})