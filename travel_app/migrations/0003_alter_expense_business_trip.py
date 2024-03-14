# Generated by Django 5.0.2 on 2024-03-14 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0002_alter_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='business_trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='travel_app.businesstrip'),
        ),
    ]
