from rest_framework import serializers #using rest_framework to serialize the data (from models to json)
from .models import SalesItem

class SalesItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesItem
        fields = ['id', 'user_account_id', 'name', 'price']
# may need to check if this pep8 complient