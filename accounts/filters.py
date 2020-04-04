import django_filters
from django_filters import DateFilter, CharFilter # CharFilter - to search customized parameters instead of dropdowns
from .models import *

class OrderFilter(django_filters.FilterSet):
	# Intialize DateFilter
	start_date = DateFilter(field_name='date_created', lookup_expr='gte')
	end_date = DateFilter(field_name='date_created', lookup_expr='lte')
# 	note = CharField(field_name='note', lookup_expr='icontains') icontains means ignore case sensitivity
	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer', 'date_created']