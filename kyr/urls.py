"""kyr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from kyr.complaints.api import ComplaintViewSet
from kyr.parliament.api import MemberOfParliamentViewSet


router = routers.DefaultRouter(trailing_slash=True)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/complaints/$', ComplaintViewSet.as_view()),
    url(r'^api/membersearch/name/(?P<name_of_the_mp>.+)/$', MemberOfParliamentViewSet.as_view()),
    # For the above URL pattern We need a better REGEX or something of that sort to handle
    # name which is being searched
]
