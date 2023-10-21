"""
URL configuration for Samarth_Restaurant project.

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
from django.urls import path,include

# added code 
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Samarth Restaurant"
admin.site.site_title = " Samarth Admin Portal"
admin.site.index_title = "Welcome to Samarth Restaurant Web Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Restaurant_App.urls')),
    path('favicon.png/', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.png')))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
