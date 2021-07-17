from django.db import models

# Product model
class Product(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the product")
    price = models.IntegerField(help_text="Price of the product")
    brand = models.CharField(max_length=100, help_text="Manufacturer of the product")
    category = models.CharField(max_length=100, help_text="Category of the product")
    picture = models.CharField(max_length=100, help_text="URL to the product picture") # Like "product_pictures/picture_name.png"

    def __str__(self):
        return self.name