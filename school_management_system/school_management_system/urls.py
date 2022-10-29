"""school_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from school_management_system import views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.admin_dashboard),
    path('admin_teachers', views.admin_teacher),
    path('admin_students', views.admin_students),
    path('teacher_dashboard', views.teacher_dashboard),
    path('student_dashboard', views.student_dashboard),
    path('student_details', views.student_details),
    path('teacher_details', views.teacher_details),
    path('view_student_details/<int:id>', views.view_student_details, name='view_student_details'),
    path('view_teacher_details/<int:id>', views.view_teacher_details, name='view_teacher_details'),
    path('update_student_details', views.update_student_details),
    path('update_teacher_details', views.update_teacher_details),
    path('pay_fees', views.pay_fee),
    path('fee_receipt', views.fee_recipt),
    path('fee_details', views.fee_details),
    path('student_fee_details', views.student_fee_details),
    path("accounts/", include('accounts.urls')),
     
]
