from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from django.contrib import messages
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from account.utils import send_activation_email
from account.models import User

# Create your views here.
def home(request):
    return render(request, 'account/home.html')

def login_view(request):
    if request.method == "POST":
        return redirect('customer_dashboard')
    return render(request, 'account/login.html')

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.is_active = False
            user.save()
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token})
            activation_url = f'{settings.SITE_DOMAIN}{activation_link}'
            send_activation_email(user.email, activation_url)
            messages.success(
                request,
                'Registration successful! Please check your email to activate your account.',
            )
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})

def activate_account(requst, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if user.is_active:
            messages.warning(
                requst, "This account has already been activated.")
            return redirect('login')
        
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(
                requst, "Your account has been activated Successfully!")
            return redirect('login')
        else:
            messages.error(
                requst, "The activation link is invalid or has expired.")
            return redirect('login')
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(
            requst, "Invalid activation link.")
        return redirect('login')

def password_reset_view(request):
    return render(request, 'account/password_reset.html')

def password_reset_confirm_view(request):
    return render(request, 'account/password_reset_confirm.html')
