from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Experience, Education


# Create your views here.
def index(request):
    exp0 = Experience()
    exp0.id = 0
    exp0.name = "IT intern (Department of Technology and Operation)"
    exp0.location = "DBS Bank"
    exp0.details = ["• supported the testing team of DBS Strategic COREBanking Solution project"]
    exp0.duration = "July. 2022 – Present"

    exp1 = Experience()
    exp1.id = 1
    exp1.name = "DeFi Research and Data Science Intern"
    exp1.location = "OTSO FINTECH CORP."
    exp1.details = ["• Developed quantitative trading strategy in cryptocurrency market with python and machine "
                    "learning model",
                    "• Developed the FTX historical trading pair data crawler system",
                    "• Surveyed and researched the latest DeFi projects"]
    exp1.duration = "Nov. 2021 – Jan 2022"

    edu0 = Education()
    edu0.id = 0
    edu0.school = "NATIONAL YANG MING CHIAO TUNG UNIVERSITY"
    edu0.degree = "BACHELOR OF SCIENCE"
    edu0.details = ["Major in Computer Science, Minor in Finance Technology",
                    "GPA: 3.9/4.3"]
    edu0.duration = "Sep. 2018 – June. 2022"

    edu1 = Education()
    edu1.id = 1
    edu1.school = "University of Southampton"
    edu1.degree = "Exchange program in ECE school"
    edu1.details = ["Major in Computer Science"]
    edu1.duration = "Jan. 2022 – June. 2022"

    edu2 = Education()
    edu2.id = 2
    edu2.school = "SCHOOL42 SILICON VALLEY"
    edu2.degree = "SHORT-TERM STUDY PROGRAM OF CODING"
    edu2.details = ["Cooperated with coders from all over the world and experienced the innovative engineering and "
                    "programming education and paid a visit to prestigious tech companies such as, Facebook, Google, "
                    "Apple and learned how to make an impact in daily life"]
    edu2.duration = "Aug. 2019 – Sep. 2019"

    exps = [exp0, exp1]
    educ = [edu0, edu1, edu2]

    return render(request, "index.html", {"exps": exps, "educ": educ})


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
