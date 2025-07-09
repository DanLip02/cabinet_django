"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from dashboard.views import dashboard_view, services_view, services_status_view

from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", RedirectView.as_view(url="/login/", permanent=False)),  # редирект с корня на логин
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path('logout/', auth_views.LogoutView.as_view(next_page='login', redirect_field_name=None), name='logout'),
    path('services/', services_view, name='services'),  # Новый маршрут
    path('monitoring/', services_status_view, name='monitoring'),
    path('chat/', include('internal_chat.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)