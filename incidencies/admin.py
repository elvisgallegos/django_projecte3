from django.contrib import admin
from django import forms
from .models import Incident, Treballador

class IncidentAdminForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].queryset = Treballador.objects.filter(pot_assignar=True)

class IncidentAdmin(admin.ModelAdmin):
    form = IncidentAdminForm
    list_display = ['title', 'created_by', 'assigned_to', 'status', 'created_at']
    list_filter = ['status', 'created_by', 'assigned_to']

admin.site.register(Incident, IncidentAdmin)
admin.site.register(Treballador)
