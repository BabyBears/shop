from rest_framework import generics
# from django_filters import rest_framework as filters
import django_filters
from django.db.models import Q
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    # min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    # max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    pricemin = django_filters.NumberFilter(name='shop_price',lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
    # name = django_filters.CharFilter(name='name',lookup_expr='icontains')
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self,queryset,name,value):
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))


    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax']

