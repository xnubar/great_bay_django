from django.db import models

class Item(models.Model):
    name = models.CharField( max_length=120)
    user_id = models.ForeignKey("users_app.Customer", on_delete=models.CASCADE)
    start_bid = models.FloatField(default=.0)
    status = models.IntegerField(default=0)