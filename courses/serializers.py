from rest_framework import serializers
from courses.models import (
    Course,
    Lesson,
    Student,
)


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField()
    
    class Meta:
        model = Course
        fields = ('title', 'date_start', 'time_start', 'price', 'lessons_count')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('title',)


class CourseLessonSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(
        many=True,
        read_only=True
    )
    
    class Meta:
        model = Course
        fields = ('title', 'lessons',)

