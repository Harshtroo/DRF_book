# Generated by Django 4.2.3 on 2023-07-22 08:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_crud", "0002_alter_book_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="publication_date",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
