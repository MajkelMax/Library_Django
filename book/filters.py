import django_filters
from django_filters import DateFilter

from .models import *


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="pub_date", lookup_expr='gte')  # grater than, equal too
    end_date = DateFilter(field_name="pub_date", lookup_expr='lte')  # less than, equal too

    class Meta:
        model = Book
        fields = ['title', 'author', 'pub_date', 'language']

