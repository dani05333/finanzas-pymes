
from django.shortcuts import render, redirect
from finanzasApp.models import Proveedor
from .forms import formularioProveedor
from django.http import HttpRequest
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import TemplateView



class PrincipalView(TemplateView):
    template_name = 'principal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proveedores'] = Proveedor.objects.all()
        context['proveedor_form'] = formularioProveedor()
        return context



def renderInicio(request):
    proveedores = Proveedor.objects.all()    
    datos = {"proveedores" : proveedores}
    return render(request, 'inicio.html', datos)

def crearProveedor(request):
    if request.method == 'POST':
        print(request.POST)
        proveedor_form = formularioProveedor(request.POST)
        if proveedor_form.is_valid():
            proveedor_form.save()
            return redirect('principal')
    else:
        proveedor_form = formularioProveedor() 

    return render(request, 'crear_proveedor.html', {'proveedor_form': proveedor_form})

def editarProveedor(request,id):
    proveedor = Proveedor.objects.get(id = id)
    if request.method == "GET":
        proveedor_form = formularioProveedor(instance = proveedor)
    else:
        proveedor_form = formularioProveedor(request.POST, instance = proveedor)
        if proveedor_form.is_valid():
            proveedor_form.save()
        return redirect('principal')
    return render(request,'crear_proveedor.html',{'proveedor_form':proveedor_form})

def eliminarProveedor(request,id):
    proveedor = Proveedor.objects.get(id = id)
    proveedor.delete()
    return redirect('principal')

    

    
    
#def userRegisterForm(request):
#   form = forms.UserRegisterForm() --- recuerda importar la pagina de form

# Desarrollo
#   if request.method == 'POST':
#       form = forms.UserRegisterForm(request.POST)
#       if form.is_valid():
#           print("Formulario Valido")
#           print("Rut:",form.cleaned_data['rut']) --- clean data limpia todo tipo de informacion, convierte num en string
#           print("Nombre:",form.cleaned_data['nombre']) --- clean data limpia todo tipo de informacion, convierte num en string
#           print("Apellido:",form.cleaned_data['apellido']) --- clean data limpia todo tipo de informacion, convierte num en string
#           print("Email:",form.cleaned_data['email']) --- clean data limpia todo tipo de informacion, convierte num en string

#   rut = form.cleaned_data['rut']
#   nom = form.cleaned_data['nombre']
#   ape = form.cleaned_data['apellido']
#   email = form.cleaned_data['correo']
#   admin = Persona(rut=rut,nombre=nom,apellido=ape,email=email)
#   admin.save()

#   data = {'form' : form}
#   return render(request, 'userRegister.html', data)