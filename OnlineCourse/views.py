from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Lesson, Question, Choice, Submission

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'OnlineCourse/course_details_bootstrap.html', {'course': course})

@login_required
def submit(request):
    if request.method == 'POST':
        lesson_id = request.POST.get('lesson_id')
        lesson = get_object_or_404(Lesson, pk=lesson_id)

        # Get all questions for this lesson
        questions = lesson.questions.all()
        total_questions = questions.count()
        correct_answers = 0

        # Process each question submission
        for question in questions:
            choice_id = request.POST.get(f'question_{question.id}')
            if choice_id:
                try:
                    choice = Choice.objects.get(pk=choice_id, question=question)
                    is_correct = choice.is_correct

                    # Create submission record
                    Submission.objects.create(
                        user=request.user,
                        question=question,
                        selected_choice=choice,
                        is_correct=is_correct
                    )

                    if is_correct:
                        correct_answers += 1

                except Choice.DoesNotExist:
                    continue

        # Calculate score
        score = int((correct_answers / total_questions) * 100) if total_questions > 0 else 0

        # Store results in session for the result view
        request.session['exam_results'] = {
            'lesson_title': lesson.title,
            'total_questions': total_questions,
            'correct_answers': correct_answers,
            'score': score,
            'passed': score >= 70
        }

        return redirect('show_exam_result')

    return redirect('course_list')

@login_required
def show_exam_result(request):
    exam_results = request.session.get('exam_results')
    if not exam_results:
        messages.error(request, 'No exam results found.')
        return redirect('course_list')

    context = {
        'lesson_title': exam_results['lesson_title'],
        'total_questions': exam_results['total_questions'],
        'correct_answers': exam_results['correct_answers'],
        'score': exam_results['score'],
        'passed': exam_results['passed'],
    }

    # Clear the session data after displaying
    del request.session['exam_results']

    return render(request, 'OnlineCourse/exam_result.html', context)
