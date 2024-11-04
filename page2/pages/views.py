from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
import datetime

# For Tag: Loop Through a Range
years = list(range(2020, 2023))
# If Tag: Conditional Rendering
is_vision_clear = True
# Empty Tag: Check if a Variable is Empty
team_members = [] 

def homePageView(request):
    today = datetime.datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request,'home.html',{'today':today, 'days_of_week':daysOfWeek})

def aboutPageView(request):
    #var = {'var1':1, 'var2':[1,2,3], 'var3':range(1,6)} 
    #today = datetime.datetime.now().date()
    #daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    #dicts = {'a':0, 'b':1}
    # context = {'var': var, "today": today}
    #context = {"today" : today, "days_of_week" : daysOfWeek, 'dicts':dicts}
    context = {'years': years,'is_vision_clear': is_vision_clear,'team_members': team_members, 'a':'<b>Hello<b>'}
    return render(request, 'about.html', context)

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

