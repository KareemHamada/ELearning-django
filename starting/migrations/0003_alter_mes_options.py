# Generated by Django 3.2.5 on 2021-12-15 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('starting', '0002_room_participarnts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mes',
            options={'ordering': ['-updated', '-created']},
        ),
    ]