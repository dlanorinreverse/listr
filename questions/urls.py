from django.conf.urls import url
from . import views

urlpatterns = [
	# /signup/
  url(r'^$', views.index, name='index'),
  # /login/
  url(r'^login/$', views.login_view, name='login'),
  # /signup/
  url(r'^signup/$', views.signup_view, name='signup'),
  # /logout/
  url(r'^logout/$', views.logout_view, name='logout'),
  # /questions/
  url(r'^questions/$', views.questions, name='questions'),
  # /qustions/id
  url(r'^questions/(?P<question_id>[0-9]+)/$', views.question_detail, name='question_detail'),
  # /topics/
  url(r'^topics/$', views.topics, name='topics'),
  # /qustions/id
  url(r'^topics/(?P<topic_id>[0-9]+)/$', views.topic_detail, name='topic_detail'),
  # /addquestion/
  url(r'^addquestion/(?P<topic_id>[0-9]+)/$', views.addquestion, name='addquestion'),
  url(r'^answer/(?P<answer_id>[0-9]+)/$', views.answer_detail, name='answer_detail'),
  # /addanswer/
  url(r'^addanswer/(?P<question_id>[0-9]+)/$', views.addanswer, name='addanswer'),
  # /addtopic/
  url(r'^addtopic/$', views.addtopic, name='addtopic'),
  # /addcomment/
  url(r'^addcomment/(?P<answer_id>[0-9]+)/$', views.addcomment, name='addcomment'),
]
