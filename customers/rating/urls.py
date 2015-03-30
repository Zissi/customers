from django.conf.urls import patterns, include, url
from. import views

urlpatterns = patterns('',
    url(r'^$', views.CustomerView.as_view(), name='customer_view'),
    url(r'^/new$', views.CustomerCreate.as_view(), name='new_customer'),
    )
