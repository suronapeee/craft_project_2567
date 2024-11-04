from django.urls import path
from .views import homePageView, aboutPageView, HomePageView, AboutPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
]
