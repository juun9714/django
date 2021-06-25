from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Question, Choice
from django.views import generic

def index(request):
    #READ(GET)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    #render : loader와 HttpResponse를 import하지 않고, 한번에 합쳐서 처리할 수 있는 !

def detail(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html",{'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    #CREAT(POST)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        #해당 Q를 외래키로 갖는 choice들의 set을 가져오게 됨 
        #detail.html이라는 template에서 post방식으로 전송한 request에서 choice라는 이름을 가진 data의 value값과 해당 Q를 외래키로 갖는 choice들의 pk값이 같은지 확인 
        #detail.html의 form tag의 method='post'
        # request.POST는 detail.html에서 제출한 폼의 데이터를 담고 있는 객체 
        # -> request.POST['choice'] = 객체 중 이름이 choice인 input의 value를 string 형식으로 반환
        # request.POST 객체에서 choice라는 키가 없으면 -> KeyError !!        
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            #아무 선택도 하지 않고, submit했을 때, detail.html에 전달할 context data
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # model객체.save() <- create in CRUD
        # selected_choice : 선택된 선택지 : Choice instance 중 선택된 것 
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        #result view로 redirect하는 로직 
        #POST와 세트로 자주 사용됨, post 역할을 하는 view는 보통 데이터를 처리해주고, 
        #그 결과를 보여주는 template을 뿌려주는 view를 실행해야하는데, 그러려면 another url로 이동해야하기 때문
        #vote view는 어떤 화면을 갖지는 않고, 투표를 처리해주는 역할만 한다.

#Generic view
# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#     #context변수의 이름이 model명이랑 다를 땐, context_object_name에 context변수 이름을 명시해준다.


#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     #model을 명시해주면, 해당 모델 이름을 자동으로 context변수로 template에 넘겨준다.
#     template_name = 'polls/detail.html'


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'
