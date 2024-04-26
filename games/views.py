from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review
from django.views.generic import TemplateView
from games.models import Review
from games.forms import ReviewForm
from django.contrib.auth.decorators import login_required


class MathFactsView(LoginRequiredMixin, TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(LoginRequiredMixin, TemplateView):
    template_name = "anagram-hunt.html"

# class MainView(TemplateView):
#     template_name = "main.html"
#     model = Review

class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"

def main(request):
  myreviews = Review.objects.all().values()
  form = ReviewForm()
  if request.method == 'POST':
        if 'save' in request.POST:
            form = ReviewForm(request.POST)
            form.save()
  template = loader.get_template('main.html')
  context = {
    'myreviews': myreviews,
  }
  context['form'] = form
  return HttpResponse(template.render(context, request))

@login_required
def review(request):
  myreviews = Review.objects.all().values()
  form = ReviewForm()
  if request.method == 'POST':
        if 'save' in request.POST:
            form = ReviewForm(request.POST)
            form.save()
  template = loader.get_template('review.html')
  context = {
    'myreviews': myreviews,
  }
  context['form'] = form
  return HttpResponse(template.render(context, request))