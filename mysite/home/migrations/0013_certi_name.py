# Generated by Django 4.2.1 on 2023-08-02 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_certi_adnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='certi',
            name='name',
            field=models.CharField(max_length=75, null=True),
        ),
    ]