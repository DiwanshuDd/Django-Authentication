"""
URL configuration for authentication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from . import views
# from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),  # No need to duplicate index path
    # path("home/", views.home, name="home"),
    path("about/",views.about, name="about"),
    path("features/",views.features, name="features"),
    path("contact/",views.contact, name="contact"),
    path('webcam/', views.webcam_view, name='webcam'),
    
    # path('plataforma/', TemplateView.as_view(template_name='plataforma.html'), name='plataforma'),
    # path('plataforma/stream', TemplateView.as_view(template_name='stream.html'), name='stream'),
    path('', include('mainapp.urls')),
     
     
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


