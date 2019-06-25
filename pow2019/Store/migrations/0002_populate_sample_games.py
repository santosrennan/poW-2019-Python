# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations


def create_categories(apps, schema_editor):
    Category = apps.get_model("Store", "Category")
    Category.objects.create(name="Ação")
    Category.objects.create(name="Aventura")
    Category.objects.create(name="FPS")
    Category.objects.create(name="Corrida")
    Category.objects.create(name="Esportes")
    Category.objects.create(name="Puzzle")
    Category.objects.create(name="Test")

class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_categories),
    ]
