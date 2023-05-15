# Generated by Django 4.1.6 on 2023-05-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lati', '0007_alter_producto_cantidadproducto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturac',
            name='cantProduct',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='facturac',
            name='costo',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='facturac',
            name='idFacturaC',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='facturav',
            name='cantProduct',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='facturav',
            name='cuanto',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='facturav',
            name='idFacturaV',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='facturav',
            name='totall',
            field=models.PositiveIntegerField(),
        ),
    ]