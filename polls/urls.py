from django.urls import path

from polls.models import Question
from . import views

#(v2)
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    #path("", views.index, name="index"),(v1)
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    #path("<int:question_id>/", views.detail, name="detail"),(v1)
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/results/5/
    #path("<int:question_id>/results/", views.results, name="results"),(v1)
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    #ex: /pools/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
