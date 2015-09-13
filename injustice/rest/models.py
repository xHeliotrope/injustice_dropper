from __future__ import unicode_literals
from django.db import models

class Citations(models.Model):
    id = models.IntegerField()
    citation_number = models.BigIntegerField(primary_key=True)
    citation_date = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    defendant_address = models.CharField(max_length=200, blank=True, null=True)
    defendant_city = models.CharField(max_length=200, blank=True, null=True)
    defendant_state = models.CharField(max_length=2, blank=True, null=True)
    drivers_license_number = models.CharField(max_length=200, blank=True, null=True)
    court_date = models.DateField(blank=True, null=True)
    court_location = models.CharField(max_length=200, blank=True, null=True)
    court_address = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citations'

class Violations(models.Model):
    id = models.IntegerField(primary_key=True)
    citation_number = models.ForeignKey(Citations, db_column='citation_number', related_name='violations', blank=True, null=True)
    violation_number = models.CharField(max_length=200, blank=True, null=True)
    violation_description = models.CharField(max_length=500, blank=True, null=True)
    warrant_status = models.NullBooleanField()
    warrant_number = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    status_date = models.DateField(blank=True, null=True)
    fine_amount = models.TextField(blank=True, null=True)  # This field type is a guess.
    court_cost = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'violations'

class Warrants(models.Model):
    defendant = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    case_number = models.CharField(max_length=20, blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'warrants'
