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
from djano_pro1.views import FirstClassBaseView
from djano_pro1.views import GreetingView
from djano_pro1.views import ReturnJsonData
from djano_pro1.views import ReturnJsonDataChild
from djano_pro1.views import Calculaterclass
from djano_pro1.views import ContactFormView
from djano_pro1.views import ClassView
from djano_pro1.views import EmpDataListView
from djano_pro1.views import EmployeeInfo




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
    path('classview/', FirstClassBaseView.as_view()),
    path('inturl/<int:parameter>',views.JasonDataInt),
    path('strurl/<str:parameter>',views.JasonDataStr),
    path('slugurl/<slug:parameter>',views.JasonDataSlug),
    path('url/<parameter>',views.JasonData),
    path('class-view-var/', GreetingView.as_view(greeting='Hello khaqqan what are you doing')),
    path('classview-return-json/',ReturnJsonData.as_view()),
    path('classchildview-return-json/',ReturnJsonDataChild.as_view(), name='chilview'),
    path('calculater-class-view/',Calculaterclass.as_view(), name='calculater-class-view'),
    path('contactform/', views.contact_form, name='contactform'),
    path('contactform-class-view/',ContactFormView.as_view(), name='contactform-class-view'),
    path('fucntion-view/', views.functionview,{'template':'test.html'}, name='function-view'),
    path('fucntion-view2/', views.functionview, {'template':'test2.html'}, name='function-view'),
    path('class-view/', ClassView.as_view(template='test.html'), name='class-view'),
    path('class-view2/', ClassView.as_view(template='test2.html'), name='class-view2'),
    path('class-listview/', EmpDataListView.as_view(), name='class-listview'),
    path('classview-return-http/',EmployeeInfo.as_view(), name='classview'),
]
