# Generated by Django 5.0.2 on 2024-03-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
