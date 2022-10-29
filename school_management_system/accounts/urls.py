from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('teacher_registration', views.teacher_register, name='teacher_registration'),
    path('student_registration', views.student_register, name='student_registration'),
    path('login', views.view_login, name='login'),
    path('logout', views.view_logout, name='logout'),
]