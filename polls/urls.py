from django.urls import path

from polls.models import Question
from . import views

#(v2)
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/results/5/
    path("<int:question_id>/results/", views.results, name="results"),
    #ex: /pools/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]