from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('registervisitor/',views.registervisitor,name='registervisitor'),
    path('registerorganizer/',views.registerorganizer,name='registerorganizer'),
    path('ewallet/',views.ewallet,name='ewallet'),
    path('addewallet/',views.addewallet,name='addewallet'),
    path('organizer/',views.organizer,name='organizer'),
    path('createevent/',views.createEvent,name ='createevent'),
    path('edit/',views.update,name='edit'),
    path('editevent/',views.editEvent,name='editevent'),
    path('registerevent/',views.registerEvent,name='registerevent'),
    path('mytransactions/', views.myTransactions,name='mytransactions'),
    path('deletetransactions/', views.deleteTransactions,name='deletetransactions'),
    path('transaction-payment/', views.transactionPayment, name='transactionPayment'),
    path('create-testimonies/', views.createTestimonies, name='createTestimonies'),
    path('view-testimonies/', views.viewTestimonies, name='viewTestimonies'),
    path('view-event-detail/', views.viewEventDetail, name='viewEventDetail'),
    path('organizer-profile/', views.organizerProfile, name='organizerProfile'),
    path('profit-summary/', views.profitSummary, name='profitSummary'),
    path('update-delete-testimony/', views.updateDeleteTestimony, name='updateDeleteTestimony'),
    path('login/',views.login,name='login'),
    path('loginvisitor/',views.loginVisitor,name='loginvisitor'),
    path('',views.landingpage,name='landingpage')
]