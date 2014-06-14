from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import requests
import webbrowser
import dateutil.parser

API_KEY = "AIzaSyCLMOpxiN2cW1sgiKB5y6UJlL9lmQN6Gfg"
YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

def SEARCH_PARAMS(query):
    return {
        'part' : 'snippet',
        'q' : query,
        'type' : 'video',
        'key' : API_KEY,
        'thumbnails' : 'thumbnails',
        'title' : 'title',
        'maxResults' : 10,
    }

def SearchView(request):
    if 'query' in request.GET:
        youtube_search = requests.get(YOUTUBE_SEARCH_URL, params=SEARCH_PARAMS(request.GET['query']))
        data =  youtube_search.json()
        new_video = []
        for item in data['items']:
            new_video.append({
                'id' : item['id']['videoId'],
                'title' : item['snippet']['title'],
                'thumbnails' : item['snippet']['thumbnails']['high']['url'],
                'pub_date' : dateutil.parser.parse(item['snippet']['publishedAt']).strftime('%B %d, %Y, %X'),
                'infos' : item['snippet']['description'],
            })
    return render(request, 'MicroTube/search.html', {
            'new_video' : new_video,
        })

def IndexView(request):
    return render(request, 'MicroTube/base.html')
