from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    instructor_name = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True)
    def __str__(self):
        return self.course_name

class details(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    sp = models.CharField(max_length=500)
    il = models.CharField(max_length=500)
    def __str__(self):
        return self.sp
