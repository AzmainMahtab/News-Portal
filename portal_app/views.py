from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.

def index(request):
    newsApi = NewsApiClient(api_key = 'ede03d90771a44f0b747d38ba3d8340a')
    headLines = newsApi.get_top_headlines(sources = 'ign')
    articles = headLines['articles']
    title = []
    dis = []
    image = []
    link = []

    for i in range(len(articles)):
        article = articles[i]
        title.append(article['title'])
        dis.append(article['description'])
        image.append(article['urlToImage'])
        link.append(article['url'])

    myList = zip(title, dis, image, link)  

    return render(request,"portal_app/index.html", context={"myList": myList})  

