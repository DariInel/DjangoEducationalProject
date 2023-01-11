from django.shortcuts import render
from django.views.generic.list import ListView

from .models import DataFullstack, SalaryLevel, SalaryPart


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


def get_salary_level(request):
    cities = SalaryLevel.objects.all()
    return render(request, "geography.html", {"cities": cities})


def get_salary_part(request):
    parts = SalaryPart.objects.all()
    return render(request, "geography.html", {"parts": parts})


def get_salary(request):
    cities = SalaryLevel.objects.all()
    parts = SalaryPart.objects.all()

    response_data = {
        "cities": cities,
        "parts": parts,
    }

    return render(request, 'geography.html', response_data)
