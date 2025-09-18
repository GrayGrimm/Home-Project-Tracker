from django.shortcuts import render
from .models import ProjectGroup
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView

# Create your views here.


class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, "about.html")


class ProjectGroupList(ListView):
    model = ProjectGroup


class ProjectGroupDetail(DetailView):
    model = ProjectGroup


class ProjectGroupCreate(CreateView):
    model = ProjectGroup
    fields = "__all__"


class ProjectGroupUpdate(UpdateView):
    model = ProjectGroup
    fields = "__all__"

class ProjectGroupDelete(DeleteView):
    model = ProjectGroup
    success_url = '/projectgroups/'