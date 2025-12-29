from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
    fields = ['choice_text', 'is_correct']

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    inlines = [ChoiceInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'lesson', 'created_at']
    list_filter = ['lesson', 'created_at']
    search_fields = ['question_text']
    inlines = [ChoiceInline]

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    list_filter = ['course']
    search_fields = ['title', 'content']
    inlines = [QuestionInline]

# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
