from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Lesson, Question, Choice, Submission
import json


def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_details_bootstrap.html', {'course': course})


@login_required
def submit(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    questions = lesson.questions.all()

    if request.method == 'POST':
        # Get submitted answers
        submitted_answers = {}
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = key.replace('question_', '')
                submitted_answers[question_id] = value

        # Calculate score
        total_questions = questions.count()
        correct_answers = 0

        for question in questions:
            submitted_choice_id = submitted_answers.get(str(question.id))
            if submitted_choice_id:
                try:
                    choice = Choice.objects.get(id=submitted_choice_id, question=question)
                    if choice.is_correct:
                        correct_answers += 1
                except Choice.DoesNotExist:
                    pass

        score = (correct_answers / total_questions) * 100 if total_questions > 0 else 0

        # Save submission
        submission, created = Submission.objects.update_or_create(
            user=request.user,
            lesson=lesson,
            defaults={'score': score}
        )

        return redirect('show_exam_result', lesson_id=lesson.id)

    return render(request, 'exam.html', {
        'lesson': lesson,
        'questions': questions,
    })


@login_required
def show_exam_result(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    submission = get_object_or_404(Submission, user=request.user, lesson=lesson)

    questions = lesson.questions.all()
    score = submission.score
    total_questions = questions.count()
    correct_answers = int((score / 100) * total_questions)

    context = {
        'lesson': lesson,
        'score': score,
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'passed': score >= 70,  # Assuming 70% is passing grade
        'submission': submission,
    }

    return render(request, 'exam_result.html', context)