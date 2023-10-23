from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('hello/', views.home),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()