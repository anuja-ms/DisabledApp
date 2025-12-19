from django.urls import path
from InstitutionApp import views

urlpatterns = [
    path('Index/',views.Index,name='Index'),
    path('enquiryview/',views.enquiryview,name='enquiryview'),
    path('enquiryreject/<id>',views.enquiryreject,name='enquiryreject'),
    path('schedule/<id>', views.schedule, name='schedule'),
    path('scheduleprocess/<id>', views.scheduleprocess, name='scheduleprocess'),
    path('schedule_process/<id>', views.schedule_process, name='schedule_process'),
    path('equipmentview/',views.equipmentview,name='equipmentview'),
    path('requests/<id>',views.requests,name='requests'),
    path('requests_process/',views.requests_process,name='requests_process'),
    path('requestdetailsviews/',views.requestdetailsviews,name='requestdetailsviews'),
    path('payments/<id>',views.payments,name='payments'),
    path('payments_process/',views.payments_process,name='payments_process'),
    path('jobposting/',views.jobposting,name='jobposting'),
    path('jobreg_process/',views.jobreg_process,name='jobreg_process'),
    path('viewjob/',views.viewjob,name='viewjob'),
    path('deletejob/<jobid>',views.deletejob,name='deletejob'),
    path('editjob/<id>',views.editjob,name='editjob'),
    path('viewprofile/',views.viewprofile,name='viewprofile'),
    path('editprofile/<id>',views.editprofile,name='editprofile'),
    path('Logout/',views.Logout,name='Logout'),







]