 # howdy/views.py
 
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here. ##HOME PAGE VIEW
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Second page view
class GuidePageView(TemplateView):
    template_name = "guide.html"