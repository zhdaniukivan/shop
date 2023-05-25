"""
URL configuration for Pizzashop project.

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
from django.urls import path
from pizzashopapp import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pizzashopapp/sign-in', auth_views.LoginView.as_view(template_name='pizzashopapp/sign_in.html' ),
         name='pizzashop-sign-in'),
    path('pizzashopapp/sign-in', auth_views.LogoutView.as_view(next_page='/' ),
         name='pizzashop-sign-out'),
    path('pizzashopapp', views.pizzashopapp_home, name='pizzashopapp-home'),
    path('pizzashopapp/sign-up', views.pizzashopapp_sign_up, name='pizzashopapp-sign-up'),
    path('home', views.pizzashopapp_all, name='pizzashopapp-all'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
