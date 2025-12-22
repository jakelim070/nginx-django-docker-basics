from django.db import models


class EnginePart(models.Model):
    part_number = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.part_number


class EnginePartInstance(models.Model):
    engine_part = models.ForeignKey(EnginePart, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=200)
    qty = models.IntegerField()

    def __str__(self):
        return f"{self.engine_part.part_number} - {self.serial_number}"
