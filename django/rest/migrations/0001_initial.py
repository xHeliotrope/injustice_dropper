# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citations',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('citation_number', models.BigIntegerField(blank=True, null=True)),
                ('citation_date', models.DateField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=200, null=True, blank=True)),
                ('last_name', models.CharField(max_length=200, null=True, blank=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('defendant_address', models.CharField(max_length=200, null=True, blank=True)),
                ('defendant_city', models.CharField(max_length=200, null=True, blank=True)),
                ('defendant_state', models.CharField(max_length=2, null=True, blank=True)),
                ('drivers_license_number', models.CharField(max_length=200, null=True, blank=True)),
                ('court_date', models.DateField(blank=True, null=True)),
                ('court_location', models.CharField(max_length=200, null=True, blank=True)),
                ('court_address', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'citations',
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'django_content_type',
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(serialize=False, primary_key=True, max_length=40)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_session',
            },
        ),
        migrations.CreateModel(
            name='Violations',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('citation_number', models.BigIntegerField(blank=True, null=True)),
                ('violation_number', models.CharField(max_length=200, null=True, blank=True)),
                ('violation_description', models.CharField(max_length=500, null=True, blank=True)),
                ('warrant_status', models.NullBooleanField()),
                ('warrant_number', models.CharField(max_length=200, null=True, blank=True)),
                ('status', models.CharField(max_length=200, null=True, blank=True)),
                ('status_date', models.DateField(blank=True, null=True)),
                ('fine_amount', models.TextField(blank=True, null=True)),
                ('court_cost', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'violations',
            },
        ),
    ]
