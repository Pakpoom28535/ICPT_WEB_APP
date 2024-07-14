"""ICPT2024 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from polls import views
from django.conf import settings
from django.conf.urls.static import *
urlpatterns = [
   path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('Applicant-Dashboard', views.ApplicantDashboard, name='Applicant-Dashboard'),
    path('thailandinfo', views.thailandinfo, name='thailandinfo'),
      path('Client-Register', views.Register, name='Register'),
      path('Forgot-Password', views.Forgot, name='Forgot'),
      path('Applicant-Dashboard', views.ApplicantDashboard, name='Applicant-Dashboard'),
       path('Instruction', views.Instruction, name='Instruction'),
       path('CreateSubmission', views.CreateSubmission, name='CreateSubmission'),
       path('ViewSubmission', views.ViewSubmission, name='ViewSubmission'),
       path('Invitation-Letter', views.InvitationLetter, name='Invitation-Letter'),
       path('Letter-Generated', views.LetterGen, name='Letter-Generated'),
       path('Payment-Instruction', views.PaymentInstruction, name='Payment-Instruction'),
        path('Upload-payment', views.Uploadpayment, name='Upload-payment'),
        path('Ticket', views.Tickets, name='Ticket'),
        path('Receipt', views.Receipts, name='Receipt'),
       path('ViewPayment-Status', views.ViewPaymentStatus, name='ViewPayment-Status'),
       path('Hotel-Reservation', views.HotelReservation, name='Hotel-Reservation'),
       path('Staff-Login', views.StaffLogin, name='Staff-Login'),
       path('Staff-Dashboard', views.StaffDashboard, name='Staff-Dashboard'),
        path('Applicant-List', views.ApplicantList, name='Applicant-List'),
        path('Visitor-List', views.VisitorList, name='Visitor-List'),
        path('Register-Type', views.RegisterType, name='Register-Type'),
         path('email', views.sendmail, name='email'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
