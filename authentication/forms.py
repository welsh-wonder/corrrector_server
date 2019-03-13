from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ejemplo@dominio.com'}))
    first_name = forms.CharField(max_length=100, label="Nombre", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Joanne'}))
    last_name = forms.CharField(max_length=100, label="Apellido", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Rowling'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = "form-control"
        self.fields['username'].widget.attrs['placeholder'] = "joanne_rowling"
        self.fields['username'].label = "Nombre de usuario"
        self.fields['username'].help_text = '<small class="form-text text-muted">Requerido. 150 caracteres o menos. Sólo acepta letras, números y @ . + - _ .</small>'

        self.fields['password1'].widget.attrs['class'] = "form-control"
        self.fields['password1'].widget.attrs['placeholder'] = "KWQbs4{oXzeH[9EW"
        self.fields['password1'].label = "Contraseña"
        self.fields['password1'].help_text = '<small class="form-text text-muted"><ul><li>La contraseña no debe ser similar a tu otra información personal.</li><li>Tu contraseña debe contener al menos 8 caracteres.</li><li>Tu contraseña no debe ser fácil de adivinar.</li><li>Tu contraseña no puede ser completamente numérica.</li></ul></small>'

        self.fields['password2'].widget.attrs['class'] = "form-control"
        self.fields['password2'].widget.attrs['placeholder'] = "KWQbs4{oXzeH[9EW"
        self.fields['password2'].label = "Confirma tu contraseña"
        self.fields['password2'].help_text = ""
