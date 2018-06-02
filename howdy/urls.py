# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()), ##the way to setup a HOME page
    url(r'^guide/$', views.GuidePageView.as_view()), ##the way to set up additional pages
]