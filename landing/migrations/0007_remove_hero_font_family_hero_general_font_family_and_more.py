# Generated by Django 4.2.6 on 2023-10-28 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_alter_hero_font_family'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='font_family',
        ),
        migrations.AddField(
            model_name='hero',
            name='general_font_family',
            field=models.ManyToManyField(blank=True, related_name='general', to='landing.fontfamily'),
        ),
        migrations.AddField(
            model_name='hero',
            name='header_font_family',
            field=models.ManyToManyField(blank=True, related_name='headers', to='landing.fontfamily'),
        ),
    ]
