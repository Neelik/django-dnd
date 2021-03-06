# Generated by Django 2.2 on 2019-05-16 19:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifth_edition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbilityScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(1)], verbose_name='Strength')),
                ('dexterity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(1)], verbose_name='Dexterity')),
                ('constitution', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(1)], verbose_name='Constitution')),
                ('intelligence', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(1)], verbose_name='Intelligence')),
                ('wisdom', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(1)], verbose_name='Wisdom')),
                ('charisma', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(1)], verbose_name='Charisma')),
            ],
        ),
    ]
