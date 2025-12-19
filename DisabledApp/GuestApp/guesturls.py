from django.urls import path
from GuestApp import views

urlpatterns = [
    path('Login/',views.Login,name='Login'),
    path('login_process/',views.login_process,name='login_process'),
    path('',views.Index,name='Indexx'),
    path('institutionreg/',views.institutionreg,name='institutionreg'),
    path('institutionreg_process/',views.institutionreg_process,name='institutionreg_process'),
    path('disabledpersonreg/',views.disabledpersonreg,name='disabledpersonreg'),
    path('disabledpersonreg_process/',views.disabledpersonreg_process,name='disabledpersonreg_process'),
    path('viewmoreinstitutions/<id>',views.viewmoreinstitutions,name='viewmoreinstitutions'),
    path('fillinstitutions/',views.fillinstitutions,name='fillinstitutions'),
    path('institutionview/',views.institutionview,name='institutionview'),
    path('equipmentsview/',views.equipmentsview,name='equipmentsview'),






]