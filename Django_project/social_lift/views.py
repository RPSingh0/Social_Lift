from django.shortcuts import render, HttpResponse, redirect
from social_lift.facebook_bot import create_post
from social_lift.instagram_bot import insta_post
from social_lift.email_s import send_email
from social_lift.text_message import send_sms
from social_lift.models import Post_data, Wisher
from django.contrib import messages
import os
from time import sleep
import shutil
# Create your views here.


def HomePage(request):
    return render(request, 'index.html')


def WishingExpress(request):
    if request.method == "POST":
        data = Wisher()
        data.email = request.POST.get('email')
        data.password = request.POST.get('password')
        data.remail = request.POST.get('remail')
        data.message = request.POST.get('message')
        data.number = request.POST.get('number')
        data.save()

        for i in [data.email, data.password, data.remail, data.message, data.number]:
            print(i)

        if data.email.lower() == "none" and data.password.lower() == "none":
            send_email(receiver=data.remail, message=data.message,
                       Email=None, Password=None)
        else:
            send_email(receiver=data.remail, message=data.message,
                       Email=data.email, Password=data.password)

        send_sms(message=data.message, number=data.number)

        return redirect('/index')
    return render(request, 'wishing_express.html')


def MultiPost(request):
    if request.method == "POST":
        shutil.rmtree("./media", ignore_errors=True, onerror=None)
        data = Post_data()
        data.email = request.POST.get('email')
        data.password = request.POST.get('password')
        data.caption = request.POST.get('caption')

        if len(request.FILES) != 0:
            data.image = request.FILES['image']

        data.save()

        # print(os.getcwd())

        def f_p():
            return os.listdir(path=r"media")[0]

        # print(f_p())
        # print(os.getcwd()+"\media\\"+f_p())

        f = create_post(email_number=data.email, password=data.password,
                        caption=data.caption, file_path=os.getcwd()+"\media\\"+f_p())

        print(f)
        i = insta_post(caption=data.caption, media=os.getcwd() + "\media\\" +
                       f_p(), size=(1080, 1080), email=data.email, password=data.password)

        print(i)
        messages.success(request, "Posting, check after a min")
        sleep(10)
        return redirect('/index')
    return render(request, 'multipost.html')


def Info(request):
    return render(request, "info.html")
