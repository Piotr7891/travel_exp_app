from django.db import models


# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#
# class BusinessTrip(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     destination = models.CharField(max_length=255)
#     start_date = models.DateField()
#     end_date = models.DateField()