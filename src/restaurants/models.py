from django.db import models


class Restaurant(models.Model):

    name = models.CharField(max_length=50, verbose_name="Название")
    average_check = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Средний чек, тг")
    average_delivery_time = models.PositiveIntegerField(verbose_name="Среднее время доставки, минут")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"
        ordering = ('-id',)

