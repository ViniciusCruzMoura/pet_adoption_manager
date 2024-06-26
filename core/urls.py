"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # DJANGO ADMIN
    path('admin/', admin.site.urls),
    # HEALTH CHECK
    path('', include('health_check.urls')),
    # API
    path('', include('apps.management_system.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Internacionalização
from django.conf.urls.i18n import i18n_patterns
urlpatterns += [
    path("i18n/", include("django.conf.urls.i18n")),
]
#urlpatterns += i18n_patterns(path("admin/", admin.site.urls))

#Namespace
#urlpatterns = [path('petadopt/', include(urlpatterns))]

admin.site.site_header = 'Sistema de Gestão de Adoção de Animais'
admin.site.index_title = 'Atendimento' 
admin.site.site_title = 'Adoção de Animais'