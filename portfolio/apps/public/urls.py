from django.urls import path

from . import views

app_name = "public"
urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("projects/", views.projects, name="projects"),
    path("education/", views.education, name="education"),
    path("experience/", views.experience, name="experience"),
    path("skills/", views.skills, name="skills"),
]
