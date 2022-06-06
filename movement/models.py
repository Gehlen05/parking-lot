from django.db import models


class Movement(models.Model):
    entry_date = models.DateTimeField()
    exit_date = models.DateTimeField(null=True)
    validate_date = models.DateTimeField(null=True)
    value_real = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.CASCADE)
    plate = models.CharField(max_length=50)

    class Meta:
        db_table = "TB_PARKMOVEMENT"

    def __str__(self):
        return self.plate
