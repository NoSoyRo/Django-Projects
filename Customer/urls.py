from django.urls import re_path
from Customer import views 
 
urlpatterns = [ 
    re_path(r'customers', views.customerList),
    re_path(r'customers/(?P<pk>[0-9]+)', views.customerDetail)
]