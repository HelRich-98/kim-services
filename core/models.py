from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Nom de l'icône SVG ou emoji")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
    

class Journey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
    
    
class Testimonial(models.Model):
    client = models.CharField(max_length=100)
    content = models.TextField()
    note = models.PositiveIntegerField(default=5)
    date = models.DateField()

    def __str__(self):
        return f"{self.client} - {self.note} étoiles"

