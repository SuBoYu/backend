from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Experience


# Create your views here.
def index(request):
    exp1 = Experience()
    exp1.id = 0
    exp1.name = "DeFi Research and Data Science Intern"
    exp1.location = "OTSO FINTECH CORP."
    exp1.details = ["• Developed quantitative trading strategy in cryptocurrency market with python and machine "
                    "learning model",
                    "• Developed the FTX historical trading pair data crawler system",
                    "• Surveyed and researched the latest DeFi projects"]
    exp1.duration = "Nov. 2021 – Jan 2022"

    

    # exp2 = Experience()
    # exp2.id = 1
    # exp2.name = "Startup Intern"
    # exp2.location = "Epoch School - Young Entrepreneurs of the Future (YEF)"

    exps = [exp1]

    return render(request, "index.html", {"exps": exps})


def test(request):
    # sending dynamic data(like from db)
    context = {
        "name": "Patrick",
        "age": 23,
        "nationality": "Taiwanese"
    }
    return render(request, "test.html", context)


def form(request):
    return render(request, "form.html")


@csrf_exempt
def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request, "counter.html", {"amount": amount_of_words})
