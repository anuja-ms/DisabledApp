from django.shortcuts import render,redirect
from django.http import HttpResponse
from GuestApp.models import Tbl_login,Tbl_institution
from django.shortcuts import get_object_or_404
from DisabledPersonApp.models import Tbl_enquiry
from InstitutionApp.models import Tbl_schedule,Tbl_request2,Tbl_payment2,Tbl_jobposting
from AdminApp.models import Tbl_equipment,Tbl_category
from django.views.decorators.cache import cache_control





# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def Index(request):
    logid = request.session.get('loginid')
    if logid:
        return render(request,'Institution/Index.html')
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def enquiryview(request):
    logid = request.session.get('loginid')
    if logid:
        institution = Tbl_institution.objects.get(loginid=request.session['loginid'])
        enquiry = Tbl_enquiry.objects.filter(status="Not Confirmed",institutionid=institution)
        return render(request,'Institution/enquiryview.html',{'enquiry':enquiry})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
# def enquiryaccept(request,id):
#     if request.method == "POST":
#         # Fetch the request object using ID
#         request_obj = get_object_or_404(Tbl_enquiry,enquiryid=id)

#         # Create a new schedule entry
#         sob = Tbl_schedule()
#         sob.enquiryid = request_obj  
#         sob.scheduledate = request.POST.get("scheduledate")
#         sob.status = "notcomplete" 
#         sob.save()
#         request_obj.status = "Accepted"
#         request_obj.save()

#         return HttpResponse("<script>alert('Successfully registered');"
#             "window.location='/institutionapp/schedule';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def enquiryreject(request,id):
    logid = request.session.get('loginid')
    if logid:
        eob = Tbl_enquiry.objects.get(enquiryid=id)
        eob.status="Rejected"
        eob.save()
        return HttpResponse("<script>alert('Rejected..');window.location='/institutionapp/enquiryview';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def schedule(request,id):
    logid = request.session.get('loginid')
    if logid:
        enquiry = Tbl_enquiry.objects.get(enquiryid=id)
        return render(request,'Institution/schedule.html',{'enquiry':enquiry})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def scheduleprocess(request,id):
    logid = request.session.get('loginid')
    if logid:
        enquiry = Tbl_enquiry.objects.get(enquiryid=id)
        return render(request,'Institution/scheduleprocess.html',{'enquiry':enquiry})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def schedule_process(request,id):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            request_obj = get_object_or_404(Tbl_enquiry,enquiryid=id)

            enquiryid=request.POST.get("enquiryid")
            scheduledate = request.POST.get("scheduledate") #textboxname
            sob = Tbl_schedule()
            sob.scheduledate = scheduledate
            sob.status = "confirmed"
            sob.enquiryid = Tbl_enquiry.objects.get(enquiryid=enquiryid)
            request_obj.status = "Accepted"
            request_obj.save()
            if Tbl_schedule.objects.filter(scheduledate=scheduledate,enquiryid=enquiryid).exists():
                return HttpResponse("<script>alert('Already Exists..');window.location='/institutionapp/Index';</script>")
            else:
                sob.save()
                return HttpResponse("<script>alert('Successfully Inserted..');window.location='/institutionapp/Index';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def equipmentview(request):
    logid = request.session.get('loginid')
    if logid:
        equipment =Tbl_equipment.objects.all()
        return render(request,'Institution/equipmentviews.html',{'equipment':equipment})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def requests(request,id):
    logid = request.session.get('loginid')
    if logid:
        institution = Tbl_institution.objects.get(loginid=request.session['loginid'])
        equipment = Tbl_equipment.objects.get(equipmentid=id)
        return render(request, "Institution/requests.html",{'institution':institution,'equipment':equipment})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def requests_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            equipmentid=request.POST.get("equipment")
            institutionid=request.POST.get("institution")
            requesteddate = request.POST.get("requesteddate") #textboxname
            count = int(request.POST.get("count"))
            totalamount = request.POST.get("totalamount")
            equipment = get_object_or_404(Tbl_equipment, equipmentid=equipmentid)

            # Check if requested count is available in stock
            if count > equipment.equipmentstock:
                return HttpResponse("<script>alert('Not enough stock available. Please reduce the quantity.');window.location='/disabledpersonapp/Index';</script>")
            # Check if a similar request already exists
            if Tbl_request2.objects.filter(requesteddate=requesteddate, equipmentid=equipmentid, institutionid=institutionid).exists():
                return HttpResponse("<script>alert('Request already exists.');window.location='/institutionapp/Index';</script>")

            # Create request entry
            rob = Tbl_request2()
            rob.status = "Not Confirmed"
            rob.requesteddate = requesteddate
            rob.count = count
            rob.totalamount = totalamount
            rob.equipmentid = Tbl_equipment.objects.get(equipmentid=equipmentid)
            rob.institutionid = Tbl_institution.objects.get(institutionid=institutionid)
            rob.save()
            # Reduce stock
            return HttpResponse("<script>alert('Request successfully placed.');window.location='/institutionapp/Index';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def requestdetailsviews(request):
    logid = request.session.get('loginid')
    if logid:
        id = Tbl_institution.objects.get(loginid=request.session['loginid'])
        requests = Tbl_request2.objects.filter(institutionid=id).exclude(status__in=["Paid"])
        return render(request,'Institution/requestdetailsviews.html',{'requests':requests})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def payments(request,id):
    logid = request.session.get('loginid')
    if logid:
        payment = Tbl_request2.objects.get(requestid=id)
        return render(request, "Institution/payments.html",{'payment':payment})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def payments_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            requestid=request.POST.get("requestid")
            amount = request.POST.get("amount") #textboxname
            pob = Tbl_payment2()
            pob.status = "Paid"
            pob.amount = amount
            pob.requestid = Tbl_request2.objects.get(requestid=requestid)
            if Tbl_payment2.objects.filter(amount=amount,requestid=requestid).exists():
                return HttpResponse("<script>alert('Already Exists..');window.location='/institutionapp/Index';</script>")
            else:
                pob.save()
                request = Tbl_request2.objects.get(requestid=requestid)
                request.status = "paid"
                request.save()
                return HttpResponse("<script>alert('Successfully Inserted..');window.location='/institutionapp/Index';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def jobposting(request):
    logid = request.session.get('loginid')
    if logid:
        institution = Tbl_institution.objects.get(loginid=request.session['loginid'])
        return render(request, "Institution/jobposting.html",{'institution':institution})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def jobreg_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            institutionid=request.POST.get("institution")
            jtitle = request.POST.get("jobtitle") #textboxname
            jrequirements = request.POST.get("requirments")
            jdeadline = request.POST.get("deadline")
            jcontactemail = request.POST.get("contactemail")
            jdesc = request.POST.get("jobdesc")
            jimage = request.FILES["jobimage"] #filename
            job = Tbl_jobposting()
            job.jobtitle = jtitle
            job.requirments = jrequirements
            job.deadline = jdeadline
            job.contactemail = jcontactemail
            job.jobdesc = jdesc
            job.jobimage = jimage
            job.institutionid = Tbl_institution.objects.get(institutionid=institutionid)
            if Tbl_jobposting.objects.filter(jobtitle=jtitle,institutionid=institutionid).exists():
                return HttpResponse("<script>alert('Already Exists..');window.location='/Institution/jobposting';</script>")
            else:
                job.save()
                return HttpResponse("<script>alert('Successfully Inserted..');window.location='/institutionapp/jobposting';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewjob(request):
    logid = request.session.get('loginid')
    if logid:
        institution = Tbl_institution.objects.get(loginid=request.session['loginid'])
        job = Tbl_jobposting.objects.filter(institutionid=institution)
        return render(request,'Institution/viewjob.html',{'job':job})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deletejob(request, jobid):
    logid = request.session.get('loginid')
    if logid:
        job = Tbl_jobposting.objects.get(jobid=jobid) #select * from Tbl_category
        job.delete()
        return HttpResponse("<script>alert('Successfully Deleted..');window.location='/Institution/viewjob';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def editjob(request,id):
    logid = request.session.get('loginid')
    if logid:
        if request.method=='POST':
            jname=request.POST.get("jobtitle")
            jdesc=request.POST.get("jobdesc")
            jrequirements=request.POST.get("requirments")
            jcontact=request.POST.get("contactemail")
            jdeadline=request.POST.get("deadline")

            jobimage=request.POST.get("oldimage")
            job = Tbl_jobposting.objects.get(jobid=id)
            job.jobtitle = jname
            job.jobdesc = jdesc
            job.requirments = jrequirements
            job.contactemail = jcontact
            job.deadline = jdeadline
            job.jobimage = jobimage
            if 'jobimage' in request.FILES:
                job.jobimage = request.FILES["jobimage"]
            else:
                job.jobimage = request.POST.get("oldimage")

            job.save()
            return viewjob(request)
        job = Tbl_jobposting.objects.get(jobid=id)
        return render(request,"Institution/editjob.html",{'job':job})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewprofile(request):
    logid = request.session.get('loginid')
    if logid:
        institution1 = request.session['loginid']
        institution = Tbl_institution.objects.get(loginid=institution1)
        return render(request, "Institution/viewprofile.html",{'i':institution})
    else:
        return HttpResponse("<script>alert('Authentication Required Please Login First..');window.location='/Login';</script>")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def editprofile(request,id):
    logid = request.session.get('loginid')
    if logid:
        categories = Tbl_category.objects.all()
        if request.method=='POST':
            iname=request.POST.get("institutionname")
            regnumber=request.POST.get("regnumber")
            contactno=request.POST.get("contactno")
            email=request.POST.get("email")
            percentage=request.POST.get("percentage")
            institutiondesc=request.POST.get("institutiondesc")
            websiteurl=request.POST.get("websiteurl")
            categoryid=request.POST.get("categoryid")

            institutionimage=request.POST.get("oldimage")
            iob = Tbl_institution.objects.get(institutionid=id)
            iob.institutionname = iname
            iob.regnumber = regnumber
            iob.contactno = contactno
            iob.email = email
            iob.percentage = percentage
            iob.institutiondesc = institutiondesc
            iob.websiteurl = websiteurl
            iob.categoryid = Tbl_category.objects.get(categoryid=categoryid)


            iob.institutionimage = institutionimage
            if 'institutionimage' in request.FILES:
                iob.institutionimage = request.FILES["institutionimage"]
            else:
                iob.institutionimage = request.POST.get("oldimage")

            iob.save()
            return viewprofile(request)
        iob = Tbl_institution.objects.get(institutionid=id)
        return render(request,"Institution/editprofile.html",{'iob':iob,'category':categories})
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
