# Generated by Django 5.0.2 on 2024-02-14 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_mydashboard_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydashboard',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
