from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

User = get_user_model()


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

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название товара')
    slag = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='фото')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title

class CartProduct(models.Model):

    user = models.ForeignKey('Bayer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма')

    def __str__(self):
        return 'Товар: {} '.format(self.product.title)

class Cart(models.Model):

    owner = models.ForeignKey('bayer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ForeignKey(CartProduct, blank=True)
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

class Haracteric(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, verbose_name='имя товара для характеризации')

    def __str__(self):
        return "Характеристика для товара: {}".format(self.name)

    


