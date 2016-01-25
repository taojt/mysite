# -*- encoding:utf-8 -*-
from django.contrib import admin
from .models import Question, Choice


# class QuestionAdmin(admin.ModelAdmin):
# 	fields = ["pub_date", "question_text"]

# 字段集
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {"fields": ["question_text"]}),
		("Date Information", {"fields": ["pub_date"], "classes":["collapse"]}),
	]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
