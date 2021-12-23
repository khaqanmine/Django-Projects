"""djano_pro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from djano_pro1 import views
from djano_pro1.views import firstClassbaseView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',views.homepage),
    path('about-us/',views.aboutus),
    path('calculater/',views.calculater),
    path('grocery-bill/',views.grocery),
    path('even-odd/',views.checkoddeven),
    path('school-management/',views.startdevelopment),
    path('teacherdata/',views.teacherdata, name='teacherdata'),
    path('student_data/',views.studentData, name='studata'),
    path('jsondata/',views.jasondata),
    path('homepage/<int:year>', views.Urlwithparameters),
    path('classview/', firstClassbaseView.as_view()),
]
