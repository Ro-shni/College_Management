# Generated by Django 4.2.1 on 2023-05-23 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_certification_contact_internship_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='year',
            field=models.CharField(default='exit', max_length=6),
            preserve_default=False,
        ),
    ]
