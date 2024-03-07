from django.db import models


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
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class BusinessTrip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    destination = models.CharField(max_length=255, choices=COUNTRY)
    start_date = models.DateField()
    end_date = models.DateField()

class Expense(models.Model):
    business_trip = models.ForeignKey(BusinessTrip, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)