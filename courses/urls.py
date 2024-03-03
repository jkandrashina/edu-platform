from django.urls import path

from courses.views import (
    CourseListView,
    CourseLessonsListView,
    StudentSignUpView,
    TeacherSignUpView,
)


urlpatterns = [
    path('courses/', CourseListView.as_view()),
    path('<str:username>/<int:course_id>/', CourseLessonsListView.as_view()),
    path('student-signup/', StudentSignUpView.as_view(), name='student-signup'),
    path('teacher-signup/', TeacherSignUpView.as_view(), name='teacher-signup'),
]