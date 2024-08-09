# Generated by Django 5.0.3 on 2024-08-09 07:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunities',
            fields=[
                ('opportunity_id', models.AutoField(primary_key=True, serialize=False)),
                ('statement', models.TextField(default='')),
                ('plannedActions', models.TextField(default='')),
                ('kpi', models.TextField(default='')),
                ('keyPersons', models.TextField(default='')),
                ('targetOutput', models.TextField(default='')),
                ('budget', models.FloatField()),
                ('startDate', models.DateField(default=django.utils.timezone.now)),
                ('endDate', models.DateField(default=django.utils.timezone.now)),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.departmentheads')),
            ],
        ),
    ]