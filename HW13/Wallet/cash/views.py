from django.urls import reverse_lazy
from .models import Income, Costs
from django.views import generic
from django.db.models import Sum, Count
from django.views.generic.edit import CreateView


class IncomeCreate(CreateView, generic.ListView):
    model = Income
    fields = '__all__'
    template_name = "income_form.html"
    context_object_name = 'incomes_list'
    paginate_by = 10
    success_url = reverse_lazy('incomes')

    def get_context_data(self, **kwargs):
        incomes = Income.objects.aggregate(Sum('cash_income'))['cash_income__sum']
        costs = Costs.objects.aggregate(Sum('cash_out'))['cash_out__sum']
        budget = incomes - costs
        context = {
            'incomes': incomes, 'costs': costs, 'budget': budget}
        kwargs.update(context)
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        if len(self.request.GET)==0:
            return Income.objects.all()
        try:
            if 'start_date' and 'end_date' in self.request.GET:
                self.start_date = self.request.GET['start_date']
                self.end_date = self.request.GET['end_date']
                return Income.objects.filter(pub_date__range=(self.start_date, self.end_date))
        except:
            return Income.objects.all()


class CostsCreate(CreateView, generic.ListView):
    model = Costs
    fields = '__all__'
    template_name = "costs_list.html"
    context_object_name = 'costs_list'
    paginate_by = 10
    success_url = reverse_lazy('costs')

    def get_context_data(self, **kwargs):
        incomes = Income.objects.aggregate(Sum('cash_income'))['cash_income__sum']
        costs = Costs.objects.aggregate(Sum('cash_out'))['cash_out__sum']
        budget = incomes - costs
        context = {
            'incomes': incomes, 'costs': costs, 'budget': budget}
        kwargs.update(context)
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        if len(self.request.GET)==0:
            return Costs.objects.all()
        try:
            if 'start_date' and 'end_date' in self.request.GET:
                self.start_date = self.request.GET['start_date']
                self.end_date = self.request.GET['end_date']
                return Costs.objects.filter(pub_date__range=(self.start_date, self.end_date))
        except:
            return Costs.objects.all()



