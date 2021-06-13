from django.shortcuts import render

from .models import Question, choice

# Create your views here.

# get questions and display them


def index(request):
    # return a template. polls/index.html is our template
    return render(request, 'polls/index.html')
