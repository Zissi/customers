from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from rating.models import CustomerRating

class CustomerView(generic.ListView):
    template_name = 'rating/customers.html'
    context_object_name = 'customers'
    
    def get_queryset(self):
        return CustomerRating.objects.filter()
    
class CustomerCreate(CreateView):
    model = CustomerRating
    template_name = 'rating/edit_customer.html'
    fields = ['first_name', 'last_name', 'email', 'rating', 'contacted']
    success_url = '/'

