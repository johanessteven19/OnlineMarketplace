from django.shortcuts import render,redirect
from django.db import connection

# Create your views here.
def home(request):
    return render(request,'pages/index.html',{})
def landingpage(request):
    return render(request,'pages/landingpage.html',{})

def profile(request):
    return render(request,'pages/profile.html',{})
    
def editprofile(request):
    return render(request,'pages/editprofile.html',{})

def registervisitor(request):
    if(request.method=="POST"):
        profile = {}
        data= request.POST
        email = data['your_email']
        password = data['your_password']
        fname = data['your_fname']
        lname = data['your_lname']
        cursor = connection.cursor()
        cursor.execute("SET search_path TO EVENT;")
        cursor.execute("INSERT INTO EVENT.USER VALUES (%(email)s, %(password)s);",
                                {'email': email, 'password': password})
        cursor.execute("INSERT INTO EVENT.VISITOR VALUES (%(email)s, %(fname)s, %(lname)s);", {'email': email, 'fname': fname, 'lname': lname})
        profile['first_name']=fname
        profile['last_name'] = lname
        return render(request,'pages/index.html',{'profile':[profile]})

    else:
        return render(request,'pages/registervisitor.html',{})
    
def registerorganizer(request):
    if(request.method=="POST"):
        profile = {}
        data= request.POST
        email = data['your_email']
        password = data['your_password']
        fname = data['your_fname']
        lname = data['your_lname']
        npwp = data['your_npwp_ktp']
        cursor = connection.cursor()
        cursor.execute("SET search_path TO EVENT;")
        cursor.execute("INSERT INTO EVENT.USER VALUES (%(email)s, %(password)s);",
                                {'email': email, 'password': password})
        cursor.execute("INSERT INTO EVENT.ORGANIZER VALUES (%(email)s, %(npwp)s);", {'email': email, 'npwp': npwp})
        profile['first_name']=fname
        profile['last_name'] = lname
        return render(request,'pages/index.html',{'profile':[profile]})
    else:
        return render(request,'pages/registerorganizer.html',{})

def ewallet(request):
    return render(request,'pages/ewallet.html',{})
    
def addewallet(request):
    return render(request,'pages/addewallet.html',{})

def organizer(request):
    return render(request,'pages/organizer.html',{})

def createEvent(request):
    return render(request,'pages/createevent.html',{})

def editEvent(request):
    return render(request,'pages/editevent.html',{})

def update(request):
    return render(request,'pages/edit.html',{})

def registerEvent(request):
    return render(request,'pages/registerevent.html',{})

def myTransactions(request):
    return render(request,'pages/mytransactions.html',{})

def deleteTransactions(request):
    return render(request,'pages/deletetransaction.html',{})

def transactionPayment(request):
    return render(request, 'pages/transactionPayment.html', {})

def createTestimonies(request):
    return render(request, 'pages/createTestimonies.html', {})

def viewTestimonies(request):
    return render(request, 'pages/viewTestimonies.html', {})

def viewEventDetail(request):
    return render(request, 'pages/viewEventDetail.html', {})

def organizerProfile(request):
    return render(request, 'pages/organizerProfile.html', {})

def profitSummary(request):
    return render(request, 'pages/sharedProfit.html', {})

def updateDeleteTestimony(request):
    return render(request, 'pages/updatetestimony.html', {})
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
def login(request):
    if(request.method=="POST"):
        data= request.POST
        email = data['email']
        password = data['Password']
        cursor = connection.cursor()
        cursor.execute("SET search_path TO EVENT;")
        cursor.execute('SELECT password FROM EVENT.USER WHERE email = %(email)s',{'email':email})
        result = dictfetchall(cursor)
        if(result[0]['password']==password):
            cursor.execute('SELECT email FROM ORGANIZER WHERE email = %(email)s',{'email':email})
            res= dictfetchall(cursor)
            if(res[0]['email']==email):
                cursor.execute('SELECT T.theme_name, E.name,E.organizer_email,L.venue_name,L.address,L.city,E.start_date,E.end_date,E.end_time,E.start_time,E.end_time,E.total_capacity FROM EVENT E, LOCATION L, EVENT_LOCATION EL,THEME T WHERE T.event_id = E.event_id AND L.code= EL.location_code AND EL.id_event = E.event_id AND E.organizer_email=%(email)s ;',{'email':email})
                event_list = dictfetchall(cursor)
                return render(request,'pages/organizer.html',{'event':event_list})
        else:
            message ='ACCOUNT IS NOT FOUND'
            return render(request,'registration/login.html',{'message':message})
    else:
        return render(request,'registration/login.html',{})
def loginVisitor(request):
    if(request.method=="POST"):
        profile={}
        data= request.POST
        email = data['email']
        password = data['Password']
        cursor = connection.cursor()
        cursor.execute("SET search_path TO EVENT;")
        cursor.execute('SELECT password FROM EVENT.USER WHERE email = %(email)s',{'email':email})
        result = dictfetchall(cursor)
        if(result[0]['password']==password):
            cursor.execute('SELECT * FROM VISITOR WHERE email = %(email)s',{'email':email})
            res1= dictfetchall(cursor)
            first_name= res1[0]['first_name']
            last_name = res1[0]['last_name']
            profile['first_name']=first_name
            profile['last_name'] = last_name
            if(res1[0]['email']==email):
                cursor.execute('SELECT T.theme_name, E.name,E.organizer_email,L.venue_name,L.address,L.city,E.start_date,E.end_date,E.end_time,E.start_time,E.end_time,E.total_capacity FROM EVENT E, LOCATION L, EVENT_LOCATION EL,THEME T WHERE T.event_id = E.event_id AND L.code= EL.location_code AND EL.id_event = E.event_id;')
                event_list = dictfetchall(cursor)
                return render(request,'pages/index.html',{'event':event_list,'profile':[profile]})
        else:
            message ='ACCOUNT IS NOT FOUND'
            return render(request,'registration/loginVisitor.html',{'message':message})
    else:
        return render(request,'registration/loginVisitor.html',{})

# host : ec2-54-175-243-75.compute-1.amazonaws.com
# database: d40bv1a9pdpmo0
# user : msoobvwvovwzyi
# port : 5432
# password : 2cb80209623cb2d61652ba09fd10d1d011a7edb48ae10bc1a55b3dd8d9b184c2