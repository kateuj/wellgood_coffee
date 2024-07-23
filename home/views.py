from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def custom_404(request, exception=None):

    return render(request, '404.html', status=404)

def contact(request):

    return render(request, 'home/contact.html')


def contact_send(request):
    email_contact = settings.EMAIL_CONTACT

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            f'{name} has got in touch',
            message,
            email,
            [email_contact],
            fail_silently=False,
        )
        return redirect('contact_success')
    else:
        messages.error(
            request,
            "Please check your form is valid and try again."
        )

    return render(request, 'home/contact.html')


def contact_success(request):

    return render(request, 'home/contact_success.html')
