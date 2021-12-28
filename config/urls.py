"""config URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.settings import MEDIA_ROOT

from dj_rest_auth.views import PasswordResetConfirmView


app_name = 'products'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),   
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/password/reset/confirm/<uid64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),    #‌ overwrite this url for resolve a bug in dj-rest-auth package!
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)