from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_list_or_404
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #try:
        #q = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
        #raise Http404('Question does not exist')
    #return render(request, 'polls/detail.html', {'question': q})

    #快捷方式
    question = get_list_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def result(request, question_id):
    return HttpResponse("You're looking at the result of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

