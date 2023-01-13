from django.shortcuts import render
from django.views.generic.list import ListView

from .models import DataFullstack, SalaryLevel, SalaryPart, TopSkills2015, TopSkills2016, TopSkills2017, TopSkills2018, TopSkills2019, TopSkills2020, TopSkills2021, TopSkills2022


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


def get_top_skills(request):
    skills2015 = TopSkills2015.objects.all()
    skills2016 = TopSkills2016.objects.all()
    skills2017 = TopSkills2017.objects.all()
    skills2018 = TopSkills2018.objects.all()
    skills2019 = TopSkills2019.objects.all()
    skills2020 = TopSkills2020.objects.all()
    skills2021 = TopSkills2021.objects.all()
    skills2022 = TopSkills2022.objects.all()
    response_data = {
        "skills2015": skills2015,
        "skills2016": skills2016,
        "skills2017": skills2017,
        "skills2018": skills2018,
        "skills2019": skills2019,
        "skills2020": skills2020,
        "skills2021": skills2021,
        "skills2022": skills2022,
    }
    return render(request, "skills.html", response_data)
