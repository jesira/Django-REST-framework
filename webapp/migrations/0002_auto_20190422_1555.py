# Generated by Django 2.1 on 2019-04-22 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='employees',
            new_name='Employee',
        ),
    ]