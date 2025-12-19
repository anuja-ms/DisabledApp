from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from GuestApp.models import Tbl_login,Tbl_institution,Tbl_disabledperson
from AdminApp.models import Tbl_district,Tbl_location,Tbl_category,Tbl_equipment,Tbl_scholarship


# Create your views here.
def Login(request):
    return render(request,'Guest/Login.html')
def login_process(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if Tbl_login.objects.filter(username=username,password=password).exists():
            logindata = Tbl_login.objects.get(username=username,password=password)
            request.session['loginid']=logindata.loginid
            role =logindata.role
            if role =="admin":
                return redirect('/adminapp/adminhome/')
            elif role == 'institution' :
                if logindata.status == 'Accepted':
                    return redirect('/institutionapp/Index/')
                else:
                    return HttpResponse("<script>alert('Request not accepted');window.location='/guestapp/login';</script")
            elif role == 'disabledperson':
                    return redirect('/disabledpersonapp/Index')
            else:
                    return HttpResponse("<script>alert('Not an authorized institution');window.location='/guestapp/login';</script")
        else:
         context = {"error": "Incorrect username or password"}
         return render(request,'Guest/Login.html',context)                
def Index(request):
    return render(request,'Guest/Index.html')
def institutionreg(request):
    district = Tbl_district.objects.all()
    category = Tbl_category.objects.all()
    return render(request,'Guest/Institutionreg.html',{'district':district,'category':category})
def institutionreg_process(request):
    if request.method == "POST":
        lob = Tbl_login()
        lob.username = request.POST.get("username")
        lob.password = request.POST.get("password")
        lob.role = "institution"
        lob.status = "Not Confirmed"


        if Tbl_login.objects.filter(username=request.POST.get("username")).exists():
            return HttpResponse("<script>alert('Already Exists..'); window.location='/guestapp/Indexx';</script>")
        else:
            lob.save()

            iob = Tbl_institution()
            iob.institutionname = request.POST.get("institutionname")
            iob.regnumber = request.POST.get("regnumber")
            iob.email = request.POST.get("email")
            iob.contactno = request.POST.get("contactno")
            iob.websiteurl = request.POST.get("websiteurl")
            iob.locationid = Tbl_location.objects.get(locationid=request.POST.get("location"))
            iob.institutiondesc = request.POST.get("institutiondesc")
            iob.percentage = request.POST.get("percentage")
            iob.institutionimage= request.FILES["institutionimage"] 
            iob.categoryid = Tbl_category.objects.get(categoryid=request.POST.get("category"))
            iob.loginid = lob
            iob.save()
            return HttpResponse("<script>alert('Successfully registered'); window.location='/';</script>")
def disabledpersonreg(request):
    district = Tbl_district.objects.all()
    category = Tbl_category.objects.all()
    return render(request,'Guest/disabledpersonreg.html',{'district':district,'category':category})
def disabledpersonreg_process(request):
    if request.method == "POST":
        lob = Tbl_login()
        lob.username = request.POST.get("username")
        lob.password = request.POST.get("password")
        lob.role = "disabledperson"
        lob.status = "Confirmed"


        if Tbl_login.objects.filter(username=request.POST.get("username")).exists():
            return HttpResponse("<script>alert('Already Exists..'); window.location='/guestapp/Indexx';</script>")
        else:
            lob.save()

            dob = Tbl_disabledperson()
            dob.personname = request.POST.get("personname")
            dob.address = request.POST.get("address")
            dob.contactno = request.POST.get("contactno")
            dob.email = request.POST.get("email")
            dob.dob = request.POST.get("dob")
            dob.locationid = Tbl_location.objects.get(locationid=request.POST.get("location"))
            dob.categoryid = Tbl_category.objects.get(categoryid=request.POST.get("category"))
            dob.percentage = request.POST.get("percentage")
            dob.percentage = request.POST.get("percentage")
            dob.disabilitydetails = request.POST.get("disabilitydetails")
            dob.idproof= request.FILES["idproof"] 
            dob.pname = request.POST.get("pname")
            dob.pcontact = request.POST.get("pcontact")
            dob.loginid = lob
            dob.save()
            return HttpResponse("<script>alert('Successfully registered'); window.location='/';</script>")
def viewmoreinstitutions(request,id):
    request.session['institutionid'] = id
    institution = Tbl_institution.objects.filter(institutionid=id)
    return render(request, "Guest/viewmoreinstitutions.html",{'institution':institution})
def fillinstitutions(request):
    sid = int(request.POST.get("sid"))
    categoryid = int(request.POST.get("categoryid"))
    institutions = Tbl_institution.objects.filter(locationid=sid, categoryid=categoryid).values()
    return JsonResponse(list(institutions),safe=False)
def institutionview(request):
    category =Tbl_category.objects.all()
    districts = Tbl_district.objects.all()
    institution = Tbl_institution.objects.all() #select * from Tbl_category
    return render(request,'Guest/institutionview.html',{'institution':institution,'category':category,'districts':districts})
def equipmentsview(request):
    equipment =Tbl_equipment.objects.all()
    return render(request,'Guest/equipmentsview.html',{'equipment':equipment})
