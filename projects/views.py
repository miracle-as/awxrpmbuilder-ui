from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseForbidden
from django.http import Http404

from .models import rootdetail
from .models import project
from .models import subproject
from .models import subprojectrelease

from .models import package
from .models import requirement
from .models import packagetweak
from .models import packagetweakrelation

class projectListView(ListView):
    model = project 
    template_name = 'projects.html'

class SubprojectListView(ListView):
    # specify the model for create view
    model = subproject 
    template_name = 'Subprojects.html'


class SubprojectReleaseListView(ListView):
    # specify the model for create view
    model = subprojectrelease
    template_name = 'SubprojectReleases.html'

class SubprojectReleasePackageListView(ListView):
    # specify the model for create view
    model =  requirement
    template_name = 'SubprojectReleasePackages.html'


class RootDetailView(DetailView):
    model = rootdetail
    template_name = 'rootdetailview.html'


class packageListView(ListView):
    # specify the model for create view
    model = package 
    template_name = 'packages.html'
    ordering = ['packagesclrpmfilestatus']



