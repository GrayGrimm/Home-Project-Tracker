from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path("project-groups/", views.ProjectGroupList.as_view(), name="projectgroup-list"),
    path(
        "project-groups/<int:pk>/",
        views.ProjectGroupDetail.as_view(),
        name="projectgroup-detail",
    ),
    path(
        "project-groups/create/",
        views.ProjectGroupCreate.as_view(),
        name="projectgroup-create",
    ),
    path(
        "project-groups/<int:pk>/update/",
        views.ProjectGroupUpdate.as_view(),
        name="projectgroup-update",
    ),
    path(
        "project-groups/<int:pk>/delete/",
        views.ProjectGroupDelete.as_view(),
        name="projectgroup-delete",
    ),
]
