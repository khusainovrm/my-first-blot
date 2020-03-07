from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20) # max_length required
    description = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(default='this is cool!') # max_length required
    newcollection = models.BooleanField()

"""    def publish(self):
        self.save ()

    def __str__(self):
        return self.titl"""