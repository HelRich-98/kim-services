from django.shortcuts import render

from .models import Skill, Journey, Testimonial
from realization.models import Realization

def home(request):
    realisations_vedette = Realization.objects\
        .filter(is_featured=True)\
        .order_by('-created_at')[:3]
    competences = Skill.objects.all()
    temoignages = Testimonial.objects.all()[:4]
    context = {
        'realisations_vedette': realisations_vedette,
        'competences': competences,
        'temoignages': temoignages,
    }
    return render(request, 'core/home.html', context)

def about_us(request):
    return render(request, 'core/about_us.html')