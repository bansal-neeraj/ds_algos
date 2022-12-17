from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=20)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Store(models.Model):
    name = models.CharField(max_length=20)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    minor_product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='minor_prod',null=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    region_name = models.CharField(max_length=30)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)




