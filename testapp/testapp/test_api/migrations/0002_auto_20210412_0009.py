# Generated by Django 3.1.4 on 2021-04-11 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tests',
            options={'managed': False, 'verbose_name': 'Test', 'verbose_name_plural': 'Tests'},
        ),
    ]
