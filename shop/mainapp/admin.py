from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from PIL import Image


class NotebookAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style="color:red; font-size:16px;"> Загружайте изображение с минимальный разрешением от {}x{}'.format(
                                                                                                *Product.MIN_RESOLUTION)
                                                                                        ) \
                                         + \
                                         mark_safe(
                                             '<span style="color:red; font-size:16px;"> до {}x{}'.format(*Product.MAX_RESOLUTION)
                                         )

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        max_size = Product.MAX_IMAGE_SIZE
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Разрешение изображения меньше минимального!')
        elif img.height > max_height or img.width > max_width:
            raise ValidationError('Разрешение изображения больше максимального!')
        elif image.size > max_size:
            raise ValidationError('Размер изображения больше 3Mb!')
        return image


class NotebookAdmin(admin.ModelAdmin):

    form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class TvsetAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='tvsets'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)





admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Bayer)
admin.site.register(TvSet)
