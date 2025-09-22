from django.shortcuts import render, redirect
from .models import ProjectGroup
from .forms import ProjectForm
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView

# Create your views here.


class Home(LoginView):
    template_name = "home.html"


def about(request):
    return render(request, "about.html")


class ProjectGroupList(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return ProjectGroup.objects.filter(user=self.request.user)


class ProjectGroupDetail(LoginRequiredMixin, DetailView):
    model = ProjectGroup

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ProjectForm()
        return context


class ProjectGroupCreate(LoginRequiredMixin, CreateView):
    model = ProjectGroup
    fields = ["name", "type"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectGroupUpdate(LoginRequiredMixin, UpdateView):
    model = ProjectGroup
    fields = ["name", "type"]

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj


class ProjectGroupDelete(LoginRequiredMixin, DeleteView):
    model = ProjectGroup
    success_url = "/projectgroups/"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("projectgroup-list")
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)
