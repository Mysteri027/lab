from django.urls import path
from .views import get_users, get_user, get_money_transfers

urlpatterns = [
    path('users/', get_users),
    path('user/<int:user_id>', get_user),
    path('moneytranfer/<int:user_id>', get_money_transfers),
]
