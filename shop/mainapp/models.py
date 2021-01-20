from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

from PIL import Image



User = get_user_model()

def get_product_url(obj, viewname, model_name):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})



class MaxResolutionErrorExcept(Exception):
    pass

class MinResolutionErrorExcept(Exception):
    pass

class LatestProductManager:

    @staticmethod
    def get_products_for_mn(*args, **kwargs):

        prioritet = kwargs.get('prioritet')
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().orderby('-id')[:5]
            products.extend(model_products)
        if prioritet:
            ct_model = ContentType.objects.filter(model=prioritet)
            if ct_model.exists():
                if prioritet in args:
                    return sorted(products, key=lambda x: x.__class__._meta.model_name.startswith(prioritet), reverse=True)
        return products

class LatestProducts:

    objects = LatestProductManager
# Category
# Product
# CartProduct
# Cart
# Baying
# Bayer
# Haracteric

class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Название категории')
    slag = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    MIN_RESOLUTION = (400, 400)
    MAX_RESOLUTION = (700, 700)
    MAX_IMAGE_SIZE = 3145728


    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название товара')
    slag = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='фото')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        image = self.image
        img = Image.open(image)
        min_height, min_width = self.MIN_RESOLUTION
        max_height, max_width = self.MAX_RESOLUTION
        if img.height < min_height or img.width < min_width:
            raise MinResolutionErrorExcept('Разрешение изображения меньше минимального!')
        elif img.height > max_height or img.width > max_width:
            raise MaxResolutionErrorExcept('Разрешение изображения больше максимального!')
        super().save(*args, **kwargs)

class Notebook(Product):

    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    display = models.CharField(max_length=255, verbose_name='Тип дисплея')
    processor = models.CharField(max_length=255, verbose_name='Мощность процессора')
    ram = models.CharField(max_length=255, verbose_name='Оперативная память')
    battery_time = models.CharField(max_length=255, verbose_name='Время работы аккумулятора')
    video_card = models.CharField(max_length=255, verbose_name='видеокарта')

    def __str__(self):
        return '{} : {}'.format(self.category, self.title)

    def get_absolut_url(self):
        return get_product_url(self, 'product_detail')

class Smartphone(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    display = models.CharField(max_length=255, verbose_name='Тип дисплея')
    resolution = models.CharField(max_length=255, verbose_name='Разрешение экрана')
    accum_volume = models.CharField(max_length=255, verbose_name='Емкость батареи')
    ram = models.CharField(max_length=255, verbose_name='Оперативная память')
    sd = models.BooleanField(default=True)
    sd_volume_max = models.CharField(max_length=255, verbose_name='Максимальный объем встраиваемого накопителя')
    main_cam_mp = models.CharField(max_length=255, verbose_name='Основная камера')
    front_cam_mp = models.CharField(max_length=255, verbose_name='Фронтальная камера')

    def __str__(self):
        return '{} : {}'.format(self.category, self.title)

    def get_absolut_url(self):
        return get_product_url(self, 'product_detail')

class CartProduct(models.Model):

    user = models.ForeignKey('Bayer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма')

    def __str__(self):
        return 'Товар: {} '.format(self.product.title)

class Cart(models.Model):

    owner = models.ForeignKey('bayer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ForeignKey(CartProduct, blank=True, on_delete=models.CASCADE, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='общая цена')

    def __str__(self):
        return str(self.id)

class Bayer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    adress = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return "покупатель: {} {}".format(self.user.first_name, self.user.last_name)






