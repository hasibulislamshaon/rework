# Generated by Django 5.0.2 on 2024-02-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mydashboard',
            name='location',
            field=models.CharField(default='', max_length=250),
        ),
    ]
