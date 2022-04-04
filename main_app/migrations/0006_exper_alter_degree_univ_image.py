# Generated by Django 4.0.2 on 2022-03-22 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_degree'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.CharField(max_length=10)),
                ('company', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='degree',
            name='univ_image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]