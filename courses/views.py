import datetime

from django.contrib.auth.models import Group
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import CreateView

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from courses.forms import (
    StudentSignUpForm,
    TeacherSignUpForm,
)

from courses.models import (
    Course,
    Student,
)

from courses.serializers import (
    CourseSerializer,
    CourseLessonSerializer,
)


class CourseListView(APIView):
    def get(self, request, *args, **kwargs):
        courses = Course.objects.prefetch_related('lessons').annotate(lessons_count=Count('lessons'))
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CourseLessonsListView(APIView):
    def get(self, request, username, course_id, *args, **kwargs):
        user = Student.objects.filter(user__username=username).filter(courses=course_id)
        
        if not user:
            return Response(
                {'res': f'{username} не входит в число студентов платформы или не записан на данный курс'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        lessons_list = Course.objects.filter(id=course_id).prefetch_related('lessons')
        serializer = CourseLessonSerializer(lessons_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentSignUpView(CreateView):
    form_class = StudentSignUpForm
    template_name = 'courses/student-signup.html'
    success_url = '/'
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        user.groups.add(Group.objects.get(name='student'))
        return super().form_valid(form)


class TeacherSignUpView(CreateView):
    form_class = TeacherSignUpForm
    template_name = 'courses/teacher-signup.html'
    success_url = '/'
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        user.groups.add(Group.objects.get(name='teacher'))
        return super().form_valid(form)
