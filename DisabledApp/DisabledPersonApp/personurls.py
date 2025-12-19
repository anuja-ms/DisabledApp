from django.urls import path
from DisabledPersonApp import views

urlpatterns = [
    path('Index/',views.Index,name='Index'),
    path('viewinstitution/<id>',views.viewinstitution,name='viewinstitution'),
    path('enquiry/<id>',views.enquiry,name='enquiry'),
    path('viewmoreinstitution/<id>',views.viewmoreinstitution,name='viewmoreinstitution'),
    path('fillinstitutions/',views.fillinstitutions,name='fillinstitutions'),
    path('institutionviews/',views.institutionviews,name='institutionviews'),
    path('enquiry_process/',views.enquiry_process,name='enquiry_process'),
    path('scheduledetails/',views.scheduledetails,name='scheduledetails'),
    path('morescheduledetails/<id>', views.morescheduledetails, name='morescheduledetails'),
    path('equipmentviews/',views.equipmentviews,name='equipmentviews'),
    path('scholarshipviews/',views.scholarshipviews,name='scholarshipviews'),
    path('fillscholarship',views.fillscholarship,name='fillscholarship'),
    path('request/<id>',views.request,name='request'),
    path('request_process/',views.request_process,name='request_process'),
    path('requestdetailsview/',views.requestdetailsview,name='requestdetailsview'),
    path('payment/<id>',views.payment,name='payment'),
    path('payment_process/',views.payment_process,name='payment_process'),
    path('jobviews/',views.jobviews,name='jobviews'),
    path('profileview/',views.profileview,name='profileview'),
    path('profileedit/<id>',views.profileedit,name='profileedit'),
    path('Logout/',views.Logout,name='Logout'),
    path('scholarshipreq/<id>',views.scholarshipreq,name='scholarshipreq'),
    path('scholarshipreq_process/',views.scholarshipreq_process,name='scholarshipreq_process'),
    path('scholar/',views.scholarshipreqdetails,name='scholarshipreqdetails'),







]