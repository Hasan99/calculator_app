from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def calculate(request):
    data = {
        "answer": 0,
        "error_message": "",
        "expression": ""
    }

    try:
        number_1 = int(request.GET.get("number1"))
        number_2 = int(request.GET.get("number2"))
        operator = request.GET.get("operator")

        if operator == "+":
            data["answer"] = number_1 + number_2
        elif operator == "-":
            data["answer"] = number_1 - number_2
        elif operator == "*":
            data["answer"] = number_1 * number_2
        elif operator == "/":
            data["answer"] = number_1 / number_2

        data["expression"] = str(number_1) + " " + operator + " " + str(number_2) + " = "

        return render(request, "home.html", data)
    except Exception as error:
        data["error_message"] = f"Invalid Number ({str(error)})"
        return render(request, "home.html", data)
