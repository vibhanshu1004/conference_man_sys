# from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import EmailForm
from django.core.mail import send_mail

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient_email = form.cleaned_data['recipient_email']
            send_mail(
                'Subject here',
                'Here is the message.',
                'sender@example.com',
                [recipient_email],
                fail_silently=False,
            )
            return redirect('success')
    else:
        form = EmailForm()
    return render(request, 'email_sender/send_email.html', {'form': form})

def success(request):
    return render(request, 'email_sender/success.html')
