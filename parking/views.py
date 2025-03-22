import math,random
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Registration
from .models import Contact
from .models import Complaints , Vehicleentry , Vehicleexit
from django.contrib import messages

f = 0

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = Registration()
        if username =='admin' and  password =='admin123' :
            return render(request, 'adminpage.html')

        if Registration.objects.filter(username = username,password=password).all():
            user = Registration.objects.filter(username = username,password=password).all()
            n = on()
            context= {
                'f':n,
            }
            return render(request,'entryex.html',context)
        else:
            messages.info(request,"Invalid username or password")
            return redirect('/index/')
    else:
        return render(request,'index.html')
    #params = {'name':'parking', 'place': 'amity'}
    #return render(request, 'index.html', params)


def on():
    global f
    f = 1
    return f

def check():
    global f
    return f



def entryex(request):
    params = {'name': 'parking', 'place': 'mars'}
    return render(request,'entryex.html', params)

def signup(request):
    if request.method == "POST":
        print(request)
        fname=request.POST.get('fname','')
        lname = request.POST.get('lname', '')
        email=request.POST.get('email','')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        passwordr = request.POST.get('passwordr', '')
        addressfor = request.POST.get('addressfor', ' null ')
        contactnumber = request.POST.get('contactnumber', '')
        dob = request.POST.get('dob', '')
        gender = request.POST.get('gender', '')
        ques = request.POST.get('ques', '')
        answer = request.POST.get('answer', '')
        if password == passwordr:
          signup = Registration(fname=fname , lname=lname,email=email, username=username , password=password,
                              passwordr=passwordr ,addressfor=addressfor ,contactnumber=contactnumber ,
                              dob=dob,gender=gender,ques=ques,answer=answer)
          signup.save()
          messages.success(request, 'Your account has been created successfully!')
        else:
          messages.success(request, 'Password doesnt matches')
          return redirect('/signup/')


    return render(request , 'signup.html')

def forgot(request):
    if request.method == 'POST':
        username = request.POST['username']
        ques = request.POST['ques']
        answer = request.POST['answer']
        user = Registration()
        
        if Registration.objects.filter(username = username,ques=ques,answer=answer).all():
            user = Registration.objects.filter(username = username,ques=ques,answer=answer).all()
            n = on()
            context= {
                'f':n,
            }
            return render(request,'entryex.html',context)
        else:
            messages.info(request,"Invalid username")
            return redirect('/forgot/')
    else:
        return render(request,'forgot.html')
    #params = {'name': 'parking', 'place': 'mars'}
    #return render(request,'forgot.html', params)

stringspace = "123456"
stringfloor = "123"
stringtag = "29876543"

lentspace = len(stringspace)
spaceallot1 = " "
spaceallot2 = " "
for i in range(1):
   spaceallot1 +=stringspace[math.floor(random.random()*lentspace)]
for i in range(2):
   spaceallot2 +=stringspace[math.floor(random.random()*lentspace)]

lentfloor = len(stringfloor)
floorallot = " "
for i in range(1):
   floorallot +=stringfloor[math.floor(random.random()*lentfloor)]

lenttag = len(stringtag)
tagallot = " "
for i in range(2):
   tagallot +=stringtag[math.floor(random.random()*lenttag)]


from datetime import date
todaydate = date.today()

#import datetime
#from datetime import time
#todaytime = datetime.time()


#import datetime
#currentDT = datetime.datetime.now()

#import time
# now = time.strftime("%c")
#timeto = time.strftime("%X")

from datetime import *
dt=datetime.now()
t1=dt.strftime("%H:%M:%S")


def vehicleentry(request):
    n = 0
    z = check()
    if z == 1:
        n = 1
    context = {
        'n': n,
    }
    if request.method == "POST":
        print(request)
        vnumber = request.POST.get('vnumber', '')
        vtype = request.POST.get('vtype', '')
        contactno = request.POST.get('contactno', '')
        date = todaydate
        intime = datetime.now().strftime("%H:%M:%S")
        spacealloted = spaceallot1 + spaceallot2
        flooralloted = floorallot
        tagno = ('f')+ flooralloted + spaceallot1 + tagallot
        # spacealloted = request.POST.get('spacealloted', ' null ')
        # flooralloted = request.POST.get('flooralloted', ' null ')
        # tagno = request.POST.get('tagno', ' null ')
        venter = Vehicleentry(vnumber=vnumber,vtype=vtype,contactno=contactno,date=date,
                              intime=intime,spacealloted=spacealloted,flooralloted=flooralloted,
                              tagno=tagno)
        venter.save()
        return render(request, 'vehicleentry.html', {'n': 1, 'submitted': True})

    return render(request, 'vehicleentry.html',context)

    #params = {'name': 'parking', 'place': 'mars'}
    #return render(request,'vehicleentry.html', params)

def aboutus(request):
    params = {'name': 'parking', 'place': 'mars'}
    return render(request,'aboutus.html', params)

def complaint(request):
    if request.method == "POST":
        print(request)
        fname = request.POST.get('fname', '')
        mname = request.POST.get('mname', '')
        lname = request.POST.get('lname', '')
        contactno = request.POST.get('contactno', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', ' null ')
        space = request.POST.get('space', ' null ')
        message = request.POST.get('message', ' null ')
        complaint = Complaints(fname=fname,mname=mname, lname=lname, contactno=contactno, email=email,
                               address=address, space=space, message=message)
        complaint.save()
        params = {'name': 'parking', 'place': 'mars'}
        return render(request,'complaint.html', params)
    return render(request, 'complaint.html')

    #params = {'name': 'parking', 'place': 'mars'}
    #return render(request,'complaint.html', params)

def fare(request):
    params = {'name': 'parking', 'place': 'mars'}
    return render(request,'fare.html', params)

def home(request):
    params = {'name': 'parking', 'place': 'mars'}
    return render(request,'home.html', params)

def maps(request):
    params = {'name': 'parking', 'place': 'mars'}
    return render(request,'maps.html', params)

t2=dt.strftime("%H:%M:%S")

def vehicleexit(request):
    n = 0
    z = check()
    if z == 1:
        n = 1
    context = {
        'n': n,
    }
    if request.method == 'POST':
        vno = request.POST['vno']
        vty = request.POST['vty']
        tno = request.POST['tno']
        outtime = datetime.now().strftime("%H:%M:%S")
        farem = 0
        FMT = '%H:%M:%S'
        tdiff = datetime.strptime(t2, FMT) - datetime.strptime(t1, FMT)
        user = Vehicleentry()
        tc1 = timedelta(hours=6, minutes=00)
        tc2 = timedelta(hours=12, minutes=00)
        #if Vehicleentry.objects.filter(vnumber=vno, vtype=vty).all():
        user = Vehicleentry.objects.filter(vnumber=vno,vtype=vty,tagno=tno)
        if len(user)>0:
            if vty == 'two':
                if tdiff <= tc1:
                    farem = 15
                elif tdiff <= tc2:
                    farem = 25
                elif tdiff > tc2:
                    farem = 30
            elif vty == 'three':
                if tdiff <= tc1:
                    farem = 20
                elif tdiff <= tc2:
                    farem = 35
                elif tdiff > tc2:
                    farem = 40
            elif vty == 'four':
                if tdiff <= tc1:
                    farem = 30
                elif tdiff <= tc2:
                    farem = 50
                elif tdiff > tc2:
                    farem = 60
            else:
                farem = 0
            exitt = Vehicleexit(vno=vno,vty=vty,outtime=outtime,farem=farem,tno=tno)
            exitt.save()
            return HttpResponse('<h2>Vehicle found in the parking lot.</h2><br><span style="font-size:25px" class="psw"> Print <a href="/printexit/" style="color:blue" style="font-size:30px">Recipt</a></span>')
        else:
            return HttpResponse('<h2>Vehicle not found in parking lot.</h2>')
    else:
        return render(request, 'vehicleexit.html',context)

def contactus(request):
   if request.method == "POST":
       print(request)
       name= request.POST.get('name','')
       mail= request.POST.get('email','')
       contactno = request.POST.get('contactno', '')
       question = request.POST.get('question', '')
       contactus = Contact(name=name ,mail=mail, contactno=contactno , question=question)
       contactus.save()
   return render(request , 'contactus.html')

def printentry(request):
    # obj = Registration.objects.last()
    obj = Vehicleentry.objects.filter().last()
    return render(request, 'printentry.html', {'obj':obj})

def printexit(request):
    # obj = Registration.objects.last()
    obj = Vehicleexit.objects.filter().last()
    return render(request, 'printexit.html', {'obj':obj})

def printcontact(request):
    # obj = Registration.objects.last()
    obj = Contact.objects.filter().all()
    return render(request, 'printcontact.html', {'obj':obj})

def printcomplaint(request):
    # obj = Registration.objects.last()
    obj = Complaints.objects.filter().all()
    return render(request, 'printcomplaint.html', {'obj':obj})

def adminpage(request):
    params = {'name': 'parking', 'place': 'mars'}
    return render(request,'adminpage.html', params)

def printvehicles(request):
    obj = Vehicleentry.objects.filter().all()
    return render(request, 'printvehicles.html', {'obj': obj})

def searchingveh(request):
    obj = Vehicleentry.objects.all()
    return render(request, 'searchingveh.html', {'obj': obj})
from django.shortcuts import render
from .models import Vehicleentry

from django.shortcuts import render
from .models import Vehicleentry

def search_vehicle(request):
    query = request.GET.get('query')  # Retrieve the search term
    obj = None  # Default to None for no initial results
    if query:  # Perform search only if query is provided
        obj = Vehicleentry.objects.filter(vnumber=query)
    return render(request, 'searchingveh.html', {'obj': obj, 'query': query})



def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if username == 'admin' and password == 'admin':
            return render(request, 'adminpage.html')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('/adminlogin/')
    else:
        return render(request, 'adminlogin.html')
from django.shortcuts import render

def vehicle_entry(request):
    if request.method == 'POST':
        # Process form data here...
        submitted = True
        return render(request, 'your_template.html', {'n': 1, 'submitted': submitted})
    return render(request, 'your_template.html', {'n': 1})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicleentry

from django.shortcuts import get_object_or_404, render, redirect
from .models import Vehicleentry

def delete_vehicle(request, tagno):
    # Retrieve all matching vehicle entries
    vehicles = Vehicleentry.objects.filter(tagno=tagno)
    
    if not vehicles.exists():
        # Handle the case where no vehicle is found
        return HttpResponse("Vehicle not found.")
    
    if request.method == 'POST':
        if vehicles.count() >= 1:
            # Delete the single matching vehicle entry
            vehicles.first().delete()
            context={'message': 'Vehicle deleted.'}
            return render(request, 'searchingveh.html', context)
            
        else:
            context={'message': 'Multiple vehicles found. Cannot proceed with deletion.'}
            # Handle case when multiple vehicles match the same vnumber
            return render(request, 'searchingveh.html', context)
    
    return render(request, 'confirm_delete.html', {'vehicle': vehicles.first()})

from django.shortcuts import render, get_object_or_404
from .models import Registration

# View to display all users
def view_users(request):
    users = Registration.objects.all()  # Retrieve all user records
    context = {
        'users': users
    }
    return render(request, 'view_users.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from .models import Registration
from django.contrib import messages

# View to edit user details
def edit_user(request, mes_id):
    # Get the user object or return a 404 if not found
    user = get_object_or_404(Registration, mes_id=mes_id)
    
    if request.method == 'POST':
        # Get the updated details from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')
        password = request.POST.get('password')
        passwordr = request.POST.get('passwordr')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        ques = request.POST.get('ques')
        answer = request.POST.get('answer')
        # Update the user object
        user.username = username
        user.email = email
        user.contactnumber = contact_number
        user.addressfor = address
        user.password = password
        user.passwordr = passwordr
        user.fname = fname
        user.lname = lname
        user.dob = dob
        user.gender = gender
        user.ques = ques
        user.answer = answer
        user.save()
        
        messages.success(request, "User details updated successfully!")
        return redirect('view_users')
    
    context = {
        'user': user
    }
    return render(request, 'edit_user.html', context)


 # Adjust import according to your app's model

def delete_user(request, mes_id):
    if request.method == 'POST':
        # Get the user object or 404 if not found
        user = get_object_or_404(Registration, mes_id=mes_id)
        user.delete()
        messages.success(request, f'User with ID {mes_id} has been deleted successfully.')
        return redirect('view_users')  # Redirect to the admin home or a suitable page

    # If the request is not POST, redirect to a confirmation page or show an error
    messages.error(request, 'Invalid request.')
    return redirect('view_users')  # Adjust this as needed
