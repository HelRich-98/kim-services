# Site Vitrine — Atelier Kim Service

## Charpentier & Menuisier

Site web professionnel développé avec Django et Tailwind CSS.

---

## Pages

- **Accueil** — Présentation, compétences, réalisations en vedette, contact
- **Apropos de KIM** — Biographie, timeline, certifications
- **Réalisations** — Galerie filtrée par catégorie

---

## Installation avec Pip

pip install Django Pillow django-tailwind python-decouple

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Avec uv

uv sync

---

## Accès admin

URL : http://localhost:8000/admin
→ Ajouter les réalisations, témoignages et compétences depuis ici.

---

## Stack technique

- Backend : Django 6.0
- Frontend : Tailwind CSS (django-tailwind)
- Base de données : SQLite (dev) / PostgreSQL (prod)
- Images : Pillow
- Variables env : .env (python-decouple)

---

## Développé par

HelRICH BZM (Helan Hulurich Bazebimio)
-Tel: 069866202, 065585285
-Email: helrich.bzm@gmail.com
