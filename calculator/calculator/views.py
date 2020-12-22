from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def calculate(request):
    number_1 = request.GET.get("number1")
    number_2 = request.GET.get("number2")
    operator = request.GET.get("operator")
    data = {"test": f"{number_1} {operator} {number_2}"}

    return render(request, "home.html", data)
