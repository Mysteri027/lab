from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    sur_name = models.CharField(max_length=50)

    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    money_count = models.IntegerField()

    def __str__(self):
        return self.name


class MoneyTransfer(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_to')
    transfer_money_count = models.IntegerField()
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_from')

    def __str__(self):
        return f'Денежный перевод'

