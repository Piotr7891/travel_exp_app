# Generated by Django 5.0.2 on 2024-03-19 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0004_expense_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='expense_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]