"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from sitepi.views import home, form, create, resultados, visualizar, editar, atualizar, apagar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('visualizar/<int:pk>/', visualizar, name='visualizar'),
    path('editar/<int:pk>/', editar, name='editar'),
    path('atualizar/<int:pk>/', atualizar, name='atualizar'),
    path('apagar/<int:pk>/', apagar, name='apagar'),
    path('resultados/', resultados, name='resultados'),
]