from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, MagicLinkForm
from .models import MagicToken
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
import uuid

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('portefolio_app:home')
    else:
        form = AuthenticationForm()
    
    magic_form = MagicLinkForm()
    return render(request, 'accounts/login.html', {'form': form, 'magic_form': magic_form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('portefolio_app:home')

def magic_link_request(request):
    if request.method == 'POST':
        form = MagicLinkForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                user = User.objects.get(email=email)
                token = MagicToken.objects.create(user=user)
                
                # Create the link
                link = request.build_absolute_uri(
                    reverse('accounts:magic_login', args=[token.token])
                )
                
                # Send email (will show in console)
                send_mail(
                    'Seu Magic Link para Portefólio',
                    f'Clique no link para entrar: {link}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                messages.info(request, 'Um link mágico foi enviado para o seu email.')
            except User.DoesNotExist:
                # Security: don't reveal if user exists
                messages.info(request, 'Se o email existir, um link foi enviado.')
            
            return redirect('accounts:login')
    return redirect('accounts:login')

def magic_login(request, token):
    try:
        magic_token = MagicToken.objects.get(token=token)
        if magic_token.is_valid():
            login(request, magic_token.user)
            magic_token.used = True
            magic_token.save()
            return redirect('portefolio_app:home')
        else:
            messages.error(request, 'Link expirado ou já utilizado.')
    except MagicToken.DoesNotExist:
        messages.error(request, 'Link inválido.')
    
    return redirect('accounts:login')
