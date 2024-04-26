from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import path


from games.views import MathFactsView, AnagramHuntView, AboutView, ContactView

app_name = 'games'
urlpatterns = [
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    # path('', MainView.as_view(), name='main'),
    path('', views.main, name='main'),
    path('review/', views.review, name='review'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path("accounts/", include("django.contrib.auth.urls")),
    
]