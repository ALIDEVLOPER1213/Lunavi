from django.db import models
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='category_foto')
    is_active = models.BooleanField(default=True)


class Clothes(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='product_image')
    price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateField(auto_created=True)

    def __str__(self):
        return f"{self.title}-{self.price}"
