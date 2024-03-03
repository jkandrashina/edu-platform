from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from courses.models import (
    Student,
    StudentsGroup,
    Course,
)

@receiver(post_save, sender=StudentsGroup)
def create_student(sender, instance, created, **kwargs):
    if created:
        students = Student.objects.filter(courses=instance.course.id)
        print(students)
        print(instance)
        if students:
            for student in students:
                instance.student = student
                instance.save()