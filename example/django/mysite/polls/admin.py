# coding=utf-8

##1
# from django.contrib import admin
# from polls.models import Question
#
# admin.site.register(Question)

##2
# from django.contrib import admin
# from polls.models import Question
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
#
# admin.site.register(Question, QuestionAdmin)

##3
# from django.contrib import admin
# from polls.models import Question
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
#
# admin.site.register(Question, QuestionAdmin)

##4
# from django.contrib import admin
# from polls.models import Question
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]

##5
# from django.contrib import admin
# from polls.models import Choice, Question
# 
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
# 
# admin.site.register(Choice)

##6
# from django.contrib import admin
# from polls.models import Choice, Question
# 
# 
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3
# 
# 
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
# 
# admin.site.register(Question, QuestionAdmin)

##7
# from django.contrib import admin
# from polls.models import Choice, Question
# 
# 
# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3
# 
# 
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
# 
# admin.site.register(Question, QuestionAdmin)

##8
# from django.contrib import admin
# from polls.models import Choice, Question
# 
# 
# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3
# 
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#     # list_display = ('question_text', 'pub_date') # new
#     list_display = ('question_text', 'pub_date', 'was_published_recently') # new2
# 
# admin.site.register(Question, QuestionAdmin)

##9
from django.contrib import admin
from polls.models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] # new
    search_fields = ['question_text'] # new2

admin.site.register(Question, QuestionAdmin)












