from django.shortcuts import render

from .models import Question, choice

# Create your views here.

# get questions and display them


def index(request):

    # first we need to get latest 5 questions from Question table
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # now we need to make an object from this question_list
    context = {"latest_question_list": latest_question_list}

    # now we need to send this context to our template

    # return a template. polls/index.html is our template
    return render(request, 'polls/index.html', context)
