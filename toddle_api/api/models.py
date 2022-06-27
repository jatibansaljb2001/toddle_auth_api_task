from turtle import mode
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User as Teacher


class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="classroom_list")

    def __str__(self):
        return f"Classroom {self.id} - {self.teacher}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=True, unique=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="student_list")

    def __str__(self):
        return f"{self.name}, {self.email}, {self.classroom}"

class ClassNotes(models.Model):
    FILE_TYPE_CHOICES =( 
    ("aud", "AUDIO"), 
    ("vid", "VIDEO"), 
    ("img", "IMAGE"), 
    ("url", "URL"), 
)
    classroom_id = models.ForeignKey(Classroom, related_name="classnotes_list", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    note = models.FileField(upload_to="notes")
    file_type = models.CharField(max_length=3, choices=FILE_TYPE_CHOICES)
    uploaded_by = models.ForeignKey(Teacher,related_name='teacher_notes',on_delete=models.CASCADE)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-uploaded_at']

class userProfile(models.Model):
    user = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name="profile")
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username