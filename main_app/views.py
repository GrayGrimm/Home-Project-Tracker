from django.shortcuts import render
from .models import ProjectGroup
from django.views.generic import ListView
# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

class ProjectGroupList(ListView):
    model = ProjectGroup
