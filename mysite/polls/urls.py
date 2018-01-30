from django.conf.urls import url

from . import views

#url方法中指定了命名空间，则此处app_name不能少
app_name = 'polls'

urlpatterns = [
    #匹配/polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #匹配/polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #/polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name='results'),
    #/polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]