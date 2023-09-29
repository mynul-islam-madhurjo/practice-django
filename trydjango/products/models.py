from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)  # max length required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField()

    # Adding new field
    features = models.BooleanField(null=True)  # default='Empty'

    def get_absolute_url(self):
        # return f"/products/product/{self.id}"
        return reverse('show-blogs', kwargs={
            'my_id': self.id
        })