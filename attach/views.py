from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from  django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from attach import myFields
from .myFields import DayOfTheWeekField
from .models import Staff,StudentDetails,Student,Elogbook,Document,Lecturer
from django.views.generic import CreateView
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.files import File
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse


from django.shortcuts import render
from django.conf import settings
# Create your views here.

#views.py
from django.shortcuts import render, redirect  
from .forms import StudentForm,StudentDetailsForm,CompanyF1Form,LecturerF1Form,SignUpForm,LoginForm,CompDetailsForm,LecturerForm,StudentSignUpForm,SupervisorSignUpForm,ElogBookForm
from .models import Student
from attach import myFields
from .myFields import DayOfTheWeekField
# Create your views here.  
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from  django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from attach import myFields
from .myFields import DayOfTheWeekField
from django.views.generic import CreateView
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.files import File
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model

User = get_user_model()


def callindex(request):
    return render(request, 'lectures/videocall.html')

def callsupervisorindex(request):
    return render(request, 'supervisors/supervisorvideocall.html')

def callstudentindex(request):
    return render(request, 'students/studentvideocall.html')        

#register and login views
def lindex(request):
    return render(request,'logins/index.html')
    

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Your account has been sent for approval!')
            return redirect('login_view')
        else:
            message = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'logins/register.html',{'form':form})

def Supervisorregister(request):
    if request.method == 'POST':
        form = SupervisorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Your account has been sent for approval!')
            return redirect('login_view')
        else:
            message = 'form is not valid'
    else:
        form = SupervisorSignUpForm()
    return render(request,'logins/Supervisorregister.html',{'form':form})

def Studentregister(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Your account has been sent for approval!')
            return redirect('login_view')
        else:
            message = 'form is not valid'
    else:
        form = StudentSignUpForm()
    return render(request,'logins/Studentregister.html',{'form':form})



def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username =form.cleaned_data.get('username')
            password =form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None and user.is_admin:
                login(request,user)
                return redirect('adminpage')
            elif user is not None and user.is_lecturer: 
                login(request,user)
                return redirect('lecturer')
            elif user is not None and user.is_supervisor: 
                login(request,user)
                return redirect('supervisors')
            elif user is not None and user.is_student:  
                login(request,user)
                return redirect('viewstudent')    
            else:   
                msg = 'invalid credentials'
        else:       
            msg = 'error validating form'
    
    return render(request,'logins/login.html',{'form':form,'msg':msg})

#end of register and login views

#lecturer views


# @login_required
# def viewallassess(request):
#     if request.method == 'GET':
#         assess = Student.objects.all()
#     return render(request,'lectures/viewallAssessment.html',{'assess':assess})


def lecturer(request):
    return render(request,'lectures/index.html')  

@login_required
def viewallstudent(request):
    user = request.user
    dict={
    'total_student':StudentDetails.objects.all().count(),
    'total_student_company':CompDetails.objects.filter(university_name=user.university_name).count(),
    'total_student_assessed':Student.objects.filter(status="assessed").count(),
    'total_student_assessed_lecturer':Lecturer.objects.filter(status="assessed").count(),
    'students':StudentDetails.objects.filter(university_name=user.university_name),
    }
    
    # if request.method == 'GET':
    #     students = StudentDetails.objects.all()
    return render(request,'lectures/viewallstudent.html',context=dict)

@login_required
def viewCompanydetails(request):    
    user = request.user
    company = CompDetails.objects.filter(university_name=user.university_name)
    # if request.method == 'GET':
    #     company = CompDetails.objects.all()
    return render(request,'lectures/viewcompanydetails.html',{'company':company})



def lecturerassement(request):
    user = request.user
    students = Lecturer.objects.filter(status="assessed",university_name=user.university_name)
    supervisorassess = Student.objects.filter(status="assessed",university_name=user.university_name)
    return render(request,'lectures/lecturerassess.html',{'students':students,'supervisorassess':supervisorassess})

# @login_required
# def supervisorassessment(request):
#     supervisorassess = Student.objects.filter(status="assessed")
#     return render(request,'lectures/supervisorassessment.html',{'supervisorassess':supervisorassess})

@login_required
def getAssess(request, id):
    students = Student.objects.get(id=id)
    return render(request,'lectures/viewallAssessment.html',{'students':students})

@login_required
def logbookdetails(request):
    regnos = []
    user = request.user
    onelogbook = []
    logbook = Elogbook.objects.select_related().filter(student__university_name=user.university_name)
    for l in logbook:
        regnos.append(l.student.regno)
    keys = set(r for r in regnos)
        
    return render(request,'lectures/viewlogbook.html',{'logbook':keys})

@login_required
def logbookview(request, regno):
    print('before')
    logbooks = Elogbook.objects.filter(student__regno=regno)
    for p in logbooks:
        print(p)
    return render(request,'lectures/logbook.html',{'logbooks':logbooks})

@login_required
def reportview(request):
    user = request.user
    reports = Document.objects.filter(student__university_name=user.university_name)
    return render(request,'lectures/reportsview.html',{'reports':reports})

@login_required
def showassessed(request):
    user = request.user
    students = Lecturer.objects.filter(status="notassessed",university_name=user.university_name)
    return render(request,'lectures/assessed.html',{'students':students})

@login_required
def viewassess(request, id):
    student = Lecturer.objects.get(id=id)
    return render(request,'lectures/assessment.html',{'student':student})


@login_required    
def LecAssess(request, id):
    student = Lecturer.objects.get(id=id)
    return render(request,'lectures/lecAssessment.html',{'student':student})


@login_required    
def LecUpdate(request, id):  
    student = Lecturer.objects.get(id=id)  
    form = LecturerForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("viewall")  
    return render(request, 'lectures/lecAssessment.html', {'student': student})      
#end of lecturer views    








#supervisor views
def supervisor(request):
    return render(request,'supervisors/base.html')

def index(request):  
    user = request.user
    students = Student.objects.filter(status="notassessed",company_name=user.company_name)  
    return render(request,'supervisors/show.html',{'students':students})  

#assessment
@login_required    
def edit(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'supervisors/edit.html', {'student':student})  

@login_required    
def update(request, id):  
    student = Student.objects.get(id=id)  
    form = StudentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("assess")  
    return render(request, 'supervisors/edit.html', {'student': student})  
#delete assessment    
@login_required
def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/")

#filtering assess students
@login_required
def viewassessment(request):    
    user = request.user
    assessment = Student.objects.filter(status="assessed",company_name=user.company_name)
    return render(request,'supervisors/viewassessment.html',{'assessment':assessment})
#views assessment
@login_required
def view(request, id):
    student = Student.objects.get(id=id)
    return render(request,'supervisors/assessment.html',{'student':student})

@login_required
def Logbook(request):
    regnos = []
    user = request.user
    onelogbook = []
    logbook = Elogbook.objects.select_related().filter(company__company_name=user.company_name)
    for l in logbook:
        regnos.append(l.student.regno)
    keys = set(r for r in regnos)    
    return render(request,'supervisors/viewLogbook.html',{'logbook':keys})    


@login_required
def ViewLogbook(request, regno):
    logbooks = Elogbook.objects.filter(student__regno=regno)
    for p in logbooks:
        print(p)
    return render(request,'supervisors/Logbook.html',{'logbooks':logbooks}) 
#end of supervisor views    



#student views

def student(request):
    return render(request,'students/base.html')

# @login_required
# def ViewStudent(request):
#     user = User.objects.get(pk=request.user.id)
#     if request.method == 'GET':
#         if user is None:
#             return redirect('student')
            
#         else:   
#             stud = StudentDetails.objects.get(user=user)
            
#     return render(request,'students/viewstudent_details.html',{'user':user,'stud':stud})

@login_required
def ViewStudent(request):
    user = User.objects.get(pk=request.user.id)
    if user == None:
        student = StudentDetails.objects.filter(user_user=user)
    else:    
        student = StudentDetails.objects.filter(user=user)
    return render(request,'students/viewstudent_details.html',{'user':user,'student':student})




@login_required
def viewCompany(request):
    user = request.user
    student = request.GET.get('student')
    if student == None:
        company = CompDetails.objects.filter(student__user=user)
    else:    
        company = CompDetails.objects.filter(
            student__regno=coursename,student__user=user)
    students = StudentDetails.objects.filter(user=user)
    context = {'students':students,'company':company}
    return render(request,'students/ViewCompany.html',context)



@login_required 
def addStudent(request):
    if request.method  == 'POST':
        form = StudentDetailsForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            # obj.user = get_object_or_404(User, user=request.user.id)
            obj.user = User.objects.get(pk=request.user.id)
            obj.save()
            return redirect('viewstudent')
    else:   
        form = StudentDetailsForm()
    return render(request,'students/student_details.html',{'form':form})

def editstudentdetails(request,id):
    studentdetails = StudentDetails.objects.get(id=id)
    return render(request,'students/editstudentdetails.html',{'studentdetails':studentdetails})

def updatestudentdetails(request,id):    
    studentdetails = StudentDetails.objects.get(id=id)
    form = StudentDetailsForm(request.POST, instance=studentdetails)
    if form.is_valid():
        form.save()
        return redirect('viewstudent')
    return render(request,'students/editstudentdetails.html',{'studentdetails':studentdetails})


@login_required
def addCompany(request):
    if request.method == 'POST':
        form = CompanyF1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ViewCompany')
    else:        
        form = CompanyF1Form()
    return render(request,'students/company.html',{'form':form})        



@login_required
def editcompany(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'students/editcompany.html', {'student':student})  

@login_required
def updatecompany(request, id):  
    student = Student.objects.get(id=id)  
    form = StudentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect('ViewCompany')  
    return render(request, 'students/editcompany.html', {'student': student})  


@login_required
def report(request):    
    user = request.user
    student = request.GET.get('student')
    if student == None:
        reports = Document.objects.filter(student__user=user)
    else:
        reports = Document.objects.filter(
            student__regno=coursename,student__user=user)
    students = StudentDetails.objects.filter(user=user)
    context = {'students':students,'reports':reports}
    return render(request,'students/reports_view.html',context) 

@login_required
def viewCompany(request):
    user = request.user
    student = request.GET.get('student')
    if student == None:
        company = CompDetails.objects.filter(student__user=user)
    else:    
        company = CompDetails.objects.filter(
            student__regno=coursename,student__user=user)
    students = StudentDetails.objects.filter(user=user)
    context = {'students':students,'company':company}
    return render(request,'students/ViewCompany.html',context)


#view for showing elogbook
@login_required
def elogbook(request):  
    user = request.user
    student = request.GET.get('student')
    if student == None:
        elogbooks = Elogbook.objects.filter(student__user=user)
    else:
        elogbooks = Elogbook.objects.filter(
            student__regno=coursename,student__user=user)
    students = StudentDetails.objects.filter(user=user)
    context = {'students':students,'elogbooks':elogbooks}
    return render(request,'students/elogbook.html',context) 



#adding details to elogbook
@login_required(login_url='login')
def elogbook_entry(request):
    user = request.user
    # company = request.company

    students = user.studentdetails_set.all()
    # companys = StudentDetails.compdetails_set.all()

    if request.method == 'POST':
        student = request.POST.get('student')
        company = request.POST.get('company')
        workdone = request.POST.get('workdone')
        skills = request.POST.get('skills')
        mdate = request.POST.get('mdate')
        dayOfTheWeek = request.POST.get('dayOfTheWeek')
        data = request.POST

        if data['student'] != 'none': 
            student = StudentDetails.objects.get(id=data['student'])
            # company = CompDetails.objects.get(id=data['company'])
        else:   
            student = None
            # company = None
        elogbook = Elogbook.objects.create(
            student=student,
            # company=company,
            workdone =workdone,
            skills = skills,
            mdate=mdate,
            dayOfTheWeek=dayOfTheWeek,

            )
        return redirect('logbook')
    context = {'students':students}
    return render(request,'students/elog.html',context) 

def editlog(request,id):
    logbook = Elogbook.objects.get(id=id)
    return render(request,'students/editlog.html',{'logbook':logbook})

def updatelog(request,id):    
    logbook = Elogbook.objects.get(id=id)
    form = ElogBookForm(request.POST, instance=logbook)
    if form.is_valid():
        form.save()
        return redirect('logbook')
    return render(request,'students/editlog.html',{'logbook':logbook})

@login_required
def deletelogbook(request):
    id = request.GET.get('id',None)
    Elogbook.objects.get(id=id).delete()
    response_data = {
        'deleted':True
    }
    return JsonResponse(response_data)
    
def skytry(request):
    user = request.user
    students = user.studentdetails_set.all()

    if request.method == 'POST':
        student = request.POST.get('student')
        name = request.POST.get('name')

        data = request.POST

        if data['student'] != 'none':
            student = StudentDetails.objects.get(id=data['student'])
        else:    
            student = None

        sky = Sky.objects.create(
            student = student,
            name = name,
            )
    return render(request,'students/sky.html',{'students':students})        


@login_required
def compdet(request):
    user = request.user
    students = user.studentdetails_set.all()

    if request.method == 'POST':
        student = request.POST.get('student')
        s_fullname = request.POST.get('s_fullname')
        university_name = request.POST.get('university_name')
        registration_no = request.POST.get('registration_no')
        phone_number = request.POST.get('phone_number')
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        county = request.POST.get('address')
        company_phone_no = request.POST.get('company_phone_no')
        supervisor_name = request.POST.get('supervisor_name')
        # form = CompDetailsForm(request.POST)

        data = request.POST

        if data['student'] != 'none':
            student = StudentDetails.objects.get(id=data['student'])
            # form.save()
        else:    
            student = None
        company = CompDetails.objects.create(
            student = student,
            s_fullname=s_fullname,
            university_name=university_name,
            registration_no = registration_no,
            phone_number = phone_number,
            company_name = company_name,
            address = address,
            county = county,
            company_phone_no = company_phone_no,
            supervisor_name = supervisor_name,

            )
        comp = Student.objects.create(
            s_fullname = s_fullname,
            university_name=university_name,
            registration_no = registration_no,
            phone_number = phone_number,
            company_name = company_name,
            address = address,
            county = county,
            company_phone_no = company_phone_no,
            supervisor_name = supervisor_name,
            )
        lec = Lecturer.objects.create(
            s_fullname = s_fullname,
            university_name=university_name,
            registration_no = registration_no,
            phone_number = phone_number,
            company_name = company_name,
            address = address,
            county = county,
            company_phone_no = company_phone_no,
            supervisor_name = supervisor_name,
            )
        return redirect('ViewCompany')
    return render(request,'students/companydetails.html',{'students':students})
 

#uploading report to database   
@login_required
def model_form_upload(request):
    user = request.user

    students = user.studentdetails_set.all()
    
    if request.method == 'POST':
        student = request.POST.get('student')
        document = request.FILES.get('document')
        
        data = request.POST

        if data['student'] != 'none':
            student = StudentDetails.objects.get(id=data['student'])
        else:   
            student = None
        documents = Document.objects.create(
            student=student,
            document=document,
            
            )
        return redirect('view_report')
    context = {'students':students}
    return render(request,'students/model_form_upload.html',context)



#end studentviews    



def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')



