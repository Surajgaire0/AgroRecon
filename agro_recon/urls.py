"""agro_recon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/recommend/', include('recommender.urls')),
    path('api/users/', include('users.urls')),
    path('api/docs/', include_docs_urls(title='AgroRecon'), name='docs'),
    path('api/', include('forum.urls')),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.api_root, name='api_root'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
