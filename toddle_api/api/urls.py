from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('students/', views.StudentList.as_view(), name='student-details'),
    path('students/list/', views.StudentListView.as_view(), name='studentlist_view'),
    path('students/<int:pk>', views.StudentDetail.as_view(), name='student-details'),

    path('teachers/', views.TeacherList.as_view(), name='teacher-details'),
    path('teachers/list/', views.TeacherListView.as_view(), name='teacherlist_view'),
    path('teachers/<int:pk>', views.TeacherDetail.as_view(), name="teacher-changes"),

    path('classroom/', views.ClassroomList.as_view(), name="classroom-list"),
    path('classroom/list/', views.ClassroomListView.as_view(), name="classroom_view"),
    path('classroom/<int:pk>', views.ClassroomDetail.as_view(), name="classroom-details"),

    path('classnotes/', views.ClassNotesList.as_view(), name="classNotes-list"),
    path('classnotes/list/', views.ClassNotesListView.as_view(), name="classNotes_view"),
    path('classnotes/<int:pk>', views.ClassNotesDetail.as_view(), name="classNotes-details"),

    path('api/token/', TokenObtainPairView.as_view(), name="get-token"),
    path('api/token/refresh', TokenRefreshView.as_view(), name="refresh-token"),

    path('all_profiles/', views.UserProfileListCreateView.as_view(), name="all-profiles"),
    path('profile/<int:pk>', views.userProfileDetailView.as_view(), name="profile"),
]