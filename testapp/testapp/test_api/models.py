# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tests(models.Model):
    # Field renamed to remove unsuitable characters.
    device_type = models.TextField(db_column='device type', blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Tests"
        db_table = 'tests'
