# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warrants',
            fields=[
                ('defendant', models.CharField(blank=True, null=True, max_length=200)),
                ('zip_code', models.CharField(blank=True, null=True, max_length=5)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('case_number', models.CharField(blank=True, null=True, max_length=20)),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'warrants',
                'managed': False,
            },
        ),
    ]
