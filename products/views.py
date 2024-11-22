from products.models import Pizza
from products.serializers import PizzaSerializer, PizzaDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Drink
from .serializers import DrinkSerializer, DrinkDetailSerializer

class PizzaListAPIView(APIView):
    """вьюха, чтобы вернуть список пицц"""

    def get(self, request, *args, **kwargs):
        pizza_list = Pizza.objects.all()
        serializer = PizzaSerializer(instance=pizza_list, many=True)
        response_body = serializer.data

        return Response(status=200, data=response_body)



class PizzaDetailAPIView(APIView):
    """вьюха для получения подробной информации о пицце"""

    def get(self, request, *args, **kwargs):
         pizza = Pizza.objects.get(id=kwargs['pk'])
         serializer = PizzaDetailSerializer(instance=pizza, many=False)
         response_body = serializer.data

         return Response(status=200, data=response_body)



class DrinkListAPIView(APIView):
    """вьюха для получения списка напитков"""

    def get(self, request, *args, **kwargs):
        drink_list = Drink.objects.all()
        serializer = DrinkSerializer(instance=drink_list, many=True)
        response_body = serializer.data
        return Response(status=200, data=response_body)

class DrinkDetailAPIView(APIView):
    """вьюха для получения подробной информации о напитке"""

    def get(self, request, *args, **kwargs):
        try:
            drink = Drink.objects.get(id=kwargs['pk'])
        except Drink.DoesNotExist:
            return Response(status=400, data={'message': 'Такого напитка не существует'})
        serializer = DrinkDetailSerializer(instance=drink, many=False)
        response_body = serializer.data
        return Response(status=200, data=response_body)
