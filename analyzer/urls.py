from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainView.as_view(), name="index"),
    path("download/", views.DownloadView.as_view(), name="download"),
]
