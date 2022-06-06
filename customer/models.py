from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "TB_CUSTOMER"

    def __str__(self):
        return {self.name}
