from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser


class UserLoginAPIView(APIView):
    """API endpoint для того, чтобы залогинить пользователя"""
    def post(self, request, *args, **kwargs):
        data = request.data
        phone_number = data.get('phone_number')
        password = data.get('password')

        try:
            user = CustomUser.objects.get(phone_number=phone_number)
        except CustomUser.DoesNotExist:
            return Response({"message": "Пользователь не найден"}, status=404)

        if not user.check_password(password):
            return Response({"message": "неправильный пароль"}, status=400)

        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)

class UserRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        phone_number = data.get('phone_number')
        password = data.get('password')

        if CustomUser.objects.filter(phone_number=phone_number).exists():
            return Response({"message": "Пользователь с таким номером телефона уже существует"}, status=400)

        user = CustomUser.objects.create_user(phone_number=phone_number, password=password)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=201)
