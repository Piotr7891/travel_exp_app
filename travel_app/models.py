from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


COUNTRY = (
    ("Poland", "Poland"),
    ("Germany", "Germany"),
    ("France", "France"),
    ("Spain", "Spain"),
    ("Italy", "Italy"),
    ("Czech Republic", "Czech Republic"),
    ("Slovakia", "Slovakia"),
    ("Austria", "Austria"),
    ("Hungary", "Hungary")
)

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class BusinessTrip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    destination = models.CharField(max_length=255, choices=COUNTRY)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name}'s Business Trip to {self.destination}"

class Expense(models.Model):
    business_trip = models.ForeignKey(BusinessTrip, on_delete=models.CASCADE, related_name='expenses')
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.description} - ${self.amount}"