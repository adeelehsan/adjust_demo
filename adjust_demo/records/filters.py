import django_filters
from rest_framework import filters
from rest_framework.filters import OrderingFilter

from adjust_demo.records.models import Records


class RecordsFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter("date", lookup_expr='gte')
    date_to = django_filters.DateFilter("date", lookup_expr='lte')
    channel = django_filters.CharFilter('channel', lookup_expr='iexact')
    country = django_filters.CharFilter('country', lookup_expr='iexact')
    os = django_filters.CharFilter('os', lookup_expr='iexact')

    class Meta:
        model = Records
        fields = ['date_from', 'date_to', 'channel', 'country', 'os']


class Ordering(OrderingFilter):

    def get_ordering(self, request, queryset, view):
        """
        Ordering is set by a comma delimited ?ordering=... query parameter.
        its assumed last parameter always be would ascending or descending.
        If not provided then it would switch to descending

        """
        params = request.query_params.get('ordering')
        ordering_type = request.query_params.get('ordering_type', 'descending').strip()
        if params:
            fields = [param.strip() for param in params.split(',')]
            if ordering_type == 'descending':
                fields = ['-' + f for f in fields]

            return fields

    def filter_queryset(self, request, queryset, view):

        fields = self.get_ordering(request, queryset, view)
        if fields:
            return queryset.order_by(*fields)

        else:
            return queryset


class GroupBy(filters.BaseFilterBackend):
    """
    apply group_by clause on given queryset

    """

    def filter_queryset(self, request, queryset, view):
        group_by_fields = request.query_params.get('group_by')
        if group_by_fields:
            group_by_fields = [f.strip() for f in group_by_fields.split(',')]
            return queryset.distinct(*group_by_fields)

        return queryset


class FilterFields(filters.BaseFilterBackend):
    """
    filter out of fields if only few fields are required instead of all
    """

    def filter_queryset(self, request, queryset, view):
        fields = request.query_params.get('fields')
        if fields:
            fields = [f.strip() for f in fields.split(',')]
            return queryset.values(*fields)

        return queryset

