from django.shortcuts import render
from .models import Realisation, Competence, Temoignage

def home(request):
    realisations_vedette = Realisation.objects.filter(en_vedette=True)[:3]
    competences = Competence.objects.all()
    temoignages = Temoignage.objects.all()[:4]
    context = {
        'realisations_vedette': realisations_vedette,
        'competences': competences,
        'temoignages': temoignages,
    }
    return render(request, 'core/home.html', context)

def story(request):
    return render(request, 'core/story.html')

def gallery(request):
    categorie = request.GET.get('categorie', '')
    realisations = Realisation.objects.all()
    if categorie:
        realisations = realisations.filter(categorie=categorie)
    context = {
        'realisations': realisations,
        'categorie_active': categorie,
    }
    return render(request, 'core/gallery.html', context)