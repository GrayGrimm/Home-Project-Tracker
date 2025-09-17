from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("project-groups/", views.ProjectGroupList.as_view(), name="project-groups-index"),
]
