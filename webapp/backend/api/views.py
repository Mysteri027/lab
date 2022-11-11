from django.http import JsonResponse

from .models import User, MoneyTransfer


def get_users(request):
    qs = User.objects.all()

    response = {'items': []}
    for obj in qs:
        response['items'].append({'user': {
            'name': obj.name,
            'surname': obj.sur_name,
            'phoneNumber': obj.phone_number,
            'email': obj.email,
            'moneyCount': obj.money_count
        }})

    return JsonResponse(response)


def get_user(request, user_id):
    try:
        obj = User.objects.get(pk=user_id)
        response = {
            'user': {
                'name': obj.name,
                'surname': obj.sur_name,
                'phoneNumber': obj.phone_number,
                'email': obj.email,
                'moneyCount': obj.money_count
            }
        }
    except:
        response = {"error": "Пользователь не найден"}

    return JsonResponse(response)


def get_money_transfers(request, user_id):
    try:
        obj = MoneyTransfer.objects.get(user_from=user_id)

        response = {
            "items" : {
                "transferMoneyCount": obj.transfer_money_count,
                "user_to": obj.user_to.phone_number
            }
        }

    except:
        response = {"error": "Данный пользователь не совершал переводов"}

    return JsonResponse(response)
