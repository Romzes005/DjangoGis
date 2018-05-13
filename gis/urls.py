"""DjangoGis4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
import gis.views

urlpatterns = [
    url(r'^$', gis.views.home, name='home'),
    url(r'^map/$', gis.views.mymap, name='map'),
    url(r'^about/$', gis.views.about, name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', gis.views.show_articles, name='article'),
    url(r'^news01/$', gis.views.news01, name='news01'),
    url(r'^news02/$', gis.views.news02, name='news02'),
    url(r'^news03/$', gis.views.news03, name='news03'),
    url(r'^news04/$', gis.views.news04, name='news04'),
    url(r'^news05/$', gis.views.news05, name='news05'),
]