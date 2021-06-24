from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Question

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     #만들어진 시간을 기준으로 객체를 정렬한 리스트에서 5개까지만 정보를 가져온다 
#     #pub_date
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    #render : loader와 HttpResponse를 import하지 않고, 한번에 합쳐서 처리할 수 있는 !

# def detail(request, question_id):
#     try:
#         question=Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html",{'question':question})


def detail(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html",{'question':question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

