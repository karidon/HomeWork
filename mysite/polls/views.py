from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.
from polls.models import Choise, Question


class IndexView(generic.ListView):  # ListView отображает список объекта
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by('-pub_date')[:5]


class DetailView(
	generic.DetailView):  # DetailView отображает подробности о конкретном объекте
	model = Question  # Общее представление
	template_name = 'polls/detail.html'  # шаблон для DetailView


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'


def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choise_set.get(pk=request.POST['choice'])
	except (KeyError, Choise.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': p,
			'error_message': "You didn't select a choice.",})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


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

# def index(request):
#	latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#	context = {'latest_question_list': latest_question_list}
#	return render(request, 'polls/index.html', context)


# def detail(request, question_id):
'''
Функция get_object_or_404() первым аргументом принимает Django модель и
произвольное количество именованных аргументов, которые передаются в метод
get() менеджера модели. Если объект не найден, вызывается исключение Http404.
'''  # question = get_object_or_404(Question, pk=question_id)
#	return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#	question = get_object_or_404(Question, pk=question_id)
#	return render(request, 'polls/results.html', {'question': question})
