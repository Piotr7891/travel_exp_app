from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView
from .models import Employee, BusinessTrip, Expense
from .forms import AddBusinessTripForm, AddExpenseForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import TemplateView

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class AddBusinessTrip(LoginRequiredMixin, View):
    template_name = 'add_trip.html'

    @method_decorator(login_required)
    def get(self, request):
        form = AddBusinessTripForm()
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = AddBusinessTripForm(request.POST)
        if form.is_valid():
            destination = form.cleaned_data['destination']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            user = request.user

            employee, created = Employee.objects.get_or_create(name=user.username)

            BusinessTrip.objects.create(
                employee=employee,
                destination=destination,
                start_date=start_date,
                end_date=end_date
            )
            return redirect("trip-list")

        return render(request, self.template_name, {'form': form})

class BusinessTripList(View):
    template_name = 'business_trip_list.html'

    def get(self, request):
        trips = BusinessTrip.objects.filter(employee__name=request.user.username)
        return render(request, self.template_name, {'trips': trips})

class AddExpenseToTrip(LoginRequiredMixin, View):
    template_name = 'add_expense.html'

    @method_decorator(login_required)
    def get(self, request, trip_id):
        trip = get_object_or_404(BusinessTrip, pk=trip_id)
        form = AddExpenseForm()
        return render(request, self.template_name, {'form': form, 'trip': trip})

    @method_decorator(login_required)
    def post(self, request, trip_id):
        trip = get_object_or_404(BusinessTrip, pk=trip_id)
        form = AddExpenseForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            amount = form.cleaned_data['amount']
            currency = form.cleaned_data['currency']


            Expense.objects.create(
                business_trip=trip,
                description=description,
                amount=amount,
                currency=currency
            )

            return redirect(reverse('trip-list'))

        return render(request, self.template_name, {'form': form, 'trip': trip})


class UpdateBusinessTrip(LoginRequiredMixin, UpdateView):
    model = BusinessTrip
    fields = ['destination', 'start_date', 'end_date']
    template_name = 'update_trip.html'
    success_url = reverse_lazy('trip-list')

class DeleteBusinessTrip(LoginRequiredMixin, DeleteView):
    model = BusinessTrip
    template_name = 'trip_confirm_delete.html'
    success_url = reverse_lazy('trip-list')

class UpdateExpense(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = ['description', 'amount', 'currency', 'expense_image']
    template_name = 'update_expense.html'
    success_url = reverse_lazy('trip-list')


class DeleteExpense(LoginRequiredMixin, DeleteView):
    model = Expense
    success_url = reverse_lazy('trip-list')
