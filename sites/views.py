from django.shortcuts import render, redirect
from .models import Atividade
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms

def home(request):
    return render(request, "sites/index.html")

def index(request):
    return render(request, 'index.html')

@login_required
def atividades(request):
    atividades = Atividade.objects.all()  # Buscar todas as atividades
    return render(request, 'atividades.html', {'atividades': atividades})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():

            return redirect("home")  # redireciona para a home após o login
    else:
        form = AuthenticationForm()  # Se for GET, cria um formulário vazio

    return render(request, "login.html", {"form": form})  # Retorna o template com o formulário

# View de registro
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo usuário no banco de dados
            return redirect("login")  # Redireciona para a página de login após o registro
    else:
        form = RegisterForm()  # Se for GET, cria um formulário vazio

    return render(request, "login.html", {"form": form})  # Retorna o template com o formulário

# Formulário de registro
class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Senha", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])  # Criptografa a senha antes de salvar
        if commit:
            user.save()
        return user