from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    TITLE_CHOICES = (
        ('HELLO', 'HELLO'),
    )

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='products')
    title = models.CharField(choices=TITLE_CHOICES, max_length=255)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return self.title



