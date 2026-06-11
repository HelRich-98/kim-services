from django.test import TestCase

from .models import Realization

# Create your tests here.

class RealizationTestCase(TestCase):
    def setUp(self):
        Realization.objects.create(
            title="Réalisation 1",
            description="Description de la réalisation 1",
            category="web",
            date="2023-01-01",
        )
        Realization.objects.create(
            title="Réalisation 2",
            description="Description de la réalisation 2",
            category="mobile",
            date="2023-02-01",
        )

    def test_realization_creation(self):
        r1 = Realization.objects.get(title="Réalisation 1")
        r2 = Realization.objects.get(title="Réalisation 2")
        self.assertEqual(r1.description, "Description de la réalisation 1")
        self.assertEqual(r1.category, "web")
        self.assertEqual(str(r1), "Réalisation 1")
        self.assertEqual(r2.description, "Description de la réalisation 2")
        self.assertEqual(r2.category, "mobile")
        self.assertEqual(str(r2), "Réalisation 2")

    def test_realization_str(self):
        r = Realization.objects.get(title="Réalisation 1")
        self.assertEqual(str(r), "Réalisation 1")

    def test_realization_get_featured_image_url(self):
        r = Realization.objects.get(title="Réalisation 1")
        self.assertIsNone(r.get_featured_image_url())


class ImageTestCase(TestCase):
    def setUp(self):
        r = Realization.objects.create(
            title="Réalisation 1",
            description="Description de la réalisation 1",
            category="web",
            date="2023-01-01",
        )
        r.images.create(description="Image 1")
        r.images.create(description="Image 2")

    def test_image_creation(self):
        r = Realization.objects.get(title="Réalisation 1")
        images = r.images.all()
        self.assertEqual(images.count(), 2)
        self.assertEqual(str(images[0]), "Image 1")
        self.assertEqual(str(images[1]), "Image 2")