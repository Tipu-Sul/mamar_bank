from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.iew
class HomeView(TemplateView):
   template_name= 'index.html'
