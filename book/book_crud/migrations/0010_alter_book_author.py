# Generated by Django 4.2.3 on 2023-08-16 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_crud", "0009_alter_book_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ManyToManyField(to="book_crud.author"),
        ),
    ]
