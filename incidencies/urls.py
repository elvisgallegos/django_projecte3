from django.urls import path
from . import views

app_name = 'incidencies'

urlpatterns = [
    path('', views.llista_incidencies, name='llista_incidencies'),
]
