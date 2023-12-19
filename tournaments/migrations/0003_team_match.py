# Generated by Django 5.0 on 2023-12-19 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_phase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('flag', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.phase')),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='tournaments.team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='tournaments.team')),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
    ]