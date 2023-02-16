from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.homeview,name ='home'),
    path('sendmail/',views.send,name = 'emailsender'),
    path('otpmail/',views.otpgen,name = 'otpgen'),
    
]
