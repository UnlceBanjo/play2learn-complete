from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from play2learn.views.generic import TemplateView


# Create your views here.



class MainView(TemplateView):
    template_name = "main.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html" 