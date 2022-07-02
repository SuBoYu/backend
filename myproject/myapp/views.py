from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    # sending dynamic data(like from db)
    context = {
        "name": "Patrick",
        "age": 23,
        "nationality": "Taiwanese"
    }
    return render(request, "index.html", context)

def form(request):

    return render(request, "form.html")

@csrf_exempt
def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request, "counter.html", {"amount": amount_of_words})
