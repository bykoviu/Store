from django.shortcuts import render
from django.views.generic import DetailView
from .models import Notebook, Smartphone

def index(request):
    return render(request, 'base.html')

class ProductDetailView(DetailView):

    CT_MODEL_MODEL_CLASS = {
        'notebook': Notebook,
        'smartphone': Smartphone
    }

    def dispatch(self, request, *args, **kwargs):
        ct_model = kwargs.get('ct_model')
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product.html'
    slug_url_kwarg = 'slug'