# coding=utf-8
##1
# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
#
# ##
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


##2
# from django.http import HttpResponse
#
# from polls.models import Question
#
#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([p.question_text for p in latest_question_list])
#     return HttpResponse(output)
#
# # Leave the rest of the views (detail, results, vote) unchanged
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


##3
# from django.http import HttpResponse
# from django.template import RequestContext, loader # new
# from polls.models import Question
#
#
# def index(request):                                                    # changed
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]  # changed
#     template = loader.get_template('polls/index.html')                 # changed
#     context = RequestContext(request, {                                # changed
#         'latest_question_list': latest_question_list,                  # changed
#     })                                                                 # changed
#     return HttpResponse(template.render(context))
#
# # Leave the rest of the views (detail, results, vote) unchanged
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


##3
# from django.http import HttpResponse
# # from django.template import RequestContext, loader
# from polls.models import Question
# from django.shortcuts import render
#
#
#
# def index(request):                                                         # changed
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5] # changed
#     context = {'latest_question_list': latest_question_list}                # changed
#     return render(request, 'polls/index.html', context)                     # changed
#
# # Leave the rest of the views (detail, results, vote) unchanged
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


##4
# from django.http import HttpResponse
# from django.http import Http404
# from django.shortcuts import render
# from polls.models import Question
#
# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
# # def detail(request, question_id):
# #     try:
# #         question = Question.objects.get(pk=question_id)
# #     except Question.DoesNotExist:
# #         raise Http404
# #     return render(request, 'polls/detail.html', {'question': question})
#
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


##5
# from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
# 
# from polls.models import Choice, Question
# # ...
# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
# 
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
# 
# # def results(request, question_id):
# #     response = "You're looking at the results of question %s."
# #     return HttpResponse(response % question_id)
# 
# def results(request, question_id):                                       # changed
#     question = get_object_or_404(Question, pk=question_id)               # changed
#     return render(request, 'polls/results.html', {'question': question}) # changed
# # ...
# def vote(request, question_id):
#     p = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': p,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


##6
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

