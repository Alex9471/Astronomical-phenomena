from django.shortcuts import render

def index(request):
    return render(request,"main/index.html")

def blackout(request):
    return render(request,"main/blackout.html")

def about_project(request):
    return render(request,"main/about_project.html")

def comets(request):
    return render(request,"main/comets.html")

def polar_lights(request):
    return render(request,"main/polar_lights.html")