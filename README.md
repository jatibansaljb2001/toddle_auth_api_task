# toddle_auth_api_task

It is a simple stateless microservice with few API endpoints:

   Note: All the Rest Endpoints can be accessed using LocalHost or Allowed Host.

#Authentication endpoint
'api/token/' uses TokenObtainPairView to generate JWT Auth token.
'api/token/refresh' uses TokenRefreshView to generate JWT Auth token.

#REST API endpoints for a Class Files app
    ● [Create] - POST 'teachers/' uses views.TeacherList to create Teacher.
    ● [List] - POST 'teachers/list/' uses views.TeacherListView to list Teacher with Classrooms.
    ● [Retrieve] - GET 'teachers/<int:pk>' uses views.TeacherDetail to get Teacher with id=pk.
    ● [Update] - PUT 'teachers/<int:pk>' uses views.TeacherDetail to update Teacher with id=pk.
    ● [Delete] - DELETE 'teachers/<int:pk>' uses views.TeacherDetail to delete Teacher with id=pk.

   ● [List] GET 'students/' uses views.StudentList to list Student.
   ● [Create] - POST 'students/' uses views.StudentList to create Student.
    ● [ListWithNotes] - POST 'students/list/' uses views.StudentListView to list All Student with Notes.
    ● [Retrieve] - GET 'students/<int:pk>' uses views.StudentDetail to get Student with id=pk.
    ● [Update] - PUT 'students/<int:pk>' uses views.StudentDetail to update Student with id=pk.
    ● [Delete] - DELETE 'students/<int:pk>' uses views.StudentDetail to delete Student with id=pk.

   ● [List] - GET 'classroom/' uses views.ClassroomList to list Classroom.
    ● [Create] - POST 'classroom/' uses views.ClassroomList to create Classroom.
    ● [Retrieve] - GET 'classroom/<int:pk>' uses views.ClassroomDetail to get Classroom with id=pk.
    ● [Delete] - DELETE 'classroom/<int:pk>' uses views.ClassroomDetail to delete Classroom with id=pk.

   ● [List] GET 'classnotes/' uses views.ClassNotesList to list Classnotes.
    ● [Create] - POST 'classnotes/' uses views.ClassNotesList to create Classnotes.
    ● [Search Filter] - POST 'classnotes/list/?search' uses views.ClassNotesListView to search with file name and file type.
    ● [Retrieve] - GET 'classnotes/<int:pk>' uses views.ClassNotesDetail to get Classnotes with id=pk.
    ● [Update] - PUT 'classnotes/<int:pk>' uses views.ClassNotesDetail to update Classnotes with id=pk.
    ● [Delete] - DELETE 'classnotes/<int:pk>' uses views.ClassNotesDetail to delete Classnotes with id=pk.