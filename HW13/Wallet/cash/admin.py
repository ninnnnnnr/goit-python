from django.contrib import admin
from .models import Income, Costs


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('cash_income', 'categories', 'comment', 'pub_date')
    list_filter = ('pub_date',)


@admin.register(Costs)
class CostsAdmin(admin.ModelAdmin):
    list_display = ('cash_out', 'categories', 'comment', 'pub_date')
    list_filter = ('pub_date',)


