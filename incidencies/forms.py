from django import forms
from .models import Incident, Treballador

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'description', 'assigned_to', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Només mostrar treballadors que poden resoldre tasques
        self.fields['assigned_to'].queryset = Treballador.objects.filter(pot_resoldre=True)
