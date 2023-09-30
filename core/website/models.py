from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=255)
    persentage = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(100)], default=0)
    class Meta:
        ordering = ['name', 'persentage']

    def __str__(self):
        return self.name