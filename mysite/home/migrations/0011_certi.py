# Generated by Django 4.2.1 on 2023-08-02 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_internship_contact_contact_adnum_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='certi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('nptel', 'nptel'), ('workshops', 'workshops'), ('seminar', 'seminar'), ('sports', 'sports')], max_length=100, null=True)),
                ('credits', models.PositiveBigIntegerField(null=True)),
                ('score', models.PositiveBigIntegerField(null=True)),
                ('level', models.CharField(choices=[('easy', 'easy'), ('moderate', 'moderate'), ('hard', 'hard')], max_length=100, null=True)),
            ],
        ),
    ]