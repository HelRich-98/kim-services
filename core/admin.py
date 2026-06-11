from django.contrib import admin

from .models import Skill, Journey, Testimonial

# Register your models here.


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "order")


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = ("title", "date")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("client", "note", "date")
    