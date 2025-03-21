from django.contrib import admin
from django.urls import path
from dashboard import views
from .report import download_report

urlpatterns = [
    path("",views.index, name="home"),
    path("invoice/",views.invoice, name="invoice"),
    path("download-report/", download_report, name="download_report"),
]

