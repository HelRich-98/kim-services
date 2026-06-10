from django.contrib import admin

from .models import Realisation, Competence, Temoignage

# Register your models here.

@admin.register(Realisation)
class RealisationAdmin(admin.ModelAdmin):
    list_display = ("titre", "categorie", "created_at", "annee")


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ("nom", "ordre")

@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ("client", "note", "date")
