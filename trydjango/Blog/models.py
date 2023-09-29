from django.db import models
from django.urls import reverse


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(null=True)

    def get_absolute_url(self):
        # return f"/products/product/{self.id}"
        return reverse('blogs:blog-details', kwargs={
            'id': self.id
        })
