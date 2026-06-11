from django.db import models

# Create your models here.

class Realization(models.Model):
    CATEGORIE_CHOICES = [
        ('charpente', 'Charpente'),
        ('menuiserie', 'Menuiserie'),
        ('mixte', 'Mixte'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)
    location = models.CharField(max_length=100, blank=True)
    client = models.CharField(max_length=100, blank=True)
    date = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def get_featured_image_url(self):
        return self.images.first().image.url if self.images.exists() else None

class Image(models.Model):
    image = models.ImageField(upload_to='realisations/')
    description = models.CharField(max_length=255, blank=True)
    realization = models.ForeignKey(
        Realization, 
        related_name='images', 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.description or f"Image {self.id}"