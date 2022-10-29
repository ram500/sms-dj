from django.contrib.auth.models import Group, User, auth
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import Student, Teacher

import school_management_system
app_name = school_management_system

# Create your views here.

def teacher_register(request):
    
    if request.method=='POST':
        reg_id = request.POST['registration_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        full_name = request.POST['full_name']
        username = request.POST['username']
        mobile_no = request.POST['mobilenum']
        email = request.POST['email']
        gender = request.POST['gender']
        date_of_birth = request.POST['dob']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['zip']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        salary = request.POST['salary']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('teacher_registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('teacher_registration')  
            else:      
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                data = Teacher.objects.create(registration_id=reg_id,first_name=first_name,last_name=last_name,full_name=full_name,username=username,date_of_birth=date_of_birth,email=email,mobile_number=mobile_no,gender=gender,address=address,city=city,pincode=pincode,state=state,country=country,father_name=father_name,mother_name=mother_name,password=password1,salary=salary)
                data.save()
                my_admin_group = Group.objects.get_or_create(name='TEACHER')
                my_admin_group[0].user_set.add(user)
                messages.success(request,'Teacher added sucessfully')
                return redirect('/admin_teachers')

        else:
            messages.info(request,'password not matching')
            return redirect('teacher_registration') 

    else:             
        return render(request,'teacher_registration.html')


def student_register(request):
    if request.method == 'POST':
        reg_id = request.POST['registration_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        full_name = request.POST['full_name']
        username = request.POST['username']
        mobile_no = request.POST['mobilenum']
        email = request.POST['email']
        gender = request.POST['gender']
        date_of_birth = request.POST['dob']
        class_no = request.POST['class']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['zip']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        fees = request.POST['fees']
        

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('student_registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('student_registration')  
            else:      
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                data = Student.objects.create(registration_id=reg_id,first_name=first_name,last_name=last_name,full_name=full_name,username=username,date_of_birth=date_of_birth,email=email,mobile_number=mobile_no,gender=gender,address=address,city=city,pincode=pincode,state=state,country=country,class_no=class_no,father_name=father_name,mother_name=mother_name,password=password1,fees=fees)
                data.save()
                my_admin_group = Group.objects.get_or_create(name='STUDENT')
                my_admin_group[0].user_set.add(user)
                
                messages.success(request,'Student added sucessfully')
                return redirect('/admin_students')

        else:
            messages.info(request,'password not matching')
            return redirect('student_registration') 

    else:             
        return render(request,'student_registration.html')


def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        
        if user is not None:
            if user.groups.filter(name='ADMIN').exists():
                login(request, user)
                return redirect("/")  

            elif user.groups.filter(name='TEACHER').exists():
                login(request, user)
                return redirect("/teacher_dashboard") 

            elif user.groups.filter(name='STUDENT').exists():
                login(request, user)
                return redirect("/student_dashboard")      

            else:
                return redirect('login')
            
        else:
            print('user is not found')
            return redirect('login')

    else:
        return render(request,'login.html')        


def view_logout(request):
    logout(request)
    return redirect('login')        