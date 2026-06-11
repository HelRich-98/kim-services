from django.test import TestCase

from .models import Skill, Journey, Testimonial

# Create your tests here.

class SkillTestCase(TestCase):
    def setUp(self):
        Skill.objects.create(name="Python", icon="🐍", description="Langage de programmation polyvalent", order=1)
        Skill.objects.create(name="Django", icon="🌐", description="Framework web en Python", order=2)

    def test_skill_creation(self):
        s1 = Skill.objects.get(name="Python")
        s2 = Skill.objects.get(name="Django")
        self.assertEqual(s1.icon, "🐍")
        self.assertEqual(s1.description, "Langage de programmation polyvalent")
        self.assertEqual(s1.order, 1)
        self.assertEqual(str(s1), "Python")
        self.assertEqual(s2.icon, "🌐")
        self.assertEqual(s2.description, "Framework web en Python")
        self.assertEqual(s2.order, 2)
        self.assertEqual(str(s2), "Django")

    def test_skill_str(self):
        s = Skill.objects.get(name="Python")
        self.assertEqual(str(s), "Python")


class JourneyTestCase(TestCase):
    def setUp(self):
        Journey.objects.create(title="Début de la carrière", description="J'ai commencé à coder en 2010", date="2010-01-01")
        Journey.objects.create(title="Premier emploi", description="J'ai obtenu mon premier emploi en 2012", date="2012-06-01")

    def test_journey_creation(self):
        j1 = Journey.objects.get(title="Début de la carrière")
        j2 = Journey.objects.get(title="Premier emploi")
        self.assertEqual(j1.description, "J'ai commencé à coder en 2010")
        self.assertEqual(j1.date.strftime("%Y-%m-%d"), "2010-01-01")
        self.assertEqual(str(j1), "Début de la carrière")
        self.assertEqual(j2.description, "J'ai obtenu mon premier emploi en 2012")
        self.assertEqual(j2.date.strftime("%Y-%m-%d"), "2012-06-01")
        self.assertEqual(str(j2), "Premier emploi")

    def test_journey_str(self):
        j = Journey.objects.get(title="Début de la carrière")
        self.assertEqual(str(j), "Début de la carrière")

    
class TestimonialTestCase(TestCase):
    def setUp(self):
        Testimonial.objects.create(client="Alice", content="Excellent service!", note=5, date="2023-01-01")
        Testimonial.objects.create(client="Bob", content="Très satisfait du travail.", note=4, date="2023-02-01")

    def test_testimonial_creation(self):
        t1 = Testimonial.objects.get(client="Alice")
        t2 = Testimonial.objects.get(client="Bob")
        self.assertEqual(t1.content, "Excellent service!")
        self.assertEqual(t1.note, 5)
        self.assertEqual(t1.date.strftime("%Y-%m-%d"), "2023-01-01")
        self.assertEqual(str(t1), "Alice - 5 étoiles")
        self.assertEqual(t2.content, "Très satisfait du travail.")
        self.assertEqual(t2.note, 4)
        self.assertEqual(t2.date.strftime("%Y-%m-%d"), "2023-02-01")
        self.assertEqual(str(t2), "Bob - 4 étoiles")

    def test_testimonial_str(self):
        t = Testimonial.objects.get(client="Alice")
        self.assertEqual(str(t), "Alice - 5 étoiles")