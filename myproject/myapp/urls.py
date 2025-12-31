from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('submit/', views.submit, name='submit'),
    path('exam-result/', views.show_exam_result, name='show_exam_result'),
]
