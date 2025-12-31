from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Course, Lesson, Question, Choice, Submission

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_details_bootstrap.html', {'course': course})

@login_required
def submit(request):
    if request.method == 'POST':
        # Process exam submission
        user = request.user
        submitted_answers = {}

        # Collect all submitted answers
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = key.replace('question_', '')
                choice_id = value
                submitted_answers[question_id] = choice_id

        # Save submissions to database
        for question_id, choice_id in submitted_answers.items():
            try:
                question = Question.objects.get(pk=question_id)
                choice = Choice.objects.get(pk=choice_id, question=question)

                # Create or update submission
                submission, created = Submission.objects.get_or_create(
                    user=user,
                    question=question,
                    defaults={'selected_choice': choice}
                )
                if not created:
                    submission.selected_choice = choice
                    submission.save()

            except (Question.DoesNotExist, Choice.DoesNotExist):
                continue

        messages.success(request, 'Your exam has been submitted successfully!')
        return redirect('show_exam_result')

    return redirect('course_list')

@login_required
def show_exam_result(request):
    user = request.user

    # Get all submissions for this user
    submissions = Submission.objects.filter(user=user).select_related('question', 'selected_choice')

    if not submissions:
        messages.warning(request, 'You have not submitted any exam yet.')
        return redirect('course_list')

    # Calculate results
    total_questions = submissions.count()
    correct_answers = 0
    results = []

    for submission in submissions:
        is_correct = submission.selected_choice.is_correct
        if is_correct:
            correct_answers += 1

        results.append({
            'question': submission.question,
            'selected_choice': submission.selected_choice,
            'is_correct': is_correct
        })

    score = (correct_answers / total_questions) * 100 if total_questions > 0 else 0

    # Determine if user passed (let's say 70% is passing)
    passed = score >= 70

    context = {
        'results': results,
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'score': round(score, 2),
        'passed': passed
    }

    return render(request, 'exam_result.html', context)
