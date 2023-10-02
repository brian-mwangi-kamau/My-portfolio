from django.shortcuts import render, redirect
from .models import Project


# Create your views here.
def home(request):
    projects = Project.objects.all()

    context = {
        "projects": projects,
    }
    return render(request, 'home.html', context)