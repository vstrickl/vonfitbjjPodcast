# Generated by Django 4.2.6 on 2023-10-28 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_rename_general_font_family_hero_general_font_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fontfamily',
            old_name='name',
            new_name='family_name',
        ),
        migrations.RenameField(
            model_name='fontfamily',
            old_name='family',
            new_name='serif_type',
        ),
    ]
