# Generated by Django 4.2.1 on 2023-05-23 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_contact_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='year',
        ),
        migrations.AddField(
            model_name='contact',
            name='stdyear',
            field=models.IntegerField(null=True),
        ),
    ]
