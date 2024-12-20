# Generated by Django 5.1.2 on 2024-10-26 19:13

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
            name='Forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formNumber', models.CharField(max_length=30, unique=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=django.utils.timezone.now, max_length=100, unique=True)),
                ('project_code', models.CharField(blank=True, default='None', max_length=50, null=True)),
                ('Phase_Name', models.CharField(blank=True, default='undefined', max_length=30, null=True)),
                ('target_HHs', models.CharField(blank=True, default='undefined', max_length=30, null=True)),
                ('enrolled_HHs', models.CharField(blank=True, default='undefined', max_length=30, null=True)),
                ('project_id', models.CharField(blank=True, default='undefined', max_length=30, null=True)),
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
                ('phoneNumber', models.CharField(blank=True, default='undefined', max_length=30, null=True)),
                ('national_id', models.CharField(blank=True, default='undefined', max_length=30, null=True)),
                ('gender', models.CharField(blank=True, default='undefined', max_length=30, null=True)),
                ('district_name', models.CharField(blank=True, default='undefined', max_length=30, null=True)),
                ('traditional_authority_name', models.CharField(blank=True, default='undefined', max_length=30, null=True)),
                ('group_village_head_name', models.CharField(blank=True, default='undefined', max_length=30, null=True)),
                ('village_name', models.CharField(blank=True, default='undefined', max_length=30, null=True)),
                ('household_id', models.CharField(blank=True, default='undefined', max_length=30, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='app.project')),
            ],
        ),
    ]
