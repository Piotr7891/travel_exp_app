import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed
from .models import Employee, BusinessTrip, Expense


@pytest.mark.django_db
def test_login_view(client):
    response = client.post(reverse('login'), {'username': 'testuser', 'password': 'password123'})
    assert response.status_code == 200  # Adjust status code as needed



@pytest.mark.django_db
def test_add_business_trip_view(client):
    user = User.objects.create_user(username='testuser', password='password123')
    client.force_login(user)
    response = client.post(reverse('add-trip'), {'destination': 'New York', 'start_date': '2024-03-20', 'end_date': '2024-03-25'})
    assert response.status_code == 200  # should be 302?


@pytest.mark.django_db
def test_trip_list_view(client):
    user = User.objects.create_user(username='testuser', password='password123')
    client.force_login(user)
    response = client.get(reverse('trip-list'))
    assert response.status_code == 200  # Adjust status code as needed
    assertTemplateUsed(response, 'business_trip_list.html')

@pytest.mark.django_db
def test_employee_creation():
    employee = Employee.objects.create(name='John Doe')
    assert employee.name == 'John Doe'

@pytest.mark.django_db
def test_business_trip_creation():
    employee = Employee.objects.create(name='John Doe')
    trip = BusinessTrip.objects.create(employee=employee, destination='Poland', start_date='2024-03-20', end_date='2024-03-25')
    assert trip.destination == 'Poland'
    assert trip.employee == employee

@pytest.mark.django_db
def test_expense_creation():
    employee = Employee.objects.create(name='John Doe')
    trip = BusinessTrip.objects.create(employee=employee, destination='Poland', start_date='2024-03-20', end_date='2024-03-25')
    expense = Expense.objects.create(business_trip=trip, description='Hotel', amount=100.50, currency='USD')
    assert expense.description == 'Hotel'
    assert expense.amount == 100.50
    assert expense.currency == 'USD'
