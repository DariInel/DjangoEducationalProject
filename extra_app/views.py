from django.shortcuts import render

from extra_app.models import Profession


def index_page(request):
    # data = {"profession": Profession.objects.get(id(1))}
    return render(request, "main_page.html")


def demand_page(request):
    # data = {"profession": Profession.objects.get(id(1))}
    return render(request, "demand_page.html")
