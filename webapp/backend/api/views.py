import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, MoneyTransfer


def get_users(request):
    qs = User.objects.all()

    response = {'items': []}
    for obj in qs:
        response['items'].append({
            'user': {
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
            'name': obj.name,
            'surName': obj.sur_name,
            'email': obj.email,
            'moneyCount': obj.money_count,
            'phoneNumber': obj.phone_number
        }

        print(response["moneyCount"])
    except:
        response = {"error": "Пользователь не найден"}

    return JsonResponse(response)


def get_money_transfers(request, user_id):
    qs = MoneyTransfer.objects.all()
    response = {'items': []}
    for obj in qs:
        if obj.user_from.pk == user_id:
            response['items'].append({
                "transferMoneyCount": obj.transfer_money_count,
                "user_to": obj.user_to.phone_number
            })

    if len(response['items']) == 0:
        response['items'] = "Пользователь не совершал переводов"

    return JsonResponse(response)


@csrf_exempt
def money_transfer(request):
    phone_number = json.loads(request.body)["phoneNumber"]
    user_id = json.loads(request.body)["userId"]
    money = json.loads(request.body)["money"]

    user_from = User.objects.get(pk=user_id)
    user_to = User.objects.get(phone_number=phone_number)

    print(f'{user_to.pk}')
    print(f'{user_from.pk}')

    if user_from is not None and user_to is not None:
        if int(money) <= user_from.money_count:
            user_from.money_count -= int(money)
            user_to.money_count += int(money)

            user_from.save()
            user_to.save()

            money_transfer = MoneyTransfer()
            money_transfer.transfer_money_count = int(money)
            money_transfer.user_from = user_from
            money_transfer.user_to = user_to

            money_transfer.save()

            response = {"success": "Перевод прошел успешно"}

        else:
            response = {"error": "Недостаточно средств"}
    else:
        response = {"error": "Перевод данному пользователю не доступен"}

    return JsonResponse(response)


@csrf_exempt
def registration(request):
    email = json.loads(request.body)["email"]
    phone_number = json.loads(request.body)["phoneNumber"]
    name = json.loads(request.body)["name"]
    sur_name = json.loads(request.body)["surName"]
    password = json.loads(request.body)["password"]
    second_password = json.loads(request.body)["secondPassword"]

    print(email, name, sur_name, password, second_password)

    if password == second_password:
        user = User()
        user.email = email
        user.name = name
        user.sur_name = sur_name
        user.password = password
        user.money_count = 1000
        user.phone_number = phone_number

        user.save()

        print("Пользователь добавлен")
        response = {"success": user.pk}
        print(response['success'])

    else:
        response = {"error": "Пароли не совпадают"}

    return JsonResponse(response)


@csrf_exempt
def login(request):
    email = json.loads(request.body)["email"]
    password = json.loads(request.body)["password"]

    users = User.objects.all()

    for user in users:
        if email == user.email and password == user.password:
            response = {"success": user.pk}
            print("success", user.pk)
            return JsonResponse(response)

    print("Пользователь не найден")
    response = {"error": "Пользователь не найден"}
    return JsonResponse(response)
