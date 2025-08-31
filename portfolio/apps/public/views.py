from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request):
    print(request.user)
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def experience(request: HttpRequest) -> HttpResponse:
    return render(request, "experience.html")


def education(request: HttpRequest) -> HttpResponse:
    return render(request, "education.html")


def projects(request: HttpRequest) -> HttpResponse:
    return render(request, "projects.html")


def skills(request: HttpRequest) -> HttpResponse:
    return render(request, "skills.html")
