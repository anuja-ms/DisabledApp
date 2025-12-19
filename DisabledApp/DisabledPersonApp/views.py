from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from DisabledPersonApp.models import Tbl_enquiry,Tbl_request,Tbl_payment,Tbl_scholarshipreq
from AdminApp.models import Tbl_category,Tbl_district,Tbl_equipment,Tbl_scholarship
from GuestApp.models import Tbl_institution,Tbl_disabledperson
from InstitutionApp.models import Tbl_schedule,Tbl_jobposting
from django.views.decorators.cache import cache_control



# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def Index(request):
    logid = request.session.get('loginid')
    if logid:
        category =Tbl_category.objects.all()
        return render(request,'DisabledPerson/Index.html',{'category':category})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewinstitution(request,id):
    logid = request.session.get('loginid')
    if logid:
        request.session['categoryid'] = id
        cat = Tbl_institution.objects.filter(categoryid=id)
        return render(request, "DisabledPerson/viewinstitution.html",{'cat':cat})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def enquiry(request,id):
    logid = request.session.get('loginid')
    if logid:
        disabledperson = Tbl_disabledperson.objects.get(loginid=request.session['loginid'])
        institution = Tbl_institution.objects.get(institutionid=id)
        return render(request, "DisabledPerson/enquiry.html",{'disabledperson':disabledperson,'institution':institution})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewmoreinstitution(request,id):
    logid = request.session.get('loginid')
    if logid:
        request.session['institutionid'] = id
        institution = Tbl_institution.objects.filter(institutionid=id)
        return render(request, "DisabledPerson/viewmoreinstitution.html",{'institution':institution})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")

def fillinstitutions(request):
    sid = int(request.POST.get("sid"))
    categoryid = int(request.POST.get("categoryid"))
    institutions = Tbl_institution.objects.filter(locationid=sid, categoryid=categoryid).values()
    return JsonResponse(list(institutions),safe=False)
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def institutionviews(request):
    logid = request.session.get('loginid')
    if logid:
        category =Tbl_category.objects.all()
        districts = Tbl_district.objects.all()
        institution = Tbl_institution.objects.all() #select * from Tbl_category
        return render(request,'DisabledPerson/institutionviews.html',{'institution':institution,'category':category,'districts':districts})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def enquiry_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            institutionid=request.POST.get("institution")
            personid=request.POST.get("disabledperson")
            enquiry = request.POST.get("enquiry") #textboxname
            eob = Tbl_enquiry()
            eob.status = "Not Confirmed"
            eob.enquiry = enquiry
            eob.institutionid = Tbl_institution.objects.get(institutionid=institutionid)
            eob.personid = Tbl_disabledperson.objects.get(personid=personid)

            if Tbl_enquiry.objects.filter(enquiry=enquiry,institutionid=institutionid,personid=personid).exists():
                return HttpResponse("<script>alert('Already Exists..');window.location='/DisabledPerson/Index';</script>")
            else:
                eob.save()
                return HttpResponse("<script>alert('Successfully Inserted..');window.location='/disabledpersonapp/Index';</script>")
        else:
            return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def scheduledetails(request):
    logid = request.session.get('loginid')
    if logid:
        disabledperson = Tbl_disabledperson.objects.get(loginid=request.session['loginid'])
        schedule = Tbl_schedule.objects.filter(enquiryid__personid=disabledperson)
        return render(request,'DisabledPerson/scheduledetails.html',{'schedule':schedule})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def morescheduledetails(request,id):
    logid = request.session.get('loginid')
    if logid:
        schedule = Tbl_schedule.objects.get(scheduleid=id)
        return render(request,'DisabledPerson/morescheduledetails.html',{'schedule':schedule})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def equipmentviews(request):
    logid = request.session.get('loginid')
    if logid:
        equipment =Tbl_equipment.objects.all()
        return render(request,'DisabledPerson/equipmentviews.html',{'equipment':equipment})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def scholarshipviews(request):
    logid = request.session.get('loginid')
    if logid:
        category = Tbl_category.objects.all() #select * from Tbl_district
        scholarship = Tbl_scholarship.objects.all()
        return render(request,'DisabledPerson/scholarshipviews.html',{'category':category})
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
def request(request,id):
    logid = request.session.get('loginid')
    if logid:
        disabledperson = Tbl_disabledperson.objects.get(loginid=request.session['loginid'])
        equipment = Tbl_equipment.objects.get(equipmentid=id)
        return render(request, "DisabledPerson/request.html",{'disabledperson':disabledperson,'equipment':equipment})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
from django.shortcuts import get_object_or_404

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def request_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            equipmentid = request.POST.get("equipment")
            personid = request.POST.get("disabledperson")
            requesteddate = request.POST.get("requesteddate")
            count = int(request.POST.get("count"))
            totalamount = request.POST.get("totalamount")

            # Get the equipment instance
            equipment = get_object_or_404(Tbl_equipment, equipmentid=equipmentid)

            # Check if requested count is available in stock
            if count > equipment.equipmentstock:
                return HttpResponse("<script>alert('Not enough stock available. Please reduce the quantity.');window.location='/disabledpersonapp/Index';</script>")

            # Check if a similar request already exists
            if Tbl_request.objects.filter(requesteddate=requesteddate, equipmentid=equipmentid, personid=personid).exists():
                return HttpResponse("<script>alert('Request already exists.');window.location='/disabledpersonapp/Index';</script>")

            # Create request entry
            rob = Tbl_request()
            rob.status = "Not Confirmed"
            rob.requesteddate = requesteddate
            rob.count = count
            rob.totalamount = totalamount
            rob.equipmentid = equipment
            rob.personid = Tbl_disabledperson.objects.get(personid=personid)
            rob.save()

            # Reduce stock
            equipment.save()

            return HttpResponse("<script>alert('Request successfully placed.');window.location='/disabledpersonapp/Index';</script>")
    else:
        return HttpResponse("<script>alert('Authentication required. Please login first.');window.location='/Login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def requestdetailsview(request):
    logid = request.session.get('loginid')
    if logid:
        id = Tbl_disabledperson.objects.get(loginid=request.session['loginid'])
        requests = Tbl_request.objects.filter(personid=id).exclude(status__in=["Paid"])
        return render(request,'DisabledPerson/requestdetailsview.html',{'requests':requests})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def payment(request,id):
    logid = request.session.get('loginid')
    if logid:
        payment = Tbl_request.objects.get(requestid=id)
        return render(request, "DisabledPerson/payment.html",{'payment':payment})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def payment_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            requestid=request.POST.get("requestid")
            amount = request.POST.get("amount") #textboxname
            pob = Tbl_payment()
            pob.status = "Paid"
            pob.amount = amount
            pob.requestid = Tbl_request.objects.get(requestid=requestid)
            if Tbl_payment.objects.filter(amount=amount,requestid=requestid).exists():
                return HttpResponse("<script>alert('Already Exists..');window.location='/disabledpersonapp/Index';</script>")
            else:
                pob.save()
                request = Tbl_request.objects.get(requestid=requestid)
                request.status = "paid"
                request.save()
                return HttpResponse("<script>alert('Successfully Inserted..');window.location='/guestapp/Index';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def jobviews(request):
    logid = request.session.get('loginid')
    if logid:
        job =Tbl_jobposting.objects.all()
        return render(request,'DisabledPerson/jobviews.html',{'job':job})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def profileview(request):
    logid = request.session.get('loginid')
    if logid:
        person1 = request.session['loginid']
        person = Tbl_disabledperson.objects.get(loginid=person1)
        return render(request, "DisabledPerson/profileview.html",{'d':person})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def profileedit(request,id):
    logid = request.session.get('loginid')
    if logid:
        categories = Tbl_category.objects.all()
        if request.method=='POST':
            personname=request.POST.get("personname")
            address=request.POST.get("address")
            contactno=request.POST.get("contactno")
            email=request.POST.get("email")
            percentage=request.POST.get("percentage")
            disabilitydetails=request.POST.get("disabilitydetails")
            pname=request.POST.get("pname")
            pcontact=request.POST.get("pcontact")
            dob1=request.POST.get("dob")

            categoryid=request.POST.get("categoryid")

            idproof=request.POST.get("oldimage")
            dob = Tbl_disabledperson.objects.get(personid=id)
            dob.personname = personname
            dob.address = address
            dob.contactno = contactno
            dob.email = email
            dob.percentage = percentage
            dob.disabilitydetails = disabilitydetails
            dob.pname = pname
            dob.pcontact = pcontact
            dob.dob = dob1

            dob.categoryid = Tbl_category.objects.get(categoryid=categoryid)


            dob.idproof = idproof
            if 'idproof' in request.FILES:
                dob.idproof = request.FILES["idproof"]
            else:
                dob.idproof = request.POST.get("oldimage")

            dob.save()
            return profileview(request)
        dob = Tbl_disabledperson.objects.get(personid=id)
        return render(request,"DisabledPerson/profileedit.html",{'dob':dob,'category':categories})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def Logout(request):
    logid = request.session.get('loginid')
    if logid:
        request.session.clear()
        return redirect('/')
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def scholarshipreq(request,id):
    logid = request.session.get('loginid')
    if logid:
        disabledperson = Tbl_disabledperson.objects.get(loginid=request.session['loginid'])
        scholarship = Tbl_scholarship.objects.get(scholarshipid=id)
        institution = Tbl_institution.objects.all()

        return render(request, "DisabledPerson/scholarshipreq.html",{'disabledperson':disabledperson,'scholarship':scholarship,'institution':institution})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
def scholarshipreq_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            scholarshipid=request.POST.get("scholarship")
            personid=request.POST.get("disabledperson")
            institutionid=request.POST.get("institution")
            income = request.POST.get("income") #textboxname
            accountno = request.POST.get("accountno")
            course = request.POST.get("course")
            rob = Tbl_scholarshipreq()
            rob.status = "Not Confirmed"
            rob.income = income
            rob.accountno = accountno
            rob.course = course

            rob.scholarshipid = Tbl_scholarship.objects.get(scholarshipid=scholarshipid)
            rob.personid = Tbl_disabledperson.objects.get(personid=personid)
            rob.institutionid = Tbl_institution.objects.get(institutionid=institutionid)

            if Tbl_scholarshipreq.objects.filter(income=income,accountno=accountno,course=course,scholarshipid=scholarshipid,personid=personid,institutionid=institutionid).exists():
                return HttpResponse("<script>alert('Already Exists..');window.location='/DisabledPerson/Index';</script>")
            else:
                rob.save()
                return HttpResponse("<script>alert('Successfully Inserted..');window.location='/disabledpersonapp/Index';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def scholarshipreqdetails(request):
    logid = request.session.get('loginid')
    if logid:
        disabledperson = Tbl_disabledperson.objects.get(loginid=request.session['loginid'])

         #select * from Tbl_district
        scholarship = Tbl_scholarshipreq.objects.filter(personid=disabledperson)
        return render(request,'DisabledPerson/scholarshipreqdetailsview.html',{'scholarship':scholarship})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
    

