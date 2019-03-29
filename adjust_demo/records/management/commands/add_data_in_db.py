import csv

from django.core.management.base import BaseCommand

from adjust_demo.records.serializers import RecordSerializer


class Command(BaseCommand):
    help = 'add sample data to database'

    def handle(self, *args, **kwargs):
        with open("sample_data.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                serializer = RecordSerializer(data=row)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
        print('sample data is added to database')
        csvfile.close()
