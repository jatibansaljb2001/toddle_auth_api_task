# From API App
from distutils.command import upload
from logging import Filter
from msilib.schema import Class
from warnings import filters
from api.serializers import StudentSerializer, TeacherSerializer,  ClassroomSerializer, ClassNotesSerializer, userProfileSerializer, ClassroomListSerializer, TeacherListSerializer, StudentListSerializer, ClassNotesListSerializer
from api.models import Teacher, Student, Classroom, ClassNotes, userProfile
from api.permission import IsOwnerProfileOrReadOnly

#  Rest Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import filters


class TeacherList(APIView):
    """
    {Get] List all teachers, or [Post] create a new teacher. 
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        teachers = Teacher.objects.all()
        serializers = TeacherSerializer(teachers, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetail(APIView):
    """
    [Get] Retrieve, [Put] update or [Delete] delete a teacher.
    """
    permission_classes = [IsAuthenticated]
    # To Get Teacher  instance
    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return Response({"Error": "TeacherID: {} does not exist".format(pk)}, status=status.HTTP_400_BAD_REQUEST)  # doubt
        
    def get(self, request, pk):
        try:
            teacher = self.get_object(pk=pk)
            serializer = TeacherListSerializer(teacher)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Error": "TeacherID: {} does not exist.".format(pk)}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            teacher = self.get_object(pk)
            serializer = TeacherSerializer(teacher, data=request.data)
            if serializer.is_valid(raise_exception=True):
                # teacher.set_password(serializer.data.)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Error": "TeacherID: {} does not exist".format(pk)}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            teacher = self.get_object(pk=pk)
            teacher.delete()
            return Response({"Success": "Teacher is deleted."}, status=status.HTTP_200_OK)
        except:
            return Response({"Error": "TeacherID: {} does not exist".format(pk)}, status=status.HTTP_400_BAD_REQUEST)

class StudentList(APIView):
    """
    [Get] List all students, or [Post] create a new student
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    """
    [Get] Retrieve, [Put] update or [Delete] delete a student
    """
    permission_classes = [IsAuthenticated]
    # To get the student instance
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"Error": "StudentID: {} does not exist".format(pk)}, status=status.HTTP_400_BAD_REQUEST) # doubt

    def get(self, request, pk):
        try:
            student = self.get_object(pk)
            serializer = StudentListSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Error": "StudentID: {} does not exist.".format(pk)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            student = self.get_object(pk)
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Error": "StudentID: {} does not exist".format(pk)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response({"Success": "Student is deleted."},status=status.HTTP_204_NO_CONTENT)

class ClassroomList(APIView):
    """
    [Get] List all classroom, or [Post] create a new classroom
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['teacher'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClassroomDetail(APIView):
    """
    [Get] Retrieve a Classroom, [Delete] Delete a Classroom
    """
    permission_classes = [IsAuthenticated]
    # To get Classroom Intstance
    def get_object(self, pk):
        try:
            return Classroom.objects.get(pk=pk)
        except Classroom.DoesNotExist:
            return Response({"Error": "Classroom does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        try:
            classroom = self.get_object(pk)
            serializer = ClassroomListSerializer(classroom)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Error": "Classroom does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        classroom = self.get_object(pk)
        classroom.delete()
        return Response({"Success": "Classroom is Deleted."},status=status.HTTP_204_NO_CONTENT)

class ClassNotesList(APIView):
    """
    [Get] List all Notes, or [Post] create a new Class Notes
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request):
        try:
            classroom_id = request.GET['classroom_id']
            if classroom_id is not None:
                classNotes = ClassNotes.objects.filter(classroom_id = classroom_id)
                serializer = ClassNotesSerializer(classNotes, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            classNotes = ClassNotes.objects.all()
            serializer = ClassNotesSerializer(classNotes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClassNotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['uploaded_by'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassNotesDetail(APIView):
    """
    [Get] Retrieve, [Put] update or [Delete] delete a student
    """
    permission_classes = [IsAuthenticated]
    # To get the student instance
    def get_object(self, pk):
        try:
            return ClassNotes.objects.get(pk=pk)
        except ClassNotes.DoesNotExist:
            return Response({"Error": "NotesID: {} does not exist".format(pk)}, status=status.HTTP_400_BAD_REQUEST) # doubt

    def get(self, request, pk):
        try:
            classNotes = self.get_object(pk)
            serializer = ClassNotesSerializer(classNotes)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Error": "NotesID: {} does not exist.".format(pk)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        classNotes = self.get_object(pk)
        serializer = ClassNotesSerializer(classNotes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        classNotes = self.get_object(pk)
        classNotes.delete()
        return Response({"Success": "Note is deleted."},status=status.HTTP_204_NO_CONTENT)

class TeacherListView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
    pagination_class = PageNumberPagination
        
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    pagination_class = PageNumberPagination
    permission_classes=[IsAuthenticated]

class ClassroomListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

class ClassNotesListView(ListAPIView):
    queryset = ClassNotes.objects.all()
    serializer_class = ClassNotesListSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields  = ['name', 'file_type']

class UserProfileListCreateView(ListCreateAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly]
