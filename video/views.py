from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Video

def index(request):
    videos = Video.objects.all()
    context = {
        'videos' : videos
    }
    
    return render(request , 'index.html', context)