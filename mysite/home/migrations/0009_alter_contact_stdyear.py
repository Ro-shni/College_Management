# Generated by Django 4.2.1 on 2023-05-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_contact_year_contact_stdyear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='stdyear',
            field=models.CharField(default='exit', max_length=6),
            preserve_default=False,
        ),
    ]
