from os import error
from django.http.response import Http404
from django.shortcuts import render

from .models import Question, choice

from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

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


# show specific question and choices


# <a href="{% url 'polls:detail' question.id %}" class="btn btn-primary btn-sm">Vote Now</a> where question_id is the parameter
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {"question": question}
    except Question.DoesNotExist:
        raise Http404("Question doesnot exist")

    return render(request, 'polls/detail.html', context)


# <a href="{% url 'polls:results' question.id %}" class="btn btn-primary btn-sm">Results</a> where question_id is the parameter
def results(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
        context = {"question": question}
    except Question.DoesNotExist:
        raise Http404("Question doesnot exist")

    return render(request, 'polls/results.html', context)

# Vote for a question choice


def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
