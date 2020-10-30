from django.db import models

# Create your models here.

class PoolTable(models.Model):
    table_number = models.IntegerField()
    clean_rating = models.IntegerField()
    damage_rating = models.IntegerField()

    def __str__(self):
        return f'{self.table_number}'


class Review(models.Model):
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.rating}'
