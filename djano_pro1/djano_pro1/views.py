from django.http import HttpResponse, request
from django.shortcuts import render
# from .forms import calculaterForm
from .forms import groceryBill
from .forms import checkEvenOdd
from .forms import ContactForm
from .forms import StudentData
from contactform.models import ContactFormModel
from studentinfo.models import StudentInfo
from teacherdata.models import TeacherData
from django.http import JsonResponse
import json
from django.views import View
from django.views.generic.list import ListView
from employee_data.models import EmployeeData
def startdevelopment(request):
    return render(request,'1stapp.html')

def homepage(request):
    return render(request, 'index.html')

def aboutus(request):
    return HttpResponse('Welcome')
def calculater(request):
    cal=''
    try:
        if request.method=='POST':
            num_1=eval(request.POST.get('num1'))
            num_2=eval(request.POST.get('num2'))
            opreration = request.POST.get('opr')
            if opreration =='+':
                cal = num_1 + num_2
            elif opreration =='-':
                cal = num_1 - num_2
            elif opreration =='/':
                cal = num_1 / num_2
            elif opreration =='*':
                cal = num_1 * num_2
            elif opreration =='%':
                cal = num_1 % num_2
    except:
        pass
    return render(request,'calculater.html',{'c':cal})
def grocery(request):
    gbill = groceryBill()
    data = {'gb':gbill}
    total=0
    try:
        if request.method=='POST':
            p_oil = int(request.POST.get('product_oil'))
            p_sugar = int(request.POST.get('product_sugar'))
            p_flour = int(request.POST.get('product_flour'))
            total = p_oil + p_sugar + p_flour
            data = {
                'gb':gbill,
                'output':total
            }
            
    except:
        pass
    return render(request,'grocery.html',data)

def checkoddeven(request):
    cls = checkEvenOdd()
    dic = {'classform':cls}
    try:
        if request.method=='POST':
           num = int(request.POST.get('number'))
           if num%2==0:
               number ='Number is Even'
           else:
               number = 'Number is Odd'
           dic = {
                'result':number,
                'classform':cls,
            }
        
    except:
        pass
    return render(request,'evenodd.html',dic)

def teacherdata(request):   
    if request.method=='POST':
        t_name = request.POST.get('name')
        t_phone = request.POST.get('phone')
        t_address = request.POST.get('address')
        t_salary = request.POST.get('salary')

        instances = TeacherData(name=t_name, phone=t_phone, address=t_address, salary=t_salary)
        instances.save()
    return render(request,'teacherdata.html')

def studentData(request):

    data = {'stu_form' : StudentData()}
    try:
        if request.method == 'POST':
            stu_name = request.POST.get('student_name')
            stu_roll_number = request.POST.get('student_roll_number')
            stu_gender = request.POST.get('student_gender')
            stu_father_name =request.POST.get('student_father_name')
            instances = StudentInfo(name=stu_name, roll_number=stu_roll_number, gender=stu_gender, father_name=stu_father_name)
            instances.save()
    except:
        print('Error Occurred Please Check')
        
    return render(request, 'studentdata.html', data)

def jasondata(request): # Return Json Data
    data = list(TeacherData.objects.values())
    return JsonResponse(data, safe=False)

class FirstClassBaseView(View):  # Class based views    
    def get(self, request):
        a = 'Class Based View'
        return HttpResponse(a)

def JasonDataInt(request,parameter): 
    return HttpResponse(parameter)

def JasonDataStr(request, parameter):
    return HttpResponse(parameter)

def JasonDataSlug(request, parameter):
    return HttpResponse(parameter)

def JasonData(request, parameter):
    return HttpResponse(parameter)

class GreetingView(View):
    greeting = ""
    def get(self, request):
        return HttpResponse(self.greeting)

class ReturnJsonData(View):
    name='Khaaqan'
    def get(self, request):
        data = list(TeacherData.objects.values())
        return JsonResponse(data, safe=False)

class ReturnJsonDataChild(ReturnJsonData):
    def get(self, request):
        return HttpResponse(self.name)

class Calculaterclass(View):
    def get(self, request):
        return render(request, 'calculater.html')

def contact_form(request):
    data = {'form': ContactForm()}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        return HttpResponse('Form Successfully Submitted')
    else:
        data = {'form': ContactForm()}
    return render(request, 'contactform.html', data)

class ContactFormView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contactform.html', {'form':form})
    def post(self, request):
         if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            instances = ContactFormModel(name=name, phone=phone, email=email)
            instances.save()
            return HttpResponse('Form Successfully Submitted')

def functionview(request, template):
    return render(request,template)

class ClassView(View):
    template=''
    def get(self,request):
        return render(request, self.template)
#ListView
class EmpDataListView(ListView):
    model = EmployeeData
#SimpleView
class EmployeeInfo(View):
    
    def get(self, request):
        data =  list(EmployeeData.objects.values())
        return HttpResponse(data, request)
    