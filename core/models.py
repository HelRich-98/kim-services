from django.db import models
from django.urls import reverse

# Create your models here.

class App(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="apps/images/", blank=True, null=True)
    path = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("app_detail", kwargs={"pk": self.pk})
