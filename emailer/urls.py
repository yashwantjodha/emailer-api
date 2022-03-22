from django.urls import path
from . import views

## URL PATTERNS for the app
urlpatterns = [
    path("", views.index, name="index"),
    path("api", views.email_api, name="api")
]