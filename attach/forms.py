from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Staff,StudentDetails,Student,Elogbook,Document,Lecturer,CompDetails
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class StudentForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = ['s_fullname','phone_number','registration_no','company_name','address','county','company_phone_no','supervisor_name','gender',
        'punctual','regulations','workmanship','workout','adaptability','commu','reliability','team_work','overall_assessment','general_remarks'
        ,'assessed_by','position','status','mdate'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 
            's_fullname': forms.TextInput(attrs={ 'class': 'form-control' }),
            'phone_number': forms.TextInput(attrs={ 'class': 'form-control' }),
            'registration_no': forms.TextInput(attrs={ 'class': 'form-control' }),
            'company_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'address': forms.TextInput(attrs={ 'class': 'form-control' }),
            'county':forms.TextInput(attrs={'class':'form-control'}),
            'company_phone_no': forms.TextInput(attrs={ 'class': 'form-control' }),
            'supervisor_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'gender':forms.RadioSelect(choices=Student.GENDER_CHOICE),
            'period_from': forms.DateInput(attrs={ 'class': 'form-control' }),
            'period_to': forms.DateInput(attrs={ 'class': 'form-control' }),
            'punctual':forms.RadioSelect(choices=Student.PERFOMANCE_CHOICE),
            'regulations':forms.RadioSelect(choices=Student.PERFOMANCE_CHOICE),
            'workmanship':forms.RadioSelect(choices=Student.PERFOMANCE_CHOICE),
            'workout':forms.RadioSelect(choices=Student.PERFOMANCE_CHOICE),
            'adaptability':forms.RadioSelect(choices=Student.PERFOMANCE_CHOICE),
            'commu':forms.RadioSelect(choices=Student.PERFOMANCE_CHOICE),
            'reliability':forms.RadioSelect(choices=Student.PERFOMANCE_CHOICE),
            'team_work':forms.RadioSelect(choices=Student.PERFOMANCE_CHOICE),
            'overall_assessment':forms.RadioSelect(choices=Student.PERFOMANCE_CHOICE),
            'general_remarks': forms.TextInput(attrs={ 'class': 'form-control' }),
            'assessed_by': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'position': forms.TextInput(attrs={ 'class': 'form-control' }),
            'status':forms.RadioSelect(choices=Student.STATUS),
            'mdate': forms.DateInput(attrs={ 'class': 'form-control' }),
      }

class CompDetailsForm(forms.ModelForm):
    class Meta:
        model = CompDetails
        fields = ['s_fullname','phone_number','registration_no','company_name','address','county','company_phone_no','supervisor_name']


class ElogBookForm(forms.ModelForm):  
    class Meta:  
        model = Elogbook
        fields = ['workdone', 'mdate', 'skills','dayOfTheWeek'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'workdone': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'skills': forms.TextInput(attrs={ 'class': 'form-control' }),
            'mdate': forms.DateInput(attrs={ 'class': 'form-control' }),
            'dayOfTheWeek': forms.TextInput(attrs={ 'class': 'form-control' }),
      }



class CompanyF1Form(forms.ModelForm):
    class Meta:
        model = Student
        s_fullname = forms.CharField(
            widget = forms.TextInput(
                attrs={
                "class":"form-control"
            }))
        registration_no = forms.CharField(
            widget = forms.TextInput(
                attrs={
                "class":"form-control"
                }))
        phone_number = forms.CharField(
            widget = forms.TextInput(
                attrs={
                "class":"form-control"
                }))
    
        company_name = forms.CharField(
            widget = forms.TextInput(
                attrs={
                "class":"form-control"
                }))
        address = forms.CharField(
            widget=forms.TextInput(
                attrs={
                "class":"form-control"
                }))
        county = forms.CharField(
            widget=forms.TextInput(
                attrs={
                "forms":"form-control"
                }))
        company_phone_no = forms.CharField(
            widget = forms.TextInput(
                attrs={
                "class":"form-control"
                }))
        supervisor_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                "class":"form-control"
                }))
        fields = ('s_fullname','registration_no','phone_number','company_name','address','county','company_phone_no','supervisor_name')

class LecturerForm(forms.ModelForm):  
    class Meta:  
        model = Lecturer 
        fields = ['s_fullname','phone_number','registration_no','company_name','address','county','company_phone_no','supervisor_name','gender',
        'punctual','regulations','workmanship','workout','adaptability','commu','reliability','team_work','overall_assessment','general_remarks'
        ,'assessed_by','position','status','mdate'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 
            's_fullname': forms.TextInput(attrs={ 'class': 'form-control' }),
            'phone_number': forms.TextInput(attrs={ 'class': 'form-control' }),
            'registration_no': forms.TextInput(attrs={ 'class': 'form-control' }),
            'company_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'address': forms.TextInput(attrs={ 'class': 'form-control' }),
            'county':forms.TextInput(attrs={'class':'form-control'}),
            'company_phone_no': forms.TextInput(attrs={ 'class': 'form-control' }),
            'supervisor_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'gender':forms.RadioSelect(choices=Lecturer.GENDER_CHOICE),
            'period_from': forms.DateInput(attrs={ 'class': 'form-control' }),
            'period_to': forms.DateInput(attrs={ 'class': 'form-control' }),
            'punctual':forms.RadioSelect(choices=Lecturer.PERFOMANCE_CHOICE),
            'regulations':forms.RadioSelect(choices=Lecturer.PERFOMANCE_CHOICE),
            'workmanship':forms.RadioSelect(choices=Lecturer.PERFOMANCE_CHOICE),
            'workout':forms.RadioSelect(choices=Lecturer.PERFOMANCE_CHOICE),
            'adaptability':forms.RadioSelect(choices=Lecturer.PERFOMANCE_CHOICE),
            'commu':forms.RadioSelect(choices=Lecturer.PERFOMANCE_CHOICE),
            'reliability':forms.RadioSelect(choices=Lecturer.PERFOMANCE_CHOICE),
            'team_work':forms.RadioSelect(choices=Lecturer.PERFOMANCE_CHOICE),
            'overall_assessment':forms.RadioSelect(choices=Lecturer.PERFOMANCE_CHOICE),
            'general_remarks': forms.TextInput(attrs={ 'class': 'form-control' }),
            'assessed_by': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'position': forms.TextInput(attrs={ 'class': 'form-control' }),
            'status':forms.RadioSelect(choices=Lecturer.STATUS),
            'mdate': forms.DateInput(attrs={ 'class': 'form-control' }),
      }


class LecturerF1Form(forms.ModelForm):
    class Meta:
        model = Lecturer
        s_fullname = forms.CharField(
            widget = forms.TextInput(
                attrs={
                "class":"form-control"
            }))
        registration_no = forms.CharField(
            widget = forms.TextInput(
                attrs={
                "class":"form-control"
                }))
        phone_number = forms.CharField(
            widget = forms.TextInput(
                attrs={
                "class":"form-control"
                }))
    
        company_name = forms.CharField(
            widget = forms.TextInput(
                attrs={
                "class":"form-control"
                }))
        address = forms.CharField(
            widget=forms.TextInput(
                attrs={
                "class":"form-control"
                }))
        county = forms.CharField(
            widget=forms.TextInput(
                attrs={
                "forms":"form-control"
                }))
        company_phone_no = forms.CharField(
            widget = forms.TextInput(
                attrs={
                "class":"form-control"
                }))
        supervisor_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                "class":"form-control"
                }))
        fields = ('s_fullname','registration_no','phone_number','company_name','address','county','company_phone_no','supervisor_name')


class StudentDetailsForm(forms.ModelForm):
    
    class Meta:
        model = StudentDetails
        student_name = forms.CharField(
            widget = forms.TextInput(
                attrs={
                "class":"form-control"
            }))
        coursename = forms.CharField(
            widget = forms.TextInput(
                attrs={
                "class":"form-control"
            }))
        regno = forms.CharField(
            widget = forms.TextInput(
                attrs={
                "class":"form-control"
                }))
        year_of_study = forms.CharField(
            widget = forms.TextInput(
                attrs={
                "class":"form-control"
                 }))
        school = forms.CharField(
            widget= forms.TextInput(
                attrs={
                "class":"form-control-label"
                }))


        fields =('student_name' ,'coursename','regno','year_of_study','school')
        def clean(self):
            cleaned_data = super().clean()
            user = cleaned_data.get('user')
            created = datetime.now().date()
            if Student.objects.filter(user=user, created=created).exists():
                raise forms.ValidationError("User already filles the form")


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
            "class":"form-control"
            }
            )
        )
    email = forms.CharField(
        widget = forms.TextInput(
            attrs={
            "class":"form-control"
            })
        )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
            "class":"form-control"
            }
            ))
    last_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
            "class":"form-control"
            }))
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
            "class":"form-control"
            }
            )
        )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
            "class":"form-control"
            }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','is_supervisor','is_student','is_lecturer','password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )



