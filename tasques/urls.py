from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('incidencies/', include('incidencies.urls')),  # Rutes de l'app 'incidencies'
    path('', RedirectView.as_view(pattern_name='incidencies:llista_incidencies', permanent=False)),
]
