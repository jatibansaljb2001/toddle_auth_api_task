from wsgiref import validate
from rest_framework import serializers
from .models import Teacher, ClassNotes, Student, Classroom, userProfile


class StudentSerializer(serializers.ModelSerializer):
    student_id = serializers.PrimaryKeyRelatedField(read_only=True, source="id")
    class Meta:
        model = Student
        fields = ["student_id", "name", "email", "classroom"]

class TeacherSerializer(serializers.ModelSerializer):
    #  To confirm the password field use password2 field
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only = True)
    teacher_id = serializers.PrimaryKeyRelatedField(read_only=True, source='id')
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'username', 'password', 'password2', 'email']
        
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    # Validate password and confirm password while registartion
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if(password != password2):
            raise serializers.ValidationError('Confirm password does not match')
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        teacher = Teacher.objects.create_user(**validated_data)
        return teacher
    
    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.email = validated_data['email']
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class ClassroomSerializer(serializers.ModelSerializer):
    classroom_id = serializers.PrimaryKeyRelatedField(source='id', read_only=True)
    teacher = serializers.CharField(source='teacher.username', read_only=True)
    class Meta:
        model = Classroom 
        fields = ['classroom_id', 'teacher']

class ClassNotesSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.CharField(source='uploaded_by.username', read_only=True)
    class Meta:
        model = ClassNotes
        fields = ['id', 'name', 'note', 'file_type', 'uploaded_by', 'classroom_id', 'description']

class StudentListSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all(),source='classroom.id')
    classNotes = ClassNotesSerializer(many=True, source="classroom.classnotes_list", read_only=True)
    class Meta:
        model = Student
        fields = ["name", "email", "classroom", "classNotes"]

class ClassroomListSerializer(serializers.ModelSerializer):
    classroom_id = serializers.PrimaryKeyRelatedField(source='id', read_only=True)
    teacher  = serializers.CharField(source='teacher.username', read_only=True)
    student_list = StudentSerializer(many=True, read_only=True)
    class Meta:
        model = Classroom
        fields = ['classroom_id', "teacher", "student_list"]

class TeacherListSerializer(serializers.ModelSerializer):
    classrooms = ClassroomListSerializer(many=True, read_only=True, source='classroom_list')
    class Meta:
        model = Teacher
        fields = ['id', 'username', 'email', 'classrooms']

class ClassNotesListSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.CharField(source='uploaded_by.username', read_only=True)
    class Meta:
        model = ClassNotes
        fields = ['id', 'name', 'note', 'file_type', 'uploaded_by', 'classroom_id', 'description']

class userProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = userProfile
        fields = '__all__'