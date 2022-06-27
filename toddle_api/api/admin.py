from django.contrib import admin
from api.models import Student, Classroom, ClassNotes


admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(ClassNotes)
