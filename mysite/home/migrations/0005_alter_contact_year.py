# Generated by Django 4.2.1 on 2023-05-23 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_fname_contact_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
