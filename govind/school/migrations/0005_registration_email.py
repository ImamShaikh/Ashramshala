# Generated by Django 5.2 on 2025-04-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_registration_alter_contact_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
