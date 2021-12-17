from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms.widgets import RadioSelect
from attach import myFields
from .myFields import DayOfTheWeekField
from datetime import date
from django.utils import timezone
from datetime import date
from django.core.files import File
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self,email,username,first_name,password,**other_fields):
        if not email:
            raise ValueError(_("Users must have an email address"))
        if not username:
            raise ValueError(_("Users must have an unique username"))
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
    
    def create_superuser(self,email,username,first_name,password,**other_fields):
            other_fields.setdefault('is_staff',True)
            other_fields.setdefault('is_superuser',True)
            other_fields.setdefault('is_active',True)
            if other_fields.get('is_staff') is not True:
                raise ValueError('is_staff is set to False')
            if other_fields.get('is_superuser') is not True:
                raise ValueError('is_superuser is set to False')
            return self.create_user(email,username,first_name,password,**other_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email         = models.EmailField(_('email address'),max_length=60,unique=True)
    username      = models.CharField(max_length=30,unique=True)
    first_name    = models.CharField(max_length=30,blank=True)
    last_name     = models.CharField(max_length=30,blank=True)
    phone_number  = models.CharField(max_length=20, verbose_name='phone number',null=True,blank=True)
    company_name  = models.CharField(max_length=50,blank=True)
    date_joined   = models.DateTimeField(verbose_name='date_joined',auto_now_add=True)
    last_login    = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)
    is_staff      = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name']

    def __str__(self):
        return self.username



# Create your models here.
YEAR_OF_STUDY = (
	('Yr1 Sem2','yr1 Sem2'),
	('yr2 Sem2','yr2 Sem2'),
	('yr3 Sem2','yr3 Sem2'),
	('yr4 Sem2','yr4 Sem2'),
	)
SCHOOL=(
	('SCI','SCI'),
	('SBE','SBE'),
	('SHS','SHS'),
	('SEA','SEA'),
	('SED','SED'),
	('SN','SN'),
	('SPAS','SPAS'),
	('SAFS','SAFS'),
	)
# class User(AbstractUser):
# 	is_admin = models.BooleanField(default=False)
# 	is_lecturer = models.BooleanField(default=False)
# 	is_supervisor = models.BooleanField(default=False)
# 	is_student = models.BooleanField(default=False)


class Staff(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	staff_name = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=50)
	school = models.CharField(max_length=100,choices=SCHOOL)

	class Meta:
		verbose_name_plural = "Staffs"

	def __str__(self):
		return self.staff_name



class StudentDetails(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	student_name = models.CharField(max_length=255)
	coursename = models.CharField(max_length=255)
	regno = models.CharField(max_length=100)
	year_of_study = models.CharField(max_length=100,choices=YEAR_OF_STUDY)
	school = models.CharField(max_length=100,choices=SCHOOL)
	created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.regno	

class CompDetails(models.Model):
	id = models.AutoField(primary_key=True)
	student = models.ForeignKey(StudentDetails,on_delete=models.DO_NOTHING)
	s_fullname = models.CharField(max_length=255)
	registration_no = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=100)
	company_name = models.CharField(max_length=200)
	address = models.TextField()
	county = models.CharField(max_length=200)
	company_phone_no = models.CharField(max_length=255)
	supervisor_name = models.CharField(max_length=255)

	def __str__(self):
		return self.s_fullname



class Elogbook(models.Model):
	id = models.AutoField(primary_key=True)
	student = models.ForeignKey(StudentDetails,on_delete=models.DO_NOTHING)
	workdone = models.TextField()
	skills = models.TextField(default=1)
	mdate = models.DateField(null=False, blank=False)
	dayOfTheWeek = myFields.DayOfTheWeekField()
	remarks = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Elogbook'
		verbose_name_plural = "Elogbooks"

	def __str__(self):	
		return self.workdone

class Document(models.Model):		
	student = models.ForeignKey(StudentDetails,on_delete=models.DO_NOTHING)
	document = models.FileField(upload_to='document/')
	uploaded_at = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
	GENDER_CHOICE = (
		('male','male'),
		('female','female'),
		)
	PERFOMANCE_CHOICE = (
		('excellent','excellent'),
		('good','good'),
		('average','average'),
		('fair','fair'),
		('poor','poor'),
		)
	STATUS = (
		('assessed','assessed'),
		('notassessed','notassessed'),
		)
	s_fullname = models.CharField(max_length=255)
	registration_no = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=100)
	company_name = models.CharField(max_length=200)
	address = models.TextField()
	county = models.CharField(max_length=200)
	company_phone_no = models.CharField(max_length=255)
	supervisor_name = models.CharField(max_length=255)
	gender = models.CharField(max_length=100,choices=GENDER_CHOICE)
	period_from = models.DateField(null=True, blank=True)
	period_to = models.DateField(null=True,blank=True)
	punctual = models.CharField(max_length=100,choices=PERFOMANCE_CHOICE)
	regulations = models.CharField(max_length=100,choices=PERFOMANCE_CHOICE)
	workmanship = models.CharField(max_length=100,choices=PERFOMANCE_CHOICE)
	workout = models.CharField(max_length=100,choices=PERFOMANCE_CHOICE)
	adaptability = models.CharField(max_length=100,choices=PERFOMANCE_CHOICE)
	commu = models.CharField(max_length=100,choices=PERFOMANCE_CHOICE)
	reliability = models.CharField(max_length=100,choices=PERFOMANCE_CHOICE)
	team_work = models.CharField(max_length=100,choices=PERFOMANCE_CHOICE)
	overall_assessment = models.CharField(max_length=100,choices=PERFOMANCE_CHOICE)
	general_remarks = models.TextField()
	assessed_by = models.CharField(max_length=255,blank=True)
	status = models.CharField(max_length=255,choices=STATUS, default="notassessed")
	position = models.CharField(max_length=255,blank=True)
	mdate = models.DateField(null=True,blank=True)
	class Meta:
		db_table = "student"

class Lecturer(models.Model):		
	GENDER_CHOICE = (
		('male','male'),
		('female','female'),
		)
	PERFOMANCE_CHOICE = (
		('excellent','excellent'),
		('good','good'),
		('average','average'),
		('fair','fair'),
		('poor','poor'),
		)
	STATUS = (
		('assessed','assessed'),
		('notassessed','notassessed'),
		)
	s_fullname = models.CharField(max_length=255)
	registration_no = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=100)
	company_name = models.CharField(max_length=255)
	address = models.TextField()
	county = models.CharField(max_length=255)
	company_phone_no = models.CharField(max_length=50)
	supervisor_name = models.CharField(max_length=255)
	gender = models.CharField(max_length=255,choices=GENDER_CHOICE)
	period_from = models.DateField(null=True, blank=True)
	period_to = models.DateField(null=True,blank=True)
	punctual = models.CharField(max_length=255,choices=PERFOMANCE_CHOICE)
	regulations = models.CharField(max_length=255,choices=PERFOMANCE_CHOICE)
	workmanship = models.CharField(max_length=255,choices=PERFOMANCE_CHOICE)
	workout = models.CharField(max_length=255,choices=PERFOMANCE_CHOICE)
	adaptability = models.CharField(max_length=255,choices=PERFOMANCE_CHOICE)
	commu = models.CharField(max_length=255,choices=PERFOMANCE_CHOICE)
	reliability = models.CharField(max_length=255,choices=PERFOMANCE_CHOICE)
	team_work = models.CharField(max_length=255,choices=PERFOMANCE_CHOICE)
	overall_assessment = models.CharField(max_length=255,choices=PERFOMANCE_CHOICE)
	general_remarks = models.TextField()
	assessed_by = models.CharField(max_length=255)
	status = models.CharField(max_length=255,choices=STATUS, default="notassessed")
	position = models.CharField(max_length=255)
	mdate = models.DateField(null=True,blank=True)
	class Meta:
		db_table = "lecturer"





