# Generated by Django 4.0.4 on 2022-05-16 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_post_imagem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='imagem',
            new_name='image',
        ),
    ]