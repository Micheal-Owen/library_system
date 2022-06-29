# Generated by Django 3.2.7 on 2022-06-29 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_alter_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.BooleanField(choices=[(1, 'Available'), (0, 'Unavailable')], max_length=30),
        ),
    ]
