from django.contrib import admin
from django.urls import path

from webapp.views import numbers_calculation

urlpatterns = [
    path('', numbers_calculation)
]

