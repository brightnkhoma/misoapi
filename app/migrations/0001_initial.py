# Generated by Django 5.1.2 on 2024-10-19 09:16

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catchment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=django.utils.timezone.now, max_length=100, unique=True)),
                ('project_code', models.CharField(default='None', max_length=50)),
                ('Phase_Name', models.CharField(default='undefined', max_length=30)),
                ('target_HHs', models.CharField(default='undefined', max_length=30)),
                ('enrolled_HHs', models.CharField(default='undefined', max_length=30)),
                ('project_id', models.CharField(default='undefined', max_length=30)),
                ('catchment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='app.catchment')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('first_name', models.CharField(default='undefined', max_length=30)),
                ('last_name', models.CharField(default='undefined', max_length=30)),
                ('full_name', models.CharField(max_length=60)),
                ('form_number', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('phoneNumber', models.CharField(default='undefined', max_length=30)),
                ('national_id', models.CharField(default='undefined', max_length=30)),
                ('gender', models.CharField(default='undefined', max_length=30)),
                ('district_name', models.CharField(default='undefined', max_length=30)),
                ('traditional_authority_name', models.CharField(default='undefined', max_length=30)),
                ('group_village_head_name', models.CharField(default='undefined', max_length=30)),
                ('village_name', models.CharField(default='undefined', max_length=30)),
                ('household_id', models.CharField(default='undefined', max_length=30)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='app.project')),
            ],
        ),
    ]
