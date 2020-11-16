from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()                 # grabbing all the data from databases to the home page
    return render(request, 'portfolio/home.html', {'projects':projects})  #dictionary and passing it in templates/home.html
