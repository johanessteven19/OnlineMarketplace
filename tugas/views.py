from django.shortcuts import render, redirect
from django.db import connection


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
            'LIMIT %(last_page)s OFFSET %(first_page)s', {'first_page': (page - 1) * 5, 'last_page': page * 5})
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
    return render(request, 'pages/profile.html', {})


def editprofile(request):
    return render(request, 'pages/editprofile.html', {})


def registervisitor(request):
    return render(request, 'pages/registervisitor.html', {})


def registerorganizer(request):
    return render(request, 'pages/registerorganizer.html', {})


def ewallet(request):
    return render(request, 'pages/ewallet.html', {})


def addewallet(request):
    return render(request, 'pages/addewallet.html', {})


def organizer(request):
    return render(request, 'pages/organizer.html', {})


def createEvent(request):
    return render(request, 'pages/createevent.html', {})


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
        if form.is_valid():
            email = form.cleaned_data.get('email')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM event.organizer WHERE email = %(email)s', {'email': email})
            res1 = dictfetchall(cursor)
            npwp = res1[0]['npwp']

            profile = {
                'npwp': npwp,
                **form.cleaned_data,
            }

            request.session['profile'] = profile
            request.session['credentials'] = {**form.cleaned_data, }

            return redirect(reverse('landingpage'))
        else:
            message = 'ACCOUNT IS NOT FOUND'
            return render(request, 'registration/login.html', {'message': message})
    else:
        return render(request, 'registration/login.html', {})


def loginVisitor(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
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
            }

            request.session['profile'] = profile
            request.session['credentials'] = {**form.cleaned_data, }

            return redirect(reverse('landingpage'))
        else:
            message = 'ACCOUNT IS NOT FOUND'
            return render(request, 'registration/loginVisitor.html', {'message': message})
    else:
        return render(request, 'registration/loginVisitor.html', {})
