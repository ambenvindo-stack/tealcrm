# Generated by Django 4.1.7 on 2023-03-22 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='prority',
            new_name='priority',
        ),
    ]
