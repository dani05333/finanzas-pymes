from django import  forms
from .models import Proveedor

class formularioProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        

#class UserRegisterForm(forms.Form):
#   rut = forms.CharField(required=True)   --- forms es el nombre del archivo, required es porque es obligatorio
#   nombre = forms.CharField()
#   apellido = forms.CharField()
#   correo = forms.CharField(widget=forms.EmailInput()) -- o PasswordImput()
#   id = forms.IntegerField

#Esto es para bootstrap

    #rut.widget.attrs['class'] = 'form-control'
    #nombre.widget.attrs['class'] = 'form-control'
    #apellido.widget.attrs['class'] = 'form-control'
    #email.widget.attrs['class'] = 'form-control'