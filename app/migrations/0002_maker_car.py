# Generated by Django 4.1.5 on 2023-02-05 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maker', models.CharField(max_length=200, null=True, verbose_name='メーカー名')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=200, null=True, verbose_name='車名')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.maker')),
            ],
        ),
    ]