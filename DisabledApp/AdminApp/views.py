from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from AdminApp.models import Tbl_district,Tbl_category,Tbl_location,Tbl_equipment,Tbl_scholarship
from GuestApp.models import Tbl_institution,Tbl_login,Tbl_disabledperson
from DisabledPersonApp.models import Tbl_request,Tbl_payment,Tbl_enquiry,Tbl_scholarshipreq
from InstitutionApp.models import Tbl_request2,Tbl_payment2
from django.db.models import Count
from email.message import EmailMessage
import smtplib
import xlwt
import json
from django.views.generic import View
from django.views.decorators.cache import cache_control




# Create your views here.
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminhome(request):
    # Pie Chart Data (Disabled Person Categories)
    pie_labels = []
    pie_data = []
    
    pie_queryset = Tbl_disabledperson.objects.values('categoryid__categoryname').annotate(total_students=Count('personid'))
    for entry in pie_queryset:
        pie_labels.append(entry['categoryid__categoryname'])
        pie_data.append(entry['total_students'])

    # Bar Chart Data (Enquiry-wise Institutions)
    bar_labels = []
    bar_data = []

    bar_queryset = Tbl_enquiry.objects.values('institutionid__institutionname').annotate(total_institution=Count('institutionid'))
    for entry in bar_queryset:
        bar_labels.append(entry['institutionid__institutionname'])
        bar_data.append(entry['total_institution'])

    return render(request, 'Admin/index.html', {
        'pie_labels': json.dumps(pie_labels),
        'pie_data': json.dumps(pie_data),
        'bar_labels': json.dumps(bar_labels),
        'bar_data': json.dumps(bar_data)
    })


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def district(request):
    logid = request.session.get('loginid')
    if logid:
        return render(request,'Admin/District.html')
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def district_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == 'POST':
            dname = request.POST.get("districtname") #textboxname
            dob = Tbl_district()
            dob.district_name = dname
            if Tbl_district.objects.filter(district_name=dname).exists():
                return HttpResponse("<script>alert('Already Exists..');window.location='/adminapp/viewdistrict';</script>")
            else:
                dob.save()
                return HttpResponse("<script>alert('Successfully Inserted..');window.location='/adminapp/viewdistrict';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def editdistrict(request,districtid):
    logid = request.session.get('loginid')
    if logid:
        if request.method=='POST':
            dname=request.POST.get("districtname")
            dis = Tbl_district.objects.get(district_id=districtid)
            dis.district_name = dname
            dis.save()
            return viewdistrict(request)
        dis = Tbl_district.objects.get(district_id=districtid)
        return render(request,"Admin/editdistrict.html",{'dis':dis})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def category(request):
    logid = request.session.get('loginid')
    if logid:
        return render(request,'Admin/Category.html')
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)       
def category_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            cname = request.POST.get("categoryname") #textboxname
            cimage = request.FILES["categoryimage"] #filename
            cdesc = request.POST.get("categorydesc")
            cob = Tbl_category()
            cob.categoryname = cname
            cob.categoryimage = cimage
            cob.categorydesc = cdesc

            if Tbl_category.objects.filter(categoryname=cname).exists():
                return HttpResponse("<script>alert('Already Exists..');window.location='/adminapp/viewcategory';</script>")
            else:
                cob.save()
                return HttpResponse("<script>alert('Successfully Inserted..');window.location='/adminapp/viewcategory';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def location(request):
    logid = request.session.get('loginid')
    if logid:
        districts=Tbl_district.objects.all() #select * from Tbl_district
        return render(request,'Admin/Location.html',{'district':districts})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def location_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            districtid=request.POST.get("district_id")
            lname = request.POST.get("locationname") #textboxname
            lob = Tbl_location()
            lob.locationname = lname
            lob.district_id = Tbl_district.objects.get(district_id=districtid)
            if Tbl_location.objects.filter(locationname=lname,district_id=districtid).exists():
                return HttpResponse("<script>alert('Already Exists..');window.location='/adminapp/viewlocation';</script>")
            else:
                lob.save()
                return HttpResponse("<script>alert('Successfully Inserted..');window.location='/adminapp/viewlocation';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcategory(request):
    logid = request.session.get('loginid')
    if logid:
        category = Tbl_category.objects.all() #select * from Tbl_category
        return render(request,'Admin/Viewcategory.html',{'category':category})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deletecategory(request, categoryid):
    logid = request.session.get('loginid')
    if logid:
        cob = Tbl_category.objects.get(categoryid=categoryid) #select * from Tbl_category
        cob.delete()
        return HttpResponse("<script>alert('Successfully Deleted..');window.location='/adminapp/viewcategory';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewlocation(request):
    logid = request.session.get('loginid')
    if logid:
        districts = Tbl_district.objects.all() #select * from Tbl_district
        return render(request,'Admin/Viewlocation.html',{'districts':districts})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def filllocation(request):
    did = int(request.POST.get("did"))
    location = Tbl_location.objects.filter(district_id=did).values()
    return JsonResponse(list(location), safe=False)
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deletelocation(request, locationid):
    logid = request.session.get('loginid')
    if logid:
        lob = Tbl_location.objects.get(locationid=locationid) #select * from Tbl_category
        lob.delete()
        return HttpResponse("<script>alert('Successfully Deleted..');window.location='/adminapp/viewlocation';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def equipment(request):
    logid = request.session.get('loginid')
    if logid:
        return render(request,'Admin/Equipment.html')  
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def equipment_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            ename = request.POST.get("equipmentname") #textboxname
            eimage = request.FILES["equipmentimage"] #filename
            edesc = request.POST.get("equipmentdesc")
            eamount = request.POST.get("amount")
            estock = request.POST.get("equipmentstock")
            eob = Tbl_equipment()
            eob.equipmentname = ename
            eob.equipmentimage = eimage
            eob.equipmentdesc = edesc
            eob.amount = eamount
            eob.equipmentstock = estock
            if Tbl_equipment.objects.filter(equipmentname=ename).exists():
                return HttpResponse("<script>alert('Already Exists..');window.location='/adminapp/viewequipment';</script>")
            else:
                eob.save()
                return HttpResponse("<script>alert('Successfully Inserted..');window.location='/adminapp/viewequipment';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewequipment(request):
    logid = request.session.get('loginid')
    if logid:
        equipment = Tbl_equipment.objects.all()
        return render(request,'Admin/Viewequipment.html',{'equipment':equipment})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deleteequipment(request, equipmentid):
    logid = request.session.get('loginid')
    if logid:
        eob = Tbl_equipment.objects.get(equipmentid=equipmentid) 
        eob.delete()
        return HttpResponse("<script>alert('Successfully Deleted..');window.location='/adminapp/viewequipment';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def scholarship(request):
    logid = request.session.get('loginid')
    if logid:
        category=Tbl_category.objects.all()
        return render(request,'Admin/Scholarship.html',{'category':category})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def scholarship_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            sname = request.POST.get("scholarshipname")
            categoryid = request.POST.get("categoryid")
            sdesc = request.POST.get("scholarshipdesc")
            scriteria = request.POST.get("criteria")
            sstartdate = request.POST.get("startdate")
            senddate = request.POST.get("enddate")
            slink = request.POST.get("link")
            sob = Tbl_scholarship()
            sob.scholarshipname = sname
            sob.categoryid = Tbl_category.objects.get(categoryid=categoryid)
            sob.scholarshipdesc = sdesc
            sob.criteria = scriteria
            sob.startdate = sstartdate
            sob.enddate = senddate
            sob.link = slink
            if Tbl_scholarship.objects.filter(scholarshipname=sname,categoryid=categoryid).exists():
                return HttpResponse("<script>alert('Already Exists..');window.location='/adminapp/viewscholarship';</script>")
            else:
                sob.save()
                return HttpResponse("<script>alert('Successfully Inserted..');window.location='/adminapp/viewscholarship';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewscholarship(request):
    logid = request.session.get('loginid')
    if logid:
        category = Tbl_category.objects.all() #select * from Tbl_district
        scholarship = Tbl_scholarship.objects.all()
        return render(request,'Admin/Viewscholarship.html',{'category':category})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deletescholarship(request, scholarshipid):
    logid = request.session.get('loginid')
    if logid:
        sob = Tbl_scholarship.objects.get(scholarshipid=scholarshipid)
        sob.delete()
        return HttpResponse("<script>alert('Successfully Deleted..');window.location='/adminapp/viewscholarship';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewdistrict(request):
    logid = request.session.get('loginid')
    if logid:
        district = Tbl_district.objects.all()
        return render(request,'Admin/Viewdistrict.html',{'district':district})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deletedistrict(request, districtid):
    logid = request.session.get('loginid')
    if logid:
        dob = Tbl_district.objects.get(district_id=districtid) #select * from Tbl_category
        dob.delete()
        return HttpResponse("<script>alert('Successfully Deleted..');window.location='/adminapp/viewdistrict';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def institutionsview(request):
    logid = request.session.get('loginid')
    if logid:
        institution = Tbl_institution.objects.filter(loginid__status="Not Confirmed")
        return render(request,'Admin/institutionsview.html',{'institution':institution})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def institutionaccept(request,loginid):
    logid = request.session.get('loginid')
    if logid:
        lob = Tbl_login.objects.get(loginid=loginid)
        institution = Tbl_institution.objects.get(loginid=lob)
        mailid = institution.email
        lob.status="Accepted"
        lob.save()

        msg = EmailMessage()
        msg.set_content('Your Registration Request is Confirmed')
        msg['Subject'] = "Registration Request Accepted"
        msg['from'] = 'jensonjames543212345@gmail.com'
        msg['To'] = {mailid}
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login('jensonjames543212345@gmail.com','zpgg wrco qewg dfqc')
            smtp.send_message(msg)
        return HttpResponse("<script>alert('Accepted..');window.location='/adminapp/institutionsview';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def institutionreject(request,loginid):
    logid = request.session.get('loginid')
    if logid:
        lob = Tbl_login.objects.get(loginid=loginid)
        institution = Tbl_institution.objects.get(loginid=lob)
        mailid = institution.email
        lob.status="Rejected"
        lob.save()
        msg = EmailMessage()
        msg.set_content('Your Registration Request is Rejected')
        msg['Subject'] = "Registration Request Accepted"
        msg['from'] = 'jensonjames543212345@gmail.com'
        msg['To'] = {mailid}
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login('jensonjames543212345@gmail.com','zpgg wrco qewg dfqc')
            smtp.send_message(msg)
        return HttpResponse("<script>alert('Rejected..');window.location='/adminapp/institutionsview';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def fillscholarship(request):
    logid = request.session.get('loginid')
    if logid:
        cid = int(request.POST.get("cid"))
        scholarship = Tbl_scholarship.objects.filter(categoryid=cid).values()
        return JsonResponse(list(scholarship), safe=False)
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def requestview(request):
    logid = request.session.get('loginid')
    if logid:
        requests = Tbl_request.objects.filter(status="Not Confirmed")
        return render(request,'Admin/requestview.html',{'requests':requests})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")

from django.shortcuts import get_object_or_404   
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def requestaccept(request, id):
    logid = request.session.get('loginid')
    if logid:
        # Get the request object
        rob = get_object_or_404(Tbl_request, requestid=id)
        disabled_person = get_object_or_404(Tbl_disabledperson, personid=rob.personid_id)
        equipment = get_object_or_404(Tbl_equipment, equipmentid=rob.equipmentid_id)

        # Check if there is enough stock before accepting
        if rob.count > equipment.equipmentstock:
            return HttpResponse("<script>alert('Not enough stock available to accept this request.');window.location='/adminapp/requestview';</script>")

        # Reduce stock
        equipment.equipmentstock -= rob.count
        equipment.save()

        # Update request status
        rob.status = "Accepted"
        rob.save()

        # Send email
        msg = EmailMessage()
        msg.set_content(
            f'<h4>Hai {disabled_person.personname},</h4>'
            'Your order has been successfully accepted. You can pay the amount and receive the product.<br><br>',
            subtype='html'
        )
        msg['Subject'] = "Booking Accepted"
        msg['From'] = 'jensonjames543212345@gmail.com'
        msg['To'] = disabled_person.email

        # Send email via SMTP
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('jensonjames543212345@gmail.com', 'zpgg wrco qewg dfqc')
            smtp.send_message(msg)

        return HttpResponse("<script>alert('Request Accepted and Stock Updated.');window.location='/adminapp/requestview';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required. Please Login First.');window.location='/Login';</script>")
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def requestreject(request,id):
    logid = request.session.get('loginid')
    if logid:
        rob = Tbl_request.objects.get(requestid=id)
        mailid = Tbl_disabledperson.objects.get(personid=rob.personid_id).email
        personname=Tbl_disabledperson.objects.get(personid=rob.personid_id).personname
        rob.status="Rejected"
        rob.save()
        msg = EmailMessage()
        msg.set_content(f'<h4>Haii {personname},</h4>Sorry,Your order has been rejected.<br><br>',subtype='html')
        msg['Subject'] = "Booking Rejected"
        msg['from'] = 'jensonjames543212345@gmail.com'
        msg['To'] = {mailid}
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login('jensonjames543212345@gmail.com','zpgg wrco qewg dfqc')
            smtp.send_message(msg)
        return HttpResponse("<script>alert('Rejected..');window.location='/adminapp/requestview';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def requestviews(request):
    logid = request.session.get('loginid')
    if logid:
        requests = Tbl_request2.objects.filter(status="Not Confirmed")
        return render(request,'Admin/requestviews.html',{'requests':requests})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def requestsaccept(request, id):
    logid = request.session.get('loginid')
    if logid:
        # Get the request object
        rob = get_object_or_404(Tbl_request2, requestid=id)
        institution = get_object_or_404(Tbl_institution, institutionid=rob.institutionid_id)
        equipment = get_object_or_404(Tbl_equipment, equipmentid=rob.equipmentid_id)

        # Check if there is enough stock before accepting the request
        if rob.count > equipment.equipmentstock:
            return HttpResponse("<script>alert('Not enough stock available to accept this request.');window.location='/adminapp/requestviews';</script>")

        # Reduce stock
        equipment.equipmentstock -= rob.count
        equipment.save()

        # Update request status
        rob.status = "Accepted"
        rob.save()

        # Send email notification
        msg = EmailMessage()
        msg.set_content(
            f'<h4>Hai {institution.institutionname},</h4>'
            'Your order has been successfully accepted. You can pay the amount and receive the product.<br><br>',
            subtype='html'
        )
        msg['Subject'] = "Booking Accepted"
        msg['From'] = 'jensonjames543212345@gmail.com'
        msg['To'] = institution.email  # Fixed email assignment

        # Send email via SMTP
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('jensonjames543212345@gmail.com', 'zpgg wrco qewg dfqc')
            smtp.send_message(msg)

        return HttpResponse("<script>alert('Request Accepted and Stock Updated.');window.location='/adminapp/requestviews';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required. Please Login First.');window.location='/Login';</script>")
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def requestsreject(request,id):
    logid = request.session.get('loginid')
    if logid:
        rob = Tbl_request2.objects.get(requestid=id)
        mailid = Tbl_institution.objects.get(institutionid=rob.institutionid_id).email
        institutionname=Tbl_institution.objects.get(institutionid=rob.institutionid_id).institutionname
        rob.status="Rejected"
        rob.save()
        msg = EmailMessage()
        msg.set_content(f'<h4>Haii {institutionname},</h4>Sorry,Your order has been rejected.<br><br>',subtype='html')
        msg['Subject'] = "Booking Accepted"
        msg['from'] = 'jensonjames543212345@gmail.com'
        msg['To'] = {mailid}
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login('jensonjames543212345@gmail.com','zpgg wrco qewg dfqc')
            smtp.send_message(msg)
        return HttpResponse("<script>alert('Rejected..');window.location='/adminapp/requestviews';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def editlocation(request,locationid):
    logid = request.session.get('loginid')
    if logid:
        if request.method=='POST':
            lname=request.POST.get("locationname")
            loc = Tbl_location.objects.get(locationid=locationid)
            loc.locationname = lname
            loc.save()
            return viewlocation(request)
        loc = Tbl_location.objects.get(locationid=locationid)
        return render(request,"Admin/editlocation.html",{'loc':loc})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def editcategory(request,id):
    logid = request.session.get('loginid')
    if logid:
        if request.method=='POST':
            cname=request.POST.get("categoryname")
            cdescription=request.POST.get("categorydesc")
            categoryimage=request.POST.get("oldimage")
            cat = Tbl_category.objects.get(categoryid=id)
            cat.categoryname = cname
            cat.categorydesc = cdescription
            cat.categoryimage = categoryimage
            if 'categoryimage' in request.FILES:
                cat.categoryimage = request.FILES["categoryimage"]
            else:
                cat.categoryimage = request.POST.get("oldimage")

            cat.save()
            return viewcategory(request)
        cat = Tbl_category.objects.get(categoryid=id)
        return render(request,"Admin/editcategory.html",{'cat':cat})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def editequipment(request,id):
    logid = request.session.get('loginid')
    if logid:
        if request.method=='POST':
            ename=request.POST.get("equipmentname")
            edescription=request.POST.get("equipmentdesc")
            estoct=request.POST.get("equipmentstock")
            eamount=request.POST.get("amount")
            equipmentimage=request.POST.get("oldimage")
            equ = Tbl_equipment.objects.get(equipmentid=id)
            equ.equipmentname = ename
            equ.equipmentdesc = edescription
            equ.equipmentstock = estoct
            equ.amount = eamount
            equ.equipmentimage = equipmentimage
            if 'equipmentimage' in request.FILES:
                equ.equipmentimage = request.FILES["equipmentimage"]
            else:
                equ.equipmentimage = request.POST.get("oldimage")

            equ.save()
            return viewequipment(request)
        equ = Tbl_equipment.objects.get(equipmentid=id)
        return render(request,"Admin/editequipment.html",{'equ':equ})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def editscholarship(request,scholarshipid):
    logid = request.session.get('loginid')
    if logid:
        if request.method=='POST':
            sname=request.POST.get("scholarshipname")
            sdesc=request.POST.get("scholarshipdesc")
            scriteria=request.POST.get("criteria")
            senddate=request.POST.get("enddate")
            slink=request.POST.get("link")

            sch = Tbl_scholarship.objects.get(scholarshipid=scholarshipid)
            sch.scholarshipname = sname
            sch.scholarshipdesc = sdesc
            sch.criteria = scriteria
            sch.enddate = senddate
            sch.link = slink

            sch.save()
            return viewscholarship(request)
        sch = Tbl_scholarship.objects.get(scholarshipid=scholarshipid)
        return render(request,"Admin/editscholarship.html",{'sch':sch})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")




def piechartreport(request):
   
        labels = []
        data = []

        queryset = Tbl_disabledperson.objects.values('categoryid__categoryname').annotate(total_students=Count('personid'))

        for p in queryset:
            labels.append(p['categoryid__categoryname'])  
            data.append(p['total_students'])  

        return render(request, 'Admin/piechartreport.html', {
            'labels': json.dumps(labels),  # Convert to JSON
            'data': json.dumps(data)  # Convert to JSON
        })


class ExportExcelStudent(View):
    def get(self, request):
        
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="studentlist.xls"'

            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Sheet1')

            # Define the column headings
            row_num = 0
            columns = ['Equipment Name', 'Payment date', 'Amount', 'Student name', 'Contact Number']
            for col_num, column_title in enumerate(columns):
                ws.write(row_num, col_num, column_title)

            # Query the data from your model, and write it to the worksheet
                queryset = Tbl_payment.objects.select_related().values_list(
                'requestid__equipmentid__equipmentname',
                'paymentdate',
                'amount',
                'requestid__personid__personname',
                'requestid__personid__contactno')
            for row in queryset:
                row_num += 1
                for col_num, cell_value in enumerate(row):
                    ws.write(row_num, col_num, cell_value)
                    
            wb.save(response)
            return response
        
class ExportExcelInstitution(View):
    def get(self, request):
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="Institutionlist.xls"'

            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Sheet1')

            # Define the column headings
            row_num = 0
            columns = ['Equipment Name', 'Payment date', 'Amount', 'Institution name', 'Contact Number']
            for col_num, column_title in enumerate(columns):
                ws.write(row_num, col_num, column_title)

            # Query the data from your model, and write it to the worksheet
                queryset = Tbl_payment2.objects.select_related().values_list(
                'requestid__equipmentid__equipmentname',
                'paymentdate',
                'amount',
                'requestid__institutionid__institutionname',
                'requestid__institutionid__contactno')
            for row in queryset:
                row_num += 1
                for col_num, cell_value in enumerate(row):
                    ws.write(row_num, col_num, cell_value)
                    
            wb.save(response)
            return response
        
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def Logout(request):
     logid = request.session.get('loginid')
     if logid:
        request.session.clear()
        return redirect('/')
     else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewstudentpayment(request):
    logid = request.session.get('loginid')
    if logid:
        payment = Tbl_payment.objects.all()
        return render(request,'Admin/viewstudentpayment.html',{'payment':payment})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewinstitutionpayment(request):
    logid = request.session.get('loginid')
    if logid:
        payment2 = Tbl_payment2.objects.all()
        return render(request,'Admin/viewinstitutionpayment.html',{'payment2':payment2})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")

def barchartenquirybasedinstitutions(request):
    labels = []
    data = []

    queryset = Tbl_enquiry.objects.values('institutionid__institutionname').annotate(total_institution=Count('institutionid'))
    for p in queryset:
        labels.append(p['institutionid__institutionname'])  # Brand Name
        data.append(p['total_institution'])  # Total Products

    return render(request, 'Admin/barchartenquirybasedinstitutions.html', {
        'labels': labels,
        'data': data
 })
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def scholarshipreqview(request):
    logid = request.session.get('loginid')
    if logid:
        scholarshipreq = Tbl_scholarshipreq.objects.filter(status="Not Confirmed")
        return render(request,'Admin/scholarshipreqview.html',{'scholarshipreq':scholarshipreq})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def requestaccepts(request,id):
    logid = request.session.get('loginid')
    if logid:
        rob = Tbl_scholarshipreq.objects.get(requestid=id)
        mailid = Tbl_disabledperson.objects.get(personid=rob.personid_id).email
        personname=Tbl_disabledperson.objects.get(personid=rob.personid_id).personname
        rob.status="Accepted"
        rob.save()
        msg = EmailMessage()
        msg.set_content(f'<h4>Haii {personname},</h4>Your order has been successfully accepted.You can pay the amount and receive the product.<br><br>',subtype='html')
        msg['Subject'] = "Booking Accepted"
        msg['from'] = 'jensonjames543212345@gmail.com'
        msg['To'] = {mailid}
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login('jensonjames543212345@gmail.com','zpgg wrco qewg dfqc')
            smtp.send_message(msg)
        return HttpResponse("<script>alert('Accepted..');window.location='/adminapp/scholarshipreqview';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def requestrejects(request,id):
    logid = request.session.get('loginid')
    if logid:
        rob = Tbl_scholarshipreq.objects.get(requestid=id)
        mailid = Tbl_disabledperson.objects.get(personid=rob.personid_id).email
        personname=Tbl_disabledperson.objects.get(personid=rob.personid_id).personname
        rob.status="Rejected"
        rob.save()
        msg = EmailMessage()
        msg.set_content(f'<h4>Haii {personname},</h4>Sorry,Your order has been rejected.<br><br>',subtype='html')
        msg['Subject'] = "Booking Rejected"
        msg['from'] = 'jensonjames543212345@gmail.com'
        msg['To'] = {mailid}
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login('jensonjames543212345@gmail.com','zpgg wrco qewg dfqc')
            smtp.send_message(msg)
        return HttpResponse("<script>alert('Rejected..');window.location='/adminapp/scholarshipreqview';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
    

        
 
