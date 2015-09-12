from django.conf.urls import include, url
from django.contrib import admin
from rest.views import *

urlpatterns = [
    url(r'^citations$', CitationList.as_view()),
    url(r'^violations$', ViolationList.as_view()),
    url(r'^admin/', include(admin.site.urls)),
]
