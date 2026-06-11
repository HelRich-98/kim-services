from django.contrib import admin

from .models import Realization, Image

# Register your models here.

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

@admin.register(Realization)
class RealizationAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at", "date", "images_count")
    inlines = [ImageInline]

    @admin.display(description="Images associées")
    def images_count(self, obj):
        return obj.images.count()

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("description", "realization")