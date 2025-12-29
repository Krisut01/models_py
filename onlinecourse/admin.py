from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin import TabularInline
from django.contrib.admin import StackedInline
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.admin.sites import site
from .models import Course, Lesson, Question, Choice, Submission


class ChoiceInline(TabularInline):
    model = Choice
    extra = 4
    fields = ['choice_text', 'is_correct']


class QuestionInline(StackedInline):
    model = Question
    extra = 1
    fields = ['question_text']
    show_change_link = True


class QuestionAdmin(ModelAdmin):
    list_display = ['question_text', 'lesson', 'created_at']
    list_filter = ['lesson__course', 'created_at']
    search_fields = ['question_text']
    inlines = [ChoiceInline]


class LessonAdmin(ModelAdmin):
    list_display = ['title', 'course', 'order']
    list_filter = ['course']
    search_fields = ['title', 'content']
    inlines = [QuestionInline]


# Register models with admin site
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)