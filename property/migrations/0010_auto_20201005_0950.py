# Generated by Django 2.2.4 on 2020-10-05 06:50

from django.db import migrations
import phonenumbers


def create_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats:
        parsed_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        flat.owner_pure_phone = phonenumbers.format_number(parsed_number,
                                                           phonenumbers.PhoneNumberFormat.E164)
        flat.save()


def delete_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats:
        flat.owner_pure_phone = ''
        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0009_auto_20200929_1643'),
    ]

    operations = [
        migrations.RunPython(create_owner_pure_phone, delete_owner_pure_phone)
    ]
