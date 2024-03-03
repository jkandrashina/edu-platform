from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    min_students_in_group = models.PositiveIntegerField(
        default=1,
        verbose_name='Минимальное количество студентов в группе'
    )
    max_students_in_group = models.PositiveIntegerField(
        default=10,
        verbose_name='Максимальное количество студентов в группе'
    )
    date_start = models.DateField(
        verbose_name='Дата старта'
    )
    time_start = models.TimeField(
        verbose_name='Время старта'
    )
    price = models.PositiveIntegerField(
        verbose_name='Стоимость'
    )
    
    class Meta:
        verbose_name = ('Курс')
        verbose_name_plural = ('Курсы')
    
    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Студент'
    )
    courses = models.ManyToManyField(
        Course,
        related_name='students',
        verbose_name='Курс'
    )
    
    class Meta:
        verbose_name = ('Студент')
        verbose_name_plural = ('Студенты')
    
    def __str__(self):
        return self.user.username


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name='Курс'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    video_url = models.URLField(
        max_length=200,
        verbose_name='Ссылка на видео'
    )
    
    class Meta:
        verbose_name = ('Урок')
        verbose_name_plural = ('Уроки')
    
    def __str__(self):
        return self.title


class StudentsGroup(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс'
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Студент'
    )
    group_name = models.CharField(
        max_length=100,
        verbose_name='Название группы'
    )
    
    class Meta:
        verbose_name = ('Группа курса')
        verbose_name_plural = ('Группы курса')
    
    def __str__(self):
        return self.group_name    

