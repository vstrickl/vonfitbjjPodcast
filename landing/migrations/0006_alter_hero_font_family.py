# Generated by Django 4.2.6 on 2023-10-28 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_fontfamily_hero_font_family'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='font_family',
            field=models.ManyToManyField(blank=True, to='landing.fontfamily'),
        ),
    ]