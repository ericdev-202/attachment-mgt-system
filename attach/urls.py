from django.urls import path
from django.conf.urls import url, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #login and register urls
    path('',views.lindex,name='index'),
    path('login/',views.login_view, name='login_view'),
    path('register/',views.register, name='register'),
    path('logout/', views.logout_user, name="logout"),
    # path('adminpage/', views.hod, name='adminpage'),
    
    #lecturer urls
    path('lecturer_page/',views.lecturer,name='lecturer'),
    path('viewstudent/',views.viewallstudent,name='allstudent'),
    # path('viewAssessment/',views.viewallassess,name='viewallAssessment'),
    # path('viewsupervisorassess/',views.supervisorassessment,name='viewall'),
    path('lectass/',views.lecturerassement,name='viewall'),
    path('viewcompanydetails/',views.viewCompanydetails,name='allcompanydetails'),
    path('editview/<int:id>', views.getAssess),
    path('logbookdetails/',views.logbookdetails,name='logbookdetails'),
    path('viewlog/<int:id>',views.logbookview),
    path('reportview/',views.reportview,name='reportviews'),
    path('assessed/',views.showassessed,name='assessed'),
    path('lecassess/<int:id>', views.LecAssess),  
    path('lecupdate/<int:id>', views.LecUpdate), 
    path('assessview/<int:id>',views.viewassess),





    #students url
    # path('add',views.add),
    path('companydetails/',views.compdet,name='companydetails'),
    path('student/',views.student,name='student'),
    path('student_det/',views.addStudent,name='new_student'),
    path('elogbook/',views.elogbook,name='logbook'),
    path('new_entry',views.elogbook_entry,name='elogbook'),
    path('view/',views.ViewStudent,name='viewstudent'),
    path('up/',views.model_form_upload,name='report'),
    path('view_report/',views.report,name='view_report'), 
    path('company/',views.addCompany,name='companyde'),
    path('viewCompany/',views.viewCompany,name='ViewCompany'), 
    path('editcompany/<int:id>',views.editcompany),
    path('updatecompany/<int:id>',views.updatecompany),



    #suprvisor urls
    # path('',views.student),
    path('viewlogbook/',views.Logbook,name="viewlogbooks"),
    path('log/<int:id>',views.ViewLogbook),
    path('assessment/',views.viewassessment,name='assess'),
    path('assess/<int:id>',views.view,name="viewassess"),
    path('supervisor_page/',views.supervisor,name='supervisors'),
    path('studentdetails', views.index,name='details'),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    # path('delete/<int:id>', views.destroy),  


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)