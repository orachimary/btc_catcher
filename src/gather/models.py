from django.db import models

class BTC(models.Model):

    usd_price = models.FloatField()
    percent_change_1h = models.FloatField()
    percent_change_24h = models.FloatField()
    last_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Криптовалюта BTC"
        verbose_name_plural = "Криптовалюты BTC"

    def __str__(self):
        return f"{self.usd_price}"