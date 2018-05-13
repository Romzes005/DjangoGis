from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from gis.models import Articles


def home(request):
    # return HttpResponse("Hello world")
    # return render(request, 'gis/home.html')
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'gis/home.html', context)


def show_articles(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    return render(request, 'gis/article.html', {'article': article})


def about(request):
    return render(request, 'gis/about.html')


def mymap(request):
    return render(request, 'gis/map.html')

def news01(request):
    return render(request, 'gis/news01.html')

def news02(request):
    return render(request, 'gis/news02.html')

def news03(request):
    return render(request, 'gis/news03.html')

def news04(request):
    return render(request, 'gis/news04.html')

def news05(request):
    return render(request, 'gis/news05.html')