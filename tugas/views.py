from django.shortcuts import render,redirect
from django.db import connection, InternalError


# Create your views here.
from django.urls import reverse

from tugas.datalayer import dictfetchall
from tugas.forms import LoginForm
from tugas.templatetags.tags import is_authenticated


def landingpage(request):
    context = {'request': request}
    if is_authenticated(context):
        page = int(request.GET.get('page', 1))

        cursor = connection.cursor()
        cursor.execute(
            'SELECT T.theme_name, E.name,E.organizer_email,L.venue_name,L.address,L.city,E.start_date,E.end_date,E.end_time,E.start_time,E.end_time,E.total_capacity '
            'FROM event.EVENT E, event.LOCATION L, event.EVENT_LOCATION EL, event.THEME T '
            'WHERE T.event_id = E.event_id AND L.code= EL.location_code AND EL.id_event = E.event_id '
            'LIMIT %(pages)s OFFSET %(first_page)s', {'first_page': (page - 1) * 5, 'pages': 5})
        event_list = dictfetchall(cursor)

        context = {
            'event': event_list,
            'profile': profile,
            **context,
            'page': page,
        }
        return render(request, 'pages/index.html', context)

    return render(request, 'pages/landingpage.html', {})


def profile(request):
    profile = request.session.get('profile')
    credentials = request.session.get('credentials')
    context = {
        'request': request,
        'profile': profile,
    }
    return render(request, 'pages/profile.html', context)


def editprofile(request):
    return render(request, 'pages/editprofile.html', {})


def registervisitor(request):
    if (request.method == "POST"):
        profile = {}
        data = request.POST
        email = data['your_email']
        password = data['your_password']
        fname = data['your_fname']
        lname = data['your_lname']
        cursor = connection.cursor()
        try:
            cursor.execute("SET search_path TO EVENT;")
            cursor.execute("INSERT INTO EVENT.USER VALUES (%(email)s, %(password)s);",
                           {'email': email, 'password': password})
            cursor.execute("INSERT INTO EVENT.VISITOR VALUES (%(email)s, %(fname)s, %(lname)s);",
                           {'email': email, 'fname': fname, 'lname': lname})
        except InternalError:
            return render(request, 'pages/registerorganizer.html', {'message': "You've already created the account!"})
        profile['first_name'] = fname
        profile['last_name'] = lname
        return render(request, 'pages/index.html', {'profile': [profile]})

    else:
        return render(request, 'pages/registervisitor.html', {})


def registerorganizer(request):
    if (request.method == "POST"):
        profile = {}
        data = request.POST
        email = data['your_email']
        password = data['your_password']
        fname = data['your_fname']
        lname = data['your_lname']
        npwp = data['your_npwp_ktp']
        cursor = connection.cursor()
        try:
            cursor.execute("SET search_path TO EVENT;")
            cursor.execute("INSERT INTO EVENT.USER VALUES (%(email)s, %(password)s);",
                           {'email': email, 'password': password})
            cursor.execute("INSERT INTO EVENT.ORGANIZER VALUES (%(email)s, %(npwp)s);", {'email': email, 'npwp': npwp})
        except InternalError:
            return render(request, 'pages/registerorganizer.html', {'message': "You've already created the account!"})
        profile['first_name'] = fname
        profile['last_name'] = lname
        return render(request, 'pages/organizer.html', {'profile': [profile]})
    else:
        return render(request, 'pages/registerorganizer.html', {})


def ewallet(request):
    return render(request, 'pages/ewallet.html', {})


def addewallet(request):
    return render(request, 'pages/addewallet.html', {})


def organizer(request):
    return render(request, 'pages/organizer.html', {})


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
        type_id = cursor.execute('SELECT type_id FROM event.TYPE WHERE type_name = %(eventtype)s', {'eventtype': eventtype})
        organizer_email = cursor.execute("SELECT email FROM EVENT.ORGANIZER")

        cursor.execute("INSERT INTO EVENT.EVENT VALUES (%(event_id)s, %(eventname)s, %(start_date)s, %(end_date)s, %(start_time)s, %(end_time)s, %(description)s, %(total_capacity)s, %(total_available_capacity)s, %(type_id)s, %(organizer_email)s)",
        {'event_id': event_id, 'eventname': name, 'start_date': start_date, 'end_date': end_date, 'start_time': start_time, 'end_time': end_time, 'description': description, 'total_capacity': total_capacity, 'total_available_capacity': total_available_capacity, 'type_id': type_id, 'organizer_email': organizer_email})
    else:
        return render(request,'pages/createevent.html',{})


def editEvent(request):
    return render(request, 'pages/editevent.html', {})


def update(request):
    return render(request, 'pages/edit.html', {})


def registerEvent(request):
    return render(request, 'pages/registerevent.html', {})


def myTransactions(request):
    return render(request, 'pages/mytransactions.html', {})


def deleteTransactions(request):
    return render(request, 'pages/deletetransaction.html', {})


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


def login(request):
    if (request.method == "POST"):
        form = LoginForm(request.POST)
        try:
            if form.is_valid():
                email = form.cleaned_data.get('email')
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM event.organizer WHERE email = %(email)s', {'email': email})
                res1 = dictfetchall(cursor)
                npwp = res1[0]['npwp']

                profile = {
                    'npwp': npwp,
                    **form.cleaned_data,
                    'type': 'organizer',
                }

                request.session['profile'] = profile
                request.session['credentials'] = {**form.cleaned_data, }

                return redirect(reverse('landingpage'))
        except IndexError:
            pass

        message = 'ACCOUNT IS NOT FOUND'
        return render(request, 'registration/login.html', {'message': message})
    else:
        return render(request, 'registration/login.html', {})


def loginVisitor(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        try:
            if form.is_valid():
                email = form.cleaned_data.get('email')
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM event.VISITOR WHERE email = %(email)s', {'email': email})
                res1 = dictfetchall(cursor)
                first_name = res1[0]['first_name']
                last_name = res1[0]['last_name']


                profile = {
                    'first_name': first_name,
                    'last_name': last_name,
                    **form.cleaned_data,
                    'type': 'visitor',
                }

                request.session['profile'] = profile
                request.session['credentials'] = {**form.cleaned_data, }

                return redirect(reverse('landingpage'))
        except IndexError:
            pass

        message = 'ACCOUNT IS NOT FOUND'
        return render(request, 'registration/loginVisitor.html', {'message': message})
    else:
        return render(request, 'registration/loginVisitor.html', {})

def logout(request):
    profile = request.session.get('profile')
    credentials = request.session.get('credentials')
    if profile:
        del request.session['profile']

    if credentials:
        del request.session['credentials']

    return redirect(reverse('landingpage'))

# host : ec2-54-175-243-75.compute-1.amazonaws.com
# database: d40bv1a9pdpmo0
# user : msoobvwvovwzyi
# port : 5432
# password : 2cb80209623cb2d61652ba09fd10d1d011a7edb48ae10bc1a55b3dd8d9b184c2
