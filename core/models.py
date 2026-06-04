from django.db import models

class Realisation(models.Model):
    CATEGORIE_CHOICES = [
        ('charpente', 'Charpente'),
        ('menuiserie', 'Menuiserie'),
        ('mixte', 'Mixte'),
    ]
    titre = models.CharField(max_length=200)
    description = models.TextField()
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)
    image = models.ImageField(upload_to='realisations/')
    lieu = models.CharField(max_length=100, blank=True)
    annee = models.PositiveIntegerField(null=True, blank=True)
    en_vedette = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.titre


class Competence(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    icone = models.CharField(max_length=50, help_text="Nom de l'icône SVG ou emoji")
    ordre = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordre']

    def __str__(self):
        return self.nom


class Temoignage(models.Model):
    client = models.CharField(max_length=100)
    texte = models.TextField()
    note = models.PositiveIntegerField(default=5)
    date = models.DateField()

    def __str__(self):
        return f"Témoignage de {self.client}"
