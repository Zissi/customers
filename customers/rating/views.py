from django.shortcuts import render
from django.views import generic
from rating.models import CustomerRating

class CustomerView(generic.ListView):
    template_name = 'rating/customers.html'
    context_object_name = 'customers'
    
    def get_queryset(self):
        return CustomerRating.objects.filter()
