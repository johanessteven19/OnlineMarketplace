from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'pages/index.html',{})

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
