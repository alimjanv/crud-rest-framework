# Generated by Django 4.2.16 on 2024-11-12 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManager ', '0002_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='LibraryManager ',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='LibraryManager.author'),
        ),
    ]
