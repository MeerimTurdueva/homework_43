from django.shortcuts import render


# Create your views here.

def numbers_calculation(request):
    if request.method == "GET":
        return render(request, "choose_numbers.html")
    else:
        try:
            context = {
                "num1": int(request.POST.get("num1")),
                "num2": int(request.POST.get("num2")),
                "calculation": request.POST.get("calculation"),
            }
        except ValueError as e:
            context = {
                "error": f"Error: {e}"
            }
            return render(request, "choose_numbers.html", context)

        if context["calculation"] == "add":
            context["calc_nums"] = context["num1"] + context["num2"]
            context["sign"] = "+"
        elif context["calculation"] == "subtract":
            context["calc_nums"] = context["num1"] - context["num2"]
            context["sign"] = "-"
        elif context["calculation"] == "multiply":
            context["calc_nums"] = context["num1"] * context["num2"]
            context["sign"] = "*"
        else:
            try:
                context["calc_nums"] = context["num1"] / context["num2"]
                context["sign"] = "/"
            except ZeroDivisionError as e:
                context["error"] = f"Error: {e}"
        return render(request, "choose_numbers.html", context)

