# Generated by Django 4.0.4 on 2022-07-07 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_passenger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='flight',
        ),
        migrations.AddField(
            model_name='passenger',
            name='flight',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights.flight'),
        ),
    ]
