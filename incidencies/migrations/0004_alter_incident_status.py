# Generated by Django 5.2.1 on 2025-06-11 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidencies', '0003_remove_treballador_pot_resoldre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='status',
            field=models.CharField(choices=[('open', 'Oberta'), ('assigned', 'Assignada'), ('in_progress', 'En progrés'), ('resolved', 'Resolta'), ('closed', 'Tancada')], default='open', max_length=20),
        ),
    ]
