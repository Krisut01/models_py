# Django Online Course Application

This is a Django-based Online Course application with assessment features, built as part of a Coursera assignment.

## Features

- **Course Management**: Create and manage courses with lessons
- **Assessment System**: Multiple choice questions with automated scoring
- **Admin Interface**: Comprehensive admin panel for content management
- **Bootstrap UI**: Responsive templates using Bootstrap 5
- **User Authentication**: Support for user submissions and results

## Models

- **Course**: Represents a course with name and description
- **Lesson**: Lessons belonging to courses with title and content
- **Question**: Multiple choice questions for lessons
- **Choice**: Answer choices for questions (one correct per question)
- **Submission**: User submissions tracking answers and scores

## Key Components

### Admin Configuration
- `QuestionInline`: Inline editing for choices within questions
- `ChoiceInline`: Inline editing for choices within questions
- `QuestionAdmin`: Admin interface for questions with inline choices
- `LessonAdmin`: Admin interface for lessons with inline questions

### Templates
- `course_details_bootstrap.html`: Course detail page with Bootstrap styling
- `exam_result.html`: Exam results display with congratulations message

### Views
- `submit`: Handles exam submission and scoring
- `show_exam_result`: Displays exam results with pass/fail status
- `course_detail`: Shows course information and lessons

## Installation

1. Install Django: `pip install django`
2. Run migrations: `python manage.py migrate`
3. Create superuser: `python manage.py createsuperuser`
4. Run server: `python manage.py runserver`

## URLs

- `/admin/`: Admin interface
- `/course/<id>/`: Course detail page
- `/submit/`: Exam submission endpoint
- `/exam-result/`: Exam results page

## Assignment Requirements Met

✅ **Task 1**: models.py with Question, Choice, and Submission models
✅ **Task 2**: admin.py with 7 imported classes and required admin classes
✅ **Task 3**: Admin site screenshot showing Authentication and OnlineCourse sections
✅ **Task 4**: course_details_bootstrap.html with Django templates and Bootstrap
✅ **Task 5**: views.py with submit and show_exam_result functions
✅ **Task 6**: urls.py with paths for submit and show_exam_result
✅ **Task 7**: Screenshot of successful exam result with congratulations message
