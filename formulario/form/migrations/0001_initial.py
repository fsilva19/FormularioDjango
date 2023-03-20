# Generated by Django 4.1.5 on 2023-03-18 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('nascimento', models.DateTimeField()),
                ('curso', models.CharField(max_length=255)),
                ('instituicao', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.CharField(max_length=20)),
                ('instagram', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]