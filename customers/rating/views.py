from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse
from rating.models import CustomerRating
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .forms import MailForm

class CustomerView(generic.ListView):
    template_name = 'rating/customers.html'
    context_object_name = 'customers'
    
    def get_queryset(self):
        return CustomerRating.objects.filter()
    
class CustomerCreate(CreateView):
    model = CustomerRating
    template_name = 'rating/create_customer.html'
    fields = ['first_name', 'last_name', 'email', 'rating', 'contacted']
    success_url = '/'
    
class CustomerUpdate(UpdateView):
    model = CustomerRating
    fields = ['first_name', 'last_name', 'email', 'rating', 'contacted']
    template_name = 'rating/update_customer.html'
    success_url = '/'
    
def send_email(subject, text, email):
    email = EmailMessage(subject, text, to=[email])
    email.send()

def write_email(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            customer = CustomerRating.objects.get(id=1)
            email = customer.email
            send_email(subject, text, email)
            return HttpResponse('E-mail successfully sent :)')
    else:
        form = MailForm()
    return render(request, 'rating/write_email.html', {'form': form})


