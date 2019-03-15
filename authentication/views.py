from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditUserForm, ChangePasswordForm

# Create your views here.
def home(request):
    return render(request, 'authentication/home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('¡Hola de nuevo {}!'.format(username)))
            return redirect('home')
        else:
            messages.success(request, ('Tu usuario o contraseña son incorrectos.'))
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('Cerraste tu sesión, ¡hasta pronto!'))
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('¡Ya estás en corrrector, {}!'.format(username)))
            return redirect('home')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)

def edit_profile(request):
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('Cambios guardados'))
            return redirect('home')
    else:
        form = EditUserForm(instance=request.user)

    context = {'form': form}
    return render(request, 'authentication/edit_profile.html', context)

def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('Cambios guardados'))
            return redirect('home')
    else:
        form = ChangePasswordForm(user=request.user)

    context = {'form': form}
    return render(request, 'authentication/change_password.html', context)
