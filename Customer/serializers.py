from rest_framework import serializers 
from Customer.models import Customer
 
 
class CustomerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Customer
        fields = ('store_id',
                   'first_name',
                   'last_name',
                   'email',
                   'address_id',
                   'active',
                   'create_date',
                   'last_update')