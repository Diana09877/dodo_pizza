from django.contrib import admin
from django.urls import path
from products.views import PizzaListAPIView, PizzaDetailAPIView
from users.views import UserRegistrationAPIView, UserLoginAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/pizzas/", PizzaListAPIView.as_view(), name="pizza-list"),
    path("api/v1/pizzas/<int:pk>/", PizzaDetailAPIView.as_view(), name="pizza-detail"),
    path("api/v1/users/registration/", UserRegistrationAPIView.as_view(), name="user-registration"),
    path("api/v1/users/login/", UserLoginAPIView.as_view(), name="user-login"),

]
