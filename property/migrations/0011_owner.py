# Generated by Django 2.2.4 on 2020-10-06 08:51

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0010_auto_20201005_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(db_index=True, max_length=200,
                                                verbose_name='ФИО владельца')),
                ('owner_number', models.CharField(db_index=True, max_length=20,
                                                  verbose_name='Номер владельца')),
                ('owner_pure_phone',
                 phonenumber_field.modelfields.PhoneNumberField(blank=True,
                                                                db_index=True,
                                                                max_length=128,
                                                                region=None,
                                                                verbose_name='Нормализованный номер владельца')),
                ('apartments',
                 models.ManyToManyField(db_index=True, related_name='owners',
                                        to='property.Flat',
                                        verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
