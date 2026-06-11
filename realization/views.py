from django.shortcuts import render

from .models import Realization

# Create your views here.

def gallery(request):
    categorie = request.GET.get('categorie', '')
    realisations = Realization.objects.all()
    if categorie:
        realisations = realisations.filter(category=categorie)
    context = {
        'realisations': realisations,
        'categorie_active': categorie,
    }
    return render(request, 'realization/gallery.html', context)