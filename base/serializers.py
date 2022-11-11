from rest_framework import serializers
from base.models import Item
from base.models import Todo

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=["task", "completed", "timestamp", "updated"]