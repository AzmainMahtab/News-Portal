from django.shortcuts import render
from newsapi import NewsApiClient
import requests
from django.conf import settings
from isodate import parse_duration

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

def youtube(request):
    req_link = 'https://www.googleapis.com/youtube/v3/videos'
    #Parameters for the API
    params = {
        'key': settings.YOUTUBE_DATA_API_KEY,
        'part': 'snippet, contentDetails',
        'chart': 'mostPopular',
        'maxResults': 20
    }
    r = requests.get(req_link,params= params).json()
    #items for itarating item int the json list
    items = r['items']
    #empty dictonaries to append to
    #video_ids = []
    titles = []
    urls = []
    durations = []
    thumbnails = []
    #itarating items and appending them to dictonaries
    for i in range(len(items)):
        video = items[i]
        #video_ids.append(video['id'])
        titles.append(video['snippet']['title'])
        urls.append(f'https://www.youtube.com/watch?v={ video["id"] }')
        #pasing the duration to mins
        durations.append(int(parse_duration(video['contentDetails']['duration']).total_seconds()//60))
        thumbnails.append(video['snippet']['thumbnails']['high']['url'])
    
    videos = zip(thumbnails, titles, durations, urls)
    

    return render(request,"portal_app/youtube.html", {"videos": videos})