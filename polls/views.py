from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from django.contrib import messages

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from http import HTTPStatus
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from datetime import datetime, timedelta  
from django.db import models
from .models import *
from django.contrib.auth.models import User,Group
from django.core import serializers
######################## Service##################################
import random
import string
import json

import threading
def sendmail(name,mail,username,password,code):
    subject = 'Thank you for registering to our site'
    message = 'It means the world to us.'
    email_from = settings.EMAIL_HOST_USER
    html_mail = f'''
            <p class="greeting">Dear {name},</p>
            <p>We are pleased to inform you that your account on our website has been successfully created. Below are your login credentials:</p>
            <div class="credentials">
                <p><strong>CodeID:</strong> {code}</p>
                <p><strong>Username:</strong> {username}</p>
                <p><strong>Password:</strong> {password}</p>
            </div>
            <p>To log in, please visit our website at <a href="https://icpt-2025.eng.cmu.ac.th/">https://icpt-2025.eng.cmu.ac.th/</a> and enter your credentials.</p>
            <p>For security purposes, we recommend changing your password upon your first login. You can do this by navigating to the account settings section once you are logged in.</p>
            <p>If you encounter any issues or have any questions, please do not hesitate to contact our support team at <a href="mailto:icpt-2025@cmu.ac.th">icpt-2025@cmu.ac.th</a>.</p>
            <p>Thank you for choosing our services.</p>
            <div class="signature">
                <p>Best regards,</p>
                <p>CHIANG MAI UNIVERSITY<br>
                ADVANCED RAILWAY CIVIL AND FOUNDATION ENGINEERING CENTER<br>icpt-2025@cmu.ac.th</p>
            </div>
    '''
    recipient_list = [mail,]
    send_mail(subject, message, email_from, recipient_list, html_message=html_mail)
    return JsonResponse({"data": 'ok'}, status=HTTPStatus.OK)
def send_reset_email(email, new_password):
    subject = 'Password Reset Request'
    message = f'Your new password is: {new_password}'
    email_from = settings.EMAIL_HOST_USER
    html_mail = f'''
            <p class="greeting">Dear User,</p>
            <p>We have reset your password as per your request. Below is your new password:</p>
            <div class="credentials">
                <p><strong>New Password:</strong> {new_password}</p>
            </div>
            <p>Please log in using your new password and change it to something more secure at your earliest convenience.</p>
            <p>If you encounter any issues or have any questions, please do not hesitate to contact our support team.</p>
            <div class="signature">
                <p>Best regards,</p>
                <p>CHIANG MAI UNIVERSITY<br>
                ADVANCED RAILWAY CIVIL AND FOUNDATION ENGINEERING CENTER<br>icpt-2025@cmu.ac.th</p>
            </div>
    '''
    recipient_list = [email,]
    send_mail(subject, message, email_from, recipient_list, html_message=html_mail)
    return JsonResponse({"data": 'ok'}, status=HTTPStatus.OK)
def generate_random_code():
    # กำหนดความยาวของส่วนตัวอักษร
    text_length = 5
    # สร้างส่วนของตัวอักษรสุ่ม
    text_part = ''.join(random.choices(string.ascii_letters, k=text_length))
    # สร้างส่วนของตัวเลขสุ่ม
    number_part = random.randint(0, 9999)
    # รวมส่วนตัวอักษรและตัวเลขเข้าด้วยกัน
    return f"{text_part}{number_part}"
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
######################## Service##################################
def index(request):
    return render(request, "index.html")
def thailandinfo(request):
    return render(request, "thailandinfo.html")
def ApplicantDashboard(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('signin')
    return render(request, "Client/ApplicantSection/Applicant-Dashboard.html")
def Instruction(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('signin')
    return render(request, "Client/ApplicantSection/Abstract/Instruction.html")
def CreateSubmission(request):
    if request.method == 'POST':
        data = request.POST
        file = request.FILES.get('file')
        print(file)
        state_add =StateReview_User.objects.get(user__id=request.user.id,StateReview__step = 1)
        Review_User_History_ = Review_User_History()
        Review_User_History_.StateReview_User = state_add
        Review_User_History_.Submition_title =state_add.StateReview.StateReview_name+" : " +data['title']
        Review_User_History_.Submission_Code =generate_random_code()
        Review_User_History_.file = file
        Review_User_History_.save()
        return redirect('ViewSubmission')  # Redirect to a success page or another view
    if request.user.is_authenticated:
        pass
    else:
        return redirect('signin')
    return render(request, "Client/ApplicantSection/Abstract/CreateSubmission.html")
def ViewSubmission(request):
    if request.user.is_authenticated:
        ViewSubmission_ = Review_User_History.objects.all().order_by('created_at')
        ViewSubmission_ = ViewSubmission_.filter(StateReview_User__user__id  = request.user.id )
        context = {
            'data': ViewSubmission_,
            
        }

        return render(request, "Client/ApplicantSection/Abstract/ViewSubmission.html",context)
    else:
        return redirect('signin')
    
    
def InvitationLetter(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('signin')
    return render(request, "Client/ApplicantSection/Invitation/Invitation-Letter.html")
def LetterGen(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('signin')
    return render(request, "Client/ApplicantSection/Invitation/Letter-Generated.html")
def PaymentInstruction(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('signin')
    return render(request, "Client/ApplicantSection/RegistPayment/Payment-Instruction.html")
def Uploadpayment(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('signin')
    return render(request, "Client/ApplicantSection/RegistPayment/Upload-payment.html")
def ViewPaymentStatus(request):
    return render(request, "Client/ApplicantSection/RegistPayment/ViewPayment-Status.html")
def Tickets(request):
    return render(request, "Client/ApplicantSection/RegistPayment/Ticket.html")
def Receipts(request):
    return render(request, "Client/ApplicantSection/RegistPayment/Receipt.html")
def HotelReservation(request):
    return render(request, "Client/ApplicantSection/Hotel/Hotel-Reservation.html")
def StaffLogin(request):
    return render(request, "Client/StaffSection/Staff-Login.html")
def StaffDashboard(request):

            
    if request.user.is_authenticated:
        all_user = User.objects.filter(is_staff=False)
        
        # Filtering users by group
        qty_regular = all_user.filter(groups__id=1).count()
        qty_student = all_user.filter(groups__id=2).count()
        qty_visitor = all_user.filter(groups__id=3).count()
        
        qty_total = all_user.count()

        context = {
            'qty_regular': qty_regular,
            'qty_student': qty_student,
            'qty_visitor': qty_visitor,
            'qty_total': qty_total,
        }

        return render(request, "Client/StaffSection/Staff-Dashboard.html", context)
    else:
        return render(request, "Client/Login.html")
def ApplicantList(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        if data['action'] == '1':
                # Example query to filter StateReview_User based on UserProfile's codeno field
            StateReview_User_ = StateReview_User.objects.get(user__userprofile__codeno=data['User_code'],StateReview__step = data['step_id'])
            if data['step_id'] == '6':
                userprofile = UserProfile.objects.get(user__id = StateReview_User_.user.id)
                if data['status'] == 'true':
                    userprofile.paymet_status = True
                   
                else:
                    userprofile.paymet_status = False
                userprofile.save()
            if data['status'] == 'true':
                print(1)
                StateReview_User_.Review_status = True
            else:
                StateReview_User_.Review_status = False
            StateReview_User_.save()
            print(StateReview_User_)
            response = {'message': 'Data received successfully', 'received_data': data}
            return JsonResponse(response)
        if data['action'] == '2':
            StateReview_User_his = Review_User_History.objects.get(Review_User_History_id = data['reviewUserHistoryId'])
            if data['value'] == 'true':
                StateReview_User_his.status_review = True
            else:
                StateReview_User_his.status_review = False
            StateReview_User_his.save()
            response = {'message': 'Data received successfully', 'received_data': data}
            return JsonResponse(response)
       

    if request.method == 'GET':
        action_param = request.GET.get("action")
        match action_param:
                case '1':
                    print(request.GET)
                    user_id = request.GET.get("id")
                    userprofile = UserProfile.objects.filter(user_id=user_id).values()
                    user = User.objects.filter(id=user_id).values()
                    abstact = StateReview_User.objects.filter(user_id=user_id).values()
                    user_history = Review_User_History.objects.filter(StateReview_User__user_id=user_id).values()
                    res = dict()
                    res['info'] = list(user)
                    res['detial'] = list(userprofile)
                    res['abstact']= list(abstact)
                    res['sumbition']= list(user_history)
                    return JsonResponse(res, safe=False)
                case _:
                    if request.user.is_authenticated:
                        all_user = User.objects.filter(is_staff=False,groups__id=1)
                        qty_total = all_user.count()
                        paymet = all_user.filter(userprofile__paymet_status = True).count()
                        abssubmit = StateReview_User.objects.filter(Review_status = True,StateReview__step = 1).count()
                        fullsubmit = StateReview_User.objects.filter(Review_status = True,StateReview__step = 2).count()
                        step_review_list = StateReview_User.objects.all()
                        list_user_ids = all_user
                        res = {}

                        for user_data in list_user_ids:
                            list_review_user = step_review_list.filter(user_id=user_data.id)
                            res[user_data.id] = {
                                'review': list(list_review_user),
                                'userinfo': user_data,
                            }
                        print(res)
                        return render(request, "Client/StaffSection/Applicant-List.html",{'user_reviews': res,'qty_regular':qty_total,'qty_ab':abssubmit,'qty_full':fullsubmit,'Payment_qty':paymet})
    else:
        return redirect('signin') 
def VisitorList(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('signin')
    return render(request, "Client/StaffSection/Visitor-List.html")
def RegisterType(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('signin')
    return render(request, "Client/ApplicantSection/Register-Type.html")

def Register(request):
    if request.method == 'POST':
        print(request.POST)

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
       
        username = email
        password = generate_password()
        user = User.objects.filter(username=username)
        group = Group.objects.get(id = request.POST.get('User_type'))
        title = request.POST.get('title')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        fax = request.POST.get('fax')
        research_field = request.POST.get('research_field')
        institution = request.POST.get('institution')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        state_province = request.POST.get('state_province')
        zip_postal_code = request.POST.get('zip_postal_code')
        print(group)
        if user.exists():
        
            return JsonResponse({"res":'Username already taken!',"data":'not ok'},status=HTTPStatus.OK)
         
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
         
        # Set the user's password and save the user object
        user.set_password(password)
        user.groups.add(group)
        user.save()
        code = generate_random_code()
        #create userprofile
        user_profile = UserProfile(
            user=user,
            codeno= code,
            User_type=group,
            title=title,
            phone=phone,
            fax=fax,
            research_field=research_field,
            institution=institution,
            address=address,
            city=city,
            country=country,
            state_province=state_province,
            zip_postal_code=zip_postal_code
        )
        user_profile.save()
        all_review_step = StateReview.objects.all()
        for i in all_review_step:
            new_stateReview_user = StateReview_User(
                user = user,
                StateReview = i
            )
            new_stateReview_user.save()
        ############## SEND MAIL USERPASSWORD ######################
        thread = threading.Thread(target=sendmail, args=(first_name+' '+last_name,email,username,password,code))
        thread.start()
        return JsonResponse({"data":'ok',"res":'save complete'},status=HTTPStatus.OK)
    else: 
        Group_llist  = Group.objects.all()
        return render(request, "Client/Online-Register.html",{'Group_llist':Group_llist})


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass']
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            print(fname)
            print("here!!!!!!!!!!!!!!!!!!!!!!")
            if user.is_staff:
                print("here!!!!!!!!!!!!!!!!!!!!!!")
                return redirect('Staff-Dashboard')
            else:
                return redirect('Applicant-Dashboard')
        else:
            messages.error(request, "Username Password invalid!")
            return redirect('signin')
    if request.user.is_authenticated:
        if request.user.is_staff:
            print("here!!!!!!!!!!!!!!!!!!!!!!")
            return redirect('Staff-Dashboard')
        else:
            return redirect('Applicant-Dashboard')
    else:
        return render(request, "Client/Login.html")
def Forgot(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            account = User.objects.get(username=email)
            new_password = generate_password()
            account.set_password(new_password)
            account.save()
            
            # Start a new thread to send the reset email
            thread = threading.Thread(target=send_reset_email, args=(email, new_password))
            thread.start()

            messages.success(request, "A new password has been sent to your email.")
        except User.DoesNotExist:
            messages.error(request, "Username not found!")
        
        return redirect('Forgot')

    else:
        return render(request, "Client/Forgot.html")
def home(request):
    if request.user.is_authenticated:
        print("login true")
        pass
    else:
        return redirect('Login')

    return render(request, "Client/ApplicantSection/Applicant-Dashboard.html")
def signout(request):
    print(request)
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('signin')