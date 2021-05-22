"""ch05www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import re_path

from mysite.views import about, homepage, listing, post


urlpatterns = [
    re_path(r'^$', homepage),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^about/(?P<author_no>[0|1|2|3])/$', about),
    re_path(r'^list/(?P<list_date>\d{4}/\d{1,2}/\d{1,2})$', listing),
    re_path(r'^post/(\d{4})/(\d{1,2})/(\d{1,2})/(\d{1,3})$', post),
]
