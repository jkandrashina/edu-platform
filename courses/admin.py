from django.contrib import admin

from courses.models import (
    Course,
    Lesson,
    Student,
    StudentsGroup,
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_start', 'price', 'id')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(StudentsGroup)
class StudentsGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'course')
    