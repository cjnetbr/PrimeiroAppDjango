from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

#from django.http import HttpResponse(v1)
#from django.template import loader(v2)

from .models import Choice, Question


# Create your views here.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
  #return HttpResponse("You're voting on question %s." % question_id)(v1)
  question = get_object_or_404(Question, pk=question_id)
  try:
      selected_choice = question.choice_set.get(pk=request.POST["choice"])
  except (KeyError, Choice.DoesNotExist):
      # Redisplay the question voting form.
      return render(
          request,
          "polls/detail.html",
          {
              "question": question,
              "error_message": "You didn't select a choice.",
          },
      )
  else:
      selected_choice.votes = F("votes") + 1
      selected_choice.save()
      # Always return an HttpResponseRedirect after successfully dealing
      # with POST data. This prevents data from being posted twice if a
      # user hits the Back button.
      return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
'''
def index(request):
  #return HttpResponse("Hello, world. You're at the polls index.")(v1)
  latest_quetion_list = Question.objects.order_by('-pub_date')[:5]
  #template = loader.get_template('polls/index.html')(v3)
  context = {
      'latest_question_list': latest_quetion_list,
  }
  #output = ', '.join([q.question_text for q in latest_quetion_list])(v2)
  #return HttpResponse(output)(v2)
  #return HttpResponse(template.render(context, request))(v3)
  return render(request, 'polls/index.html', context)


def detail(request, question_id):
  #return HttpResponse("You're looking at question %s." % question_id)(v1)
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")(v2)
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
  #response = "You're looking at the results of question %s."(v1)
  #return HttpResponse(response % question_id)(v1)
  question = get_object_or_404(Question, pk=question_id)
  return render(request, "polls/results.html", {"question": question})
'''


