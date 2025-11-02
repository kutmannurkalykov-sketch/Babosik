from .models import Category
from django.views.generic import ListView


class CategoryListView(ListView):
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'category_list.html'
