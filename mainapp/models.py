from django.db import models

# Create your models here.


CATEGORY_CHOICES=[
("Men","men"),
("Women","women"),
("Kids","kids"),
("Featured","featured"),
("Latest","latest")
]


class Product(models.Model):
    title=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.TextField()
    size=models.CharField(max_length=20)
    category=models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    image=models.ImageField(upload_to='media')