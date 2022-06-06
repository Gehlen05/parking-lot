from django.db import models


class Vehicle(models.Model):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    plate = models.CharField(max_length=10)
    kind_choices = [(1, "Moto"), (2, "Carro")]
    kind = models.IntegerField(choices=kind_choices)

    class Meta:
        db_table = "TB_CUSTOMER_VEHICLES"

    def __str__(self):
        return self.plate
