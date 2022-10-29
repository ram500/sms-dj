from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from tomlkit import datetime
from accounts.models import Student, Teacher
from django.db.models import Sum
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login")
def home(request):
    return render(request, 'baseindex.html')  

@login_required(login_url="/accounts/login")
def admin_dashboard(request):
    studentcount=Student.objects.all().count()
    fees = Student.objects.aggregate(TOTAL = Sum('fees'))['TOTAL']
    fees_paid = Student.objects.aggregate(TOTAL = Sum('fees_paid'))['TOTAL']
    denomination = "K"
    denomination_paid = "K"
    pending_fees = fees - fees_paid

    if pending_fees >= 100000:
        denomination_paid = "L"
        fees = fees/100000
    elif pending_fees >= 10000000:
        denomination_paid = "Cr"
        fees = fees/10000000

    if fees >= 100000:
        denomination = "L"
        fees = fees/100000
    elif fees >= 10000000:
        denomination = "Cr"
        fees = fees/10000000

    teachercount=Teacher.objects.all().count()    

    my_dict = {
        'studentcount':studentcount,
        'total_fees':fees,
        'pending_fees':pending_fees,
        'denomination':denomination,
        'denomination_paid':denomination_paid,
        'teachercount':teachercount,
    }
    return render(request, 'admin_dashboard.html', context=my_dict)  

def admin_teacher(request):
    return render(request, 'admin_teachers.html') 

def admin_students(request):
    return render(request, 'admin_student.html')       

def pay_fee(request):
    if request.method == 'POST':
        if request.POST.get('reg_id'):
            
            id = request.POST['reg_id']
            stud = Student.objects.get(pk=id)
            pending_fees = stud.fees - stud.fees_paid
            dict={ 'student':stud, 'pending_fees':pending_fees, }
            return render(request, 'admin_payfees.html', context=dict)
        if request.POST.get('registration_id'):
            reg_id = request.POST['registration_id']
            currently_paid = request.POST['pay_fees']
            pending_fees = request.POST['pending_fees']
            stud = Student.objects.get(pk=reg_id)
            total_fees_paid = int(stud.fees_paid) + int(currently_paid)

            request.session['reg_id'] = reg_id
            request.session['currently_paid'] = currently_paid
            request.session['pending_fees'] = pending_fees

            Student.objects.filter(pk=reg_id,).update(fees_paid=total_fees_paid)
            return fee_recipt(request)
    return render(request, 'admin_payfees.html')

def fee_recipt(request):
    id = request.session['reg_id']
    details = Student.objects.get(pk=id)
    current_date = datetime.now().date()
    current_time = datetime.now().strftime('%H:%M:%S')
    currently_paid = request.session['currently_paid']
    pending_fees_past = request.session['pending_fees']
    pending_fee_now = details.fees - details.fees_paid
    dict={'details':details, 'today':current_date,'time':current_time,'currently_paid':currently_paid,'pending_fees_past':pending_fees_past,'pending_fees_now':pending_fee_now}
    
    return render(request, 'fee_recipt.html', context=dict )

def fee_details(request):
    return render(request, 'admin_fee_details.html')

def student_fee_details(request):
    stud = Student.objects.all()
    return render(request, 'student_fee_details.html',{'stu':stud,})

def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html') 
 
def student_dashboard(request):
    return render(request, 'student_dashboard.html') 

def student_details(request):
    if request.method == 'POST':
        id = request.POST['reg_id']
        stud = Student.objects.filter(registration_id=id)
        return render(request,'admin_student_details.html',{'stu':stud,})

    stud = Student.objects.all()
    return render(request,'admin_student_details.html',{'stu':stud,})

def teacher_details(request):
    if request.method == 'POST':
        id = request.POST['reg_id']
        stud = Teacher.objects.filter(registration_id=id)
        return render(request,'admin_student_details.html',{'teach':teach,})

    teach = Teacher.objects.all()
    return render(request,'admin_teacher_details.html',{'teach':teach,})
   

def view_student_details(request, id):
    
    details = Student.objects.get(pk=id)
    pending_fees = details.fees - details.fees_paid
    di = {'details':details, 'pending_fees':pending_fees}
    return render(request, 'admin_student_details_display.html', context=di )
        
def view_teacher_details(request, id):
    print(id)
    details = Teacher.objects.get(pk=id)
    
    di = {'details':details,}
    return render(request, 'admin_teacher_details_display.html', context=di )


def update_student_details(request):
    if request.method == 'POST':
        if request.POST.get('reg_id'):
            
            id = request.POST['reg_id']
            stud = Student.objects.get(pk=id)
            pending_fees = stud.fees - stud.fees_paid
            dict={ 'student':stud, 'pending_fees':pending_fees, }
            return render(request, 'update_student_details.html', context=dict)

        if request.POST.get('registration_id'):
            
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
            password = request.POST['password']
            paid_fees = request.POST['paid_fees']
            fees = request.POST['fees']

            user = User.objects.filter(username=username).get()
            user.username=username
            user.password=password
            user.email=email
            user.first_name=first_name
            user.last_name=last_name
            user.save()

            Student.objects.filter(pk=reg_id,).update(first_name=first_name,last_name=last_name,full_name=full_name,username=username,date_of_birth=date_of_birth,email=email,mobile_number=mobile_no,gender=gender,address=address,city=city,pincode=pincode,state=state,country=country,class_no=class_no,father_name=father_name,mother_name=mother_name,password=password,fees=fees,fees_paid=paid_fees)
            messages.success(request,'Student Updated Sucessfully !!!')
            return redirect('/admin_students')

    return render(request,'update_student_details.html')


def update_teacher_details(request):
    if request.method == 'POST':
        if request.POST.get('reg_id'):
            
            id = request.POST['reg_id']
            stud = Teacher.objects.get(pk=id)
            dict={ 'student':stud, }
            return render(request, 'update_teacher_details.html', context=dict)

        if request.POST.get('registration_id'):
            
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
            password = request.POST['password']
            salary = request.POST['salary']

            user = User.objects.filter(username=username).get()
            user.username=username
            user.password=password
            user.email=email
            user.first_name=first_name
            user.last_name=last_name
            user.save()

            Teacher.objects.filter(pk=reg_id,).update(first_name=first_name,last_name=last_name,full_name=full_name,username=username,date_of_birth=date_of_birth,email=email,mobile_number=mobile_no,gender=gender,address=address,city=city,pincode=pincode,state=state,country=country,father_name=father_name,mother_name=mother_name,password=password,salary=salary)
            messages.success(request,'Teacher Updated Sucessfully !!!')
            return redirect('/admin_teachers')

    return render(request,'update_teacher_details.html')