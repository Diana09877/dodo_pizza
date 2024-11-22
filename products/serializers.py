from rest_framework import serializers
from products.models import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = (
            'id',
            'name',
            'price',
            'size',
            'image',
            'consist',

        )

class PizzaDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = (
            'id',
            'name',
            'price',
            'size',
            'image',
            'consist',
            'weight',

        )

from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = {
            'id',
            'name',
            'price',
            'volume'
        }

class DrinkDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = {
            'id',
            'name',
            'description',
            'price',
             'volume'
        }
