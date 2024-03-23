"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView
from travel_app.views import SignUpView, AddBusinessTrip, BusinessTripList, AddExpenseToTrip, UpdateBusinessTrip, DeleteBusinessTrip, UpdateExpense, DeleteExpense

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('add-trip/', AddBusinessTrip.as_view(), name='add-trip'),
    path('trip-list/', BusinessTripList.as_view(), name='trip-list'),
    path('add-expense/<int:trip_id>/', AddExpenseToTrip.as_view(), name='add-expense'),
    path('update-trip/<int:pk>/', UpdateBusinessTrip.as_view(), name='update-trip'),
    path('delete-trip/<int:pk>/', DeleteBusinessTrip.as_view(), name='delete-trip'),
    path('update-expense/<int:pk>/', UpdateExpense.as_view(), name='update-expense'),
    path('delete-expense/<int:pk>/', DeleteExpense.as_view(), name='delete-expense'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
