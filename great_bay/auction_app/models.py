from django.db import models

class Bid(models.Model):
    item_id = models.ForeignKey("products_app.Item", on_delete = models.CASCADE)
    consumer_id = models.ForeignKey("users_app.Customer", on_delete = models.CASCADE)
    last_bid = models.FloatField()
    is_closed = models.BooleanField(default=False)