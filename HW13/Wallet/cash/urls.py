from django.urls import path

from . import views

urlpatterns = [
    path('', views.IncomeCreate.as_view(), name='incomes'),
    path('costs', views.CostsCreate.as_view(), name='costs'),

]
