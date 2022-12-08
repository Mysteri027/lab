from django.urls import path
from .views import get_users, get_user, get_money_transfers, login, registration, money_transfer

urlpatterns = [
    path('users/', get_users),
    path('user/<int:user_id>', get_user),
    path('moneytranfer/<int:user_id>', get_money_transfers),
    path('login/', login),
    path('registration/', registration),
    path('maketranfer/', money_transfer),
]
