from django.conf.urls import include, url
from django.contrib import admin
from rest.views import *

urlpatterns = [
    url(r'^citations$', CitationList.as_view()),
    url(r'^citations/(?P<term1>.+),(?P<term2>.+)$', CitationFuzzy.as_view()),
    url(r'^violations$', ViolationList.as_view()),
    url(r'^violations/(?P<citation_number>.+)$', ViolationByCitationNumber.as_view()),
    url(r'^citationviolations$', CitationViolationList.as_view()),
    url(r'^citationviolations/(?P<lat>.+),(?P<lng>.+)$', CitationByLocation.as_view()),
    url(r'^courts/(?P<address>.+)$', CourtByAddress.as_view()),
    url(r'^courts/(?P<lat>.+),(?P<lng>.+)$', CourtByLocation.as_view()),
    url(r'^warrants/(?P<case_number>.+)$', WarrantsByCaseNumber.as_view()),
    url(r'^message$', received_message),
    url(r'^admin/', include(admin.site.urls)),
]
