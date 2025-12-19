from django.urls import path
from AdminApp import views
from .views import ExportExcelStudent,ExportExcelInstitution

urlpatterns = [
    path('adminhome/',views.adminhome,name='adminhome'),
    path('district/',views.district,name='district'),
    path('district_process/',views.district_process,name='district_process'),
    path('category/',views.category,name='category'),
    path('category_process/',views.category_process,name='category_process'),
    path('location/',views.location,name='location'),
    path('location_process/',views.location_process,name='location_process'),
    path('viewcategory/',views.viewcategory,name='viewcategory'),
    path('deletecategory/<categoryid>',views.deletecategory,name='deletecategory'),
    path('viewlocation',views.viewlocation,name='viewlocation'),
    path('filllocation',views.filllocation,name='filllocation'),
    path('deletelocation/<locationid>',views.deletelocation,name='deletelocation'),
    path('equipment/',views.equipment,name='equipment'),
    path('equipment_process/',views.equipment_process,name='equipment_process'),
    path('viewequipment/',views.viewequipment,name='viewequipment'),
    path('deleteequipment/<equipmentid>',views.deleteequipment,name='deleteequipment'),
    path('scholarship/',views.scholarship,name='scholarship'),
    path('scholarship_process/',views.scholarship_process,name='scholarship_process'),
    path('viewscholarship',views.viewscholarship,name='viewscholarship'),
    path('deletescholarship/<scholarshipid>',views.deletescholarship,name='deletescholarship'),
    path('viewdistrict',views.viewdistrict,name='viewdistrict'),
    path('deletedistrict/<districtid>',views.deletedistrict,name='deletedistrict'),
    path('editdistrict/<districtid>',views.editdistrict,name='editdistrict'),
    path('institutionsview/',views.institutionsview,name='institutionsview'),
    path('institutionaccept/<loginid>',views.institutionaccept,name='institutionaccept'),
    path('institutionreject/<loginid>',views.institutionreject,name='institutionreject'),
    path('fillscholarship',views.fillscholarship,name='fillscholarship'),
    path('requestview/',views.requestview,name='requestview'),
    path('requestaccept/<id>',views.requestaccept,name='requestaccept'),
    path('requestreject/<id>',views.requestreject,name='requestreject'),
    path('requestviews/',views.requestviews,name='requestviews'),
    path('requestsaccept/<id>',views.requestsaccept,name='requestsaccept'),
    path('requestsreject/<id>',views.requestsreject,name='requestsreject'),
    path('editlocation/<locationid>',views.editlocation,name='editlocation'),
    path('editcategory/<id>',views.editcategory,name='editcategory'),
    path('editequipment/<id>',views.editequipment,name='editequipment'),
    path('editscholarship/<scholarshipid>',views.editscholarship,name='editscholarship'),
    path('piechartreport',views.piechartreport,name='piechartreport'),
    path('export_excel/', ExportExcelStudent.as_view(), name='export_excel'),
    path('exportexcel/', ExportExcelInstitution.as_view(), name='exportexcel'),
    path('Logout/',views.Logout,name='Logout'),
    path('viewstudentpayment/',views.viewstudentpayment,name='viewstudentpayment'),
    path('viewinstitutionpayment/',views.viewinstitutionpayment,name='viewinstitutionpayment'),
    path('barchartenquirybasedinstitutions',views.barchartenquirybasedinstitutions,name='barchartenquirybasedinstitutions'),
    path('scholarshipreqview/',views.scholarshipreqview,name='scholarshipreqview'),
    path('requestaccepts/<id>',views.requestaccepts,name='requestaccepts'),
    path('requestrejects/<id>',views.requestrejects,name='requestrejects'),













    
















    

]