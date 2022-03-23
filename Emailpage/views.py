from django.shortcuts import render
from Emailpage.forms import emailform
from django.core.mail import send_mail
from email.mime.image import MIMEImage
from django.contrib.staticfiles import finders

def emailsendmail(request):
    if request.method == 'GET':
        form = emailform()
    else:
        form = emailform(request.POST)
        if form.is_valid():
            frommail = form.cleaned_data['from_mail']
            username = form.cleaned_data['username']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                subject,
                message,
                frommail,
                ['priyarohitsharma20@gmail.com',frommail],
            )#to Email

            return render(request, 'confirm.html', {
                                            'username': username,
                                            'message': message})

    return render(request,'Emailpage.html',{'form':form})
