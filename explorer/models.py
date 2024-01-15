from django.db import models


class StarSystem(models.Model):
    name = models.CharField(max_length=100)
    # stars = models.ManyToManyField(Star)

    def __str__(self):
        return self.name

class Star(models.Model):
    name = models.CharField(max_length=100)
    # weight = models.FloatField()
    distance = models.FloatField()
    system = models.ForeignKey(StarSystem, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name