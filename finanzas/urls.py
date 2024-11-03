"""
URL configuration for finanzas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from finanzasApp import views
from finanzasApp.views import PrincipalView


#from finanzasApp.views import userRegisterForm


urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'),name='login'), 
    path('logout/', LogoutView.as_view(),name='logout'), 
    path('admin/', admin.site.urls),
    path('inicio/', views.renderInicio), 
    path('principal/',PrincipalView.as_view(), name='principal'),
    path('crear_proveedor/',views.crearProveedor, name='crear_proveedor'),
    path('editar_proveedor/<int:id>',views.editarProveedor, name='editar_proveedor'),
    path('eliminar_proveedor/<int:id>',views.eliminarProveedor, name='eliminar_proveedor'),
    #path('register/',views.userRegisterForm)
   
]
