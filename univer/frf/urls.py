from django.urls import path
from .views import *


urlpatterns = [
    path('', FacultyViewSet.as_view({'get': 'list', 'post': 'create'}), name='faculty_list'),
    path('<int:pk>/', FacultyViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='faculty_detail'),

    path('professor/', ProfessorViewSet.as_view({'get': 'list', 'post': 'create'}), name='professor_list'),
    path('professor/<int:pk>/', ProfessorViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='professor_detail'),

    path('student/', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student_list'),
    path('student/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='student_detail'),

    path('course/', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='course_list'),
    path('course/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='course_detail'),

    path('classroom', ClassroomViewSet.as_view({'get': 'list', 'post': 'create'}), name='classroom_list'),
    path('classroom/<int:pk>/', ClassroomViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='classroom_detail'),

    path('schedule/', ScheduleViewSet.as_view({'get': 'list', 'post': 'create'}), name='schedule_list'),
    path('schedule/<int:pk>/', ScheduleViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='schedule_detail'),

    path('enrollment/', EnrollmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='enrollment_list'),
    path('enrollment/<int:pk>/', EnrollmentViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='enrollment_detail'),






]