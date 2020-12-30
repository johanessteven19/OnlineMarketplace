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
    return render(request,'pages/registervisitor.html',{})
    
def registerorganizer(request):
    return render(request,'pages/registerorganizer.html',{})

def ewallet(request):
    return render(request,'pages/ewallet.html',{})
    
def addewallet(request):
    return render(request,'pages/addewallet.html',{})

def organizer(request):
    return render(request,'pages/organizer.html',{})

def createEvent(request):
    if(request.method=="POST"):
        # Ini placeholder
        data = request.POST
        name = data['eventname']
        description = data['eventdesc']
        theme_name = data['eventtheme']
        start_date = data['startdate']
        end_date = data['enddate']
        start_time = data['start_time']
        end_time = data['end_time']
        eventtype = data['eventtype']
        eventlocation = data['eventlocation']
        ticketclass = data['ticketclass']
        total_capacity = data['capacity']
        total_available_capacity = data['capacity']

        # table event : event_id(increment), name(from form), start_date(form), end_date(form), 
        #               start_time(form), end_time(form), 
        #               description(form), total_capacity(form --> ticketclass), 
        #               total_available_capacity(form-->ticketclass), type_id(SELECT FROM TYPE), 
        #               organizer_email(SELECT FROM ORGANIZER)
        int = 100
        event_id = "E" + int    # Auto-generate?
        int+=1
        cursor = connection.cursor()
        type_id = cursor.execute("SELECT type_id FROM TYPE WHERE type_name = %(eventtype)s',{'eventtype':eventtype}))
        organizer_email = cursor.execute("SELECT email FROM EVENT.ORGANIZER)

        cursor.execute("INSERT INTO EVENT.EVENT VALUES (%(event_id)s, %(eventname)s, %(start_date)s, %(end_date)s, %(start_time)s, %(end_time)s, %(description)s, %(total_capacity)s, %(total_available_capacity)s, %(type_id)s, %(organizer_email)s;",
        {'event_id': event_id, 'eventname': eventname, 'start_date': start_date, 'end_date': end_date, 'start_time': start_time, 'end_time': end_time, 'description': description, 'total_capacity': total_capacity, 'total_available_capacity': total_available_capacity, 'type_id': type_id, 'organizer_email': organizer_email})
    else:
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
                cursor.execute('SELECT T.theme_name, E.name, E.organizer_email, L.venue_name,L.address,L.city,E.start_date,E.end_date,E.end_time,E.start_time,E.end_time,E.total_capacity FROM EVENT E, LOCATION L, EVENT_LOCATION EL,THEME T WHERE T.event_id = E.event_id AND L.code= EL.location_code AND EL.id_event = E.event_id AND E.organizer_email=%(email)s ;',{'email':email})
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
