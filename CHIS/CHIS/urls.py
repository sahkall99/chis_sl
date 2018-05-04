"""CHIS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from CHIS import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='home'),                  # url for routing to the home/index page
    url(r'^about/$', views.AboutView.as_view(), name='about'),          # url for routing to the about page
    url(r'^contact/$', views.contact_view, name='contact_us'),          # url for routing to the contact us page
    url(r'^success/$', views.SuccessView.as_view(), name='success'),    # url for routing to the contact us success page
    url(r'^chis_sl/', include('chis_sl.urls', namespace='chis_sl')),    # including chis_sl namespace
    url(r'chis_sl/', include('django.contrib.auth.urls')),              # including urls from django built in package
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)       # for serving images uploaded by user
