# Generated by Django 4.0.5 on 2022-07-06 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_merge_20220706_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='book_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='book_name',
            field=models.CharField(max_length=200),
        ),
    ]
