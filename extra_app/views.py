from django.shortcuts import render

from extra_app.models import Profession


def index_page(request):
    # data = {"profession": Profession.objects.get(id(1))}
    return render(request, "main_page.html")


def demand_page(request):
    return render(request, "demand_page.html")


def geography_page(request):
    return render(request, "geography.html")


def skills_page(request):
    return render(request, "skills.html")


def latest_vacancies_page(request):
    return render(request, "latest_vacancies.html")