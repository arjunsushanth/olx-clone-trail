from django.db import models
from django.contrib.auth.models import User


# this is user profile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_images")
    address = models.CharField(max_length=200)
    phone = models.PositiveIntegerField()


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.category_name
        


class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="product_photos",null=True,blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    condition = models.CharField(null=True, max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    options = (
        ("for sale", "for sale"),
        ("exchange", "exchange"),
        ("sold out", "sold out"),
        ("rent", "rent"),
    )
    status = models.CharField(choices=options, default="for-sale", max_length=200)
    created_date = models.DateField(auto_now_add=True)




    def __str__(self):
        return self.name
    


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to="product_images")

    def __str__(self):
        return self.product.name
    


class Notification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    options = (
        ("sent", "sent"),
        ("pending", "pending"),
        ("cancelled", "cancelled")
    )
    status = models.CharField(choices=options, default="sent", max_length=200)


# Create your models here.
