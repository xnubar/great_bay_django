from django.db import models
from django.contrib.auth.models import User

class Customer(User):
    CUSTOMER_TYPE_OWNER = 1
    CUSTOMER_TYPE_CONSUMER = 2
    choice = {
        CUSTOMER_TYPE_OWNER: 'owner',
        CUSTOMER_TYPE_CONSUMER: 'consumer'
    }
    user_type = models.IntegerField(choices = list(choice.items()))

    def save(self, *args, **kwargs):
        print("password: ",self.password)
        self.set_password(self.password)
        self.is_staff = True
        return super().save(*args, **kwargs)

