from operator import itemgetter

import django_filters
from rest_framework import viewsets, generics
from rest_framework.decorators import list_route

from adjust_demo.records.filters import RecordsFilter, Ordering, GroupBy, FilterFields
from adjust_demo.records.models import Records
from adjust_demo.records.serializers import RecordSerializer
from adjust_demo.records.utils import success_response, failure_response


class RecordsViewSet(generics.ListAPIView, viewsets.ViewSet):
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, Ordering,
                       GroupBy, FilterFields)
    filter_class = RecordsFilter
    queryset = Records.objects.all()
    serializer_class = RecordSerializer

    @list_route(methods=['POST'])
    def add_record(self, request):
        request_serializer = RecordSerializer(data=request.data)
        if request_serializer.is_valid(raise_exception=True):
            request_serializer.save()

        return success_response(data=request_serializer.data, status_code=200)

    @list_route(methods=['GET'])
    def get_cpi(self, request):
        country = request.query_params.get('country')
        if country:
            records = Records.objects.filter(country__iexact=country.strip())

            group_by_fields = request.query_params.get('group_by')
            if group_by_fields:
                group_by_fields = [f.strip() for f in group_by_fields.split(',')]
                records = records.distinct(*group_by_fields)

            if request.query_params.get('ordering'):
                order_type = request.query_params.get('ordering_type', 'descending')
                reverse = True if order_type.strip() == 'descending' else False
                records = sorted(records.values(), key=itemgetter('cpi'), reverse=reverse)

            serializer = RecordSerializer(records, many=True)
            return success_response(data=serializer.data, status_code=200)

        return failure_response(status_code=400)
