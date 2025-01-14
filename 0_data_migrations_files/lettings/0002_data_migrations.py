# Generated by Django 3.0 on 2022-04-11 17:07

from django.db import migrations


def migrate_letting_data(apps, schema_editor):
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewLetting = apps.get_model('app_lettings', 'Letting')
    Address = apps.get_model('app_lettings', 'Address')
    for old_letting_instance in OldLetting.objects.all():
        NewLetting.objects.create(
            title=old_letting_instance.title,
            address=Address.objects.get(id=old_letting_instance.address.id)
        )


def migrate_adress_data(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    NewAddress = apps.get_model('app_lettings', 'Address')
    for old_address_instance in OldAddress.objects.all():
        NewAddress.objects.create(
            number=old_address_instance.number,
            street=old_address_instance.street,
            city=old_address_instance.city,
            state=old_address_instance.state,
            zip_code=old_address_instance.zip_code,
            country_iso_code=old_address_instance.country_iso_code
        )


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
        ('app_lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_adress_data),
        migrations.RunPython(migrate_letting_data),
    ]
