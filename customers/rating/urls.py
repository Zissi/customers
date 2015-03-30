from django.conf.urls import patterns, include, url
from. import views

urlpatterns = patterns('',
    url(r'^$', views.CustomerView.as_view(), name='customer_view'),
    url(r'^/new$', views.CustomerCreate.as_view(), name='new_customer'),
    url(r'^/update_customer/(?P<pk>[0-9]+)/$', views.CustomerUpdate.as_view(), name='update_customer'),
    url(r'^/write_email', views.write_email, name='write_email'),
    )
