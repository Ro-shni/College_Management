# Generated by Django 4.2.1 on 2023-05-23 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_details_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='fname',
            new_name='fullname',
        ),
    ]