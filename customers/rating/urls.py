from django.conf.urls import patterns, include, url
from. import views

urlpatterns = patterns('',
    url(r'^$', views.CustomerView.as_view(), name='customer_view'),
    )
