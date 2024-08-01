from django.db import models
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='category_foto')
    is_active = models.BooleanField(default=True)


class Clothes(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(upload_to='image foto')
    images = models.ImageField(upload_to='images foto')
    description = models.TextField()
    price = models.IntegerField(default=100)
    color = models.CharField(max_length=120)
    country = models.CharField(max_length=120, null=True, blank=True)
    size = models.IntegerField(default=1)
    category = models.ForeignKey(Category, max_length=120, null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}-{self.price, self.image}"
