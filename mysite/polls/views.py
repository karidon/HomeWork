from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
# from django.template import RequestContext, loader
from polls.models import Question

'''
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request,
	                         {'latest_question_list': latest_question_list})
	return HttpResponse(template.render(context))
'''

'''
Процесс загрузки шаблона, добавления контекста и возврат объекта HttpResponse,
вполне тривиальный. Django предоставляет функцию для всех этих операций.
'''


def index(request):
	latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)


def detail(request, question_id):
	'''
	Функция get_object_or_404() первым аргументом принимает Django модель и
	произвольное количество именованных аргументов, которые передаются в метод
	get() менеджера модели. Если объект не найден, вызывается исключение Http404.
	'''
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)


def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
