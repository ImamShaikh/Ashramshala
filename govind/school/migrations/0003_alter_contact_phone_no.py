# Generated by Django 5.2 on 2025-04-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_contact_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_no',
            field=models.BigIntegerField(max_length=10),
        ),
    ]
