from django.shortcuts import render
from django.views.generic.list import ListView

from .models import DataFullstack


def index_page(request):
    return render(request, "main_page.html")


def demand_page(request):
    return render(request, "demand_page.html")


def geography_page(request):
    return render(request, "geography.html")


def skills_page(request):
    return render(request, "skills.html")


def latest_vacancies_page(request):
    return render(request, "latest_vacancies.html")


def get_table_fullstack(request):
    profession = DataFullstack.objects.all()
    return render(request, "demand_page.html", {"profession": profession})
