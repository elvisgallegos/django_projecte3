from django.db import models

class Treballador(models.Model):
    nom = models.CharField(max_length=100)
    pot_assignar = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class IncidentStatus(models.TextChoices):
    OPEN = 'open', 'Oberta'
    ASSIGNED = 'assigned', 'Assignada'
    IN_PROGRESS = 'in_progress', 'En progrés'
    RESOLVED = 'resolved', 'Resolta'
    CLOSED = 'closed', 'Tancada'

class Incident(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(Treballador, on_delete=models.CASCADE, related_name='incidencies_creades')
    assigned_to = models.ForeignKey(Treballador, on_delete=models.SET_NULL, null=True, blank=True, related_name='incidencies_assignades')
    status = models.CharField(max_length=20, choices=IncidentStatus.choices, default=IncidentStatus.OPEN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
