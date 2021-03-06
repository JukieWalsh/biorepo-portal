"""brp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from .views import index, changelog
from accounts.views import eula, throttled_login
from django.contrib.auth.views import logout_then_login
urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    # Third-party
    url(r'session_security/', include('session_security.urls')),
    # registration, account management urls
    url(r'^accounts/', include('accounts.urls')),
    url(r'^dataentry/', include('dataentry.urls')),
    url(r'^eula/$', eula, name='eula'),
    url(r'^login/$', throttled_login, name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^changelog/$', changelog, name='changelog'),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^brp_admin/', include('brp_admin.urls'), name='brp_admin'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
