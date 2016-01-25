# !/usr/bin/python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^(?P<question_id>\d+)/$", views.detail, name="detail"),
	url(r"^(?P<question_id>\d+)/results/$", views.results, name="results"),
	url(r"^(?P<question_id>\d+)/votes/$", views.vote, name="vote")


]