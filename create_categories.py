import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from products.models import Category

categories = [
    "Laptops",
    "Mobiles",
    "Fashion",
    "Books",
    "Accessories",
]

for name in categories:

    category, created = Category.objects.get_or_create(
        name=name
    )

    if created:
        print(f"Created category: {name}")
    else:
        print(f"Category already exists: {name}")