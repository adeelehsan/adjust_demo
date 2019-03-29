from django.test import TestCase
from rest_framework.reverse import reverse

from adjust_demo.records.serializers import RecordSerializer


class RecordsTestCases(TestCase):

    def setUp(self):
        sample_data = [
                {
                    "id": 1,
                    "date": "07.05.2017",
                    "channel": "adcolony",
                    "country": "US",
                    "os": "android",
                    "impressions": 19887,
                    "clicks": 500,
                    "installs": 76,
                    "spend": 148.2,
                    "revenue": 149.04
                },
                {
                    "id": 2,
                    "date": "07.05.2017",
                    "channel": "adcolony",
                    "country": "US",
                    "os": "android",
                    "impressions": 19887,
                    "clicks": 494,
                    "installs": 76,
                    "spend": 148.2,
                    "revenue": 149.04
                },
            ]
        for obj in sample_data:
            serializer = RecordSerializer(data=obj)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

        self.url = reverse("records-list")

    def test_records_list(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    def test_add_record(self):
        obj_data = {
                    "date": "07.05.2018",
                    "channel": "adcolony",
                    "country": "US",
                    "os": "ios",
                    "impressions": 19887,
                    "clicks": 500,
                    "installs": 76,
                    "spend": 148.2,
                    "revenue": 149.04
                }
        import pdb; pdb.set_trace()
        response = self.client.post(self.url + 'add_record/', data=obj_data, format='json')
        self.assertEqual(200, response.status_code)
