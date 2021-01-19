# Generated by Django 3.1.2 on 2021-01-19 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название товара')),
                ('slag', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='фото')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Диагональ')),
                ('display', models.CharField(max_length=255, verbose_name='Тип дисплея')),
                ('resolution', models.CharField(max_length=255, verbose_name='Разрешение экрана')),
                ('accum_volume', models.CharField(max_length=255, verbose_name='Емкость батареи')),
                ('ram', models.CharField(max_length=255, verbose_name='Оперативная память')),
                ('sd', models.BooleanField(default=True)),
                ('sd_volume_max', models.CharField(max_length=255, verbose_name='Максимальный объем встраиваемого накопителя')),
                ('main_cam_mp', models.CharField(max_length=255, verbose_name='Основная камера')),
                ('front_cam_mp', models.CharField(max_length=255, verbose_name='Фронтальная камера')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название товара')),
                ('slag', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='фото')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Диагональ')),
                ('display', models.CharField(max_length=255, verbose_name='Тип дисплея')),
                ('processor', models.CharField(max_length=255, verbose_name='Мощность процессора')),
                ('ram', models.CharField(max_length=255, verbose_name='Оперативная память')),
                ('battery_time', models.CharField(max_length=255, verbose_name='Время работы аккумулятора')),
                ('video_card', models.CharField(max_length=255, verbose_name='видеокарта')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]