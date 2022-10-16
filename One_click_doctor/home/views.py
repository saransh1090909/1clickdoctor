import random
from django.conf import settings
from email.mime import image
from importlib.resources import path
from unittest.mock import patch
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme

from .models import Tweet
from .forms import TweetForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def index(request):
    context = {
        'variable1':'ONLINE RECOMENDATION  here',
        'variable2':'ask questions and and get answer by theory' 
    } 
    return render(request, 'index.html', context)
def Aurdeva(request):
    return render(request, 'Aurdeva.html' )
    #return HttpResponse("This is Aurdeva page")
def Helpful_Herbs(request):
    return render(request, 'Helpful_Herbs.html' )
    #return HttpResponse("This is Helpful Herbs page")
def Acupressure(request):
    return render(request, 'Acupressure.html' )
    #return HttpResponse("This is Acupressure page")
def Article(request):
    return render(request, 'Article.html' )
    #return HttpResponse("This is FOR page")
def About_us(request):
    return render(request, 'index.html')
    #return HttpResponse("This is About_us page")
def top_reasons(request):
    return render(request, 'reasons.html')


def tweet_create_view(request, *args, **kwargs):
    #print("ajax", request.is_ajax())
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    print("next_url", next_url)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        #if request.is_ajax():
            #return JsonResponse({}, status=201)
            
        if next_url != None and url_has_allowed_host_and_scheme(next_url, ALLOWED_HOSTS):
           return redirect(next_url)
        form = TweetForm()
    return render(request, 'registration/form.html', context={'form':form})

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
        #"content": obj.content,
       # "image_path": obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "NOT found"
        status = 404
    return JsonResponse(data, status=status)


def post_list_view(request, *args, **kwargs):
    qs  = Tweet.objects.all()
    tweets_list =[{"id": x.id, "content":x.content, "likes": random.randint(1, 99)} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)
    
def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }