from django.urls import path
from cve import views

urlpatterns = [
    path('cves/', views.find_cves, name='find_cves'),
]
