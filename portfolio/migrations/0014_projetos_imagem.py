# Generated by Django 4.0.4 on 2022-05-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_alter_projetos_participantes'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='imagem',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]