# Generated by Django 4.1.2 on 2023-04-15 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lati', '0014_facturac_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoriaP',
        ),
    ]
