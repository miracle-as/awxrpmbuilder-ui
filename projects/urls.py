from django.urls import path, include
from django.shortcuts import redirect
from . import views
from .views import projectListView, SubprojectListView, SubprojectReleaseListView, RootDetailView, SubprojectReleasePackageListView  , packageListView                                                                                                



urlpatterns = [
#    path('', lambda request: redirect('home/root', permanent=False)),
#    path("home", RootDetailView.as_view()),
    path("", packageListView.as_view()),
    path("packages", packageListView.as_view()),
    path("projects/", projectListView.as_view()),
    path("project/<pk>", SubprojectListView.as_view()),
    path("subproject/<pk>", SubprojectReleaseListView.as_view()),
    path("releases/<slug:slug>", SubprojectReleasePackageListView.as_view()),
]

