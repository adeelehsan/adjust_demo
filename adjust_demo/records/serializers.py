from rest_framework import serializers

from adjust_demo.records.models import Records


class RecordSerializer(serializers.ModelSerializer):
    date = serializers.DateField(input_formats=["%d.%m.%Y"], format="%d.%m.%Y", required=False)
    channel = serializers.CharField(required=False)
    country = serializers.CharField(max_length=2, required=False)
    os = serializers.CharField(max_length=50, required=False)
    impressions = serializers.IntegerField(required=False)
    clicks = serializers.IntegerField(required=False)
    installs = serializers.IntegerField(required=False)
    spend = serializers.FloatField(required=False)
    revenue = serializers.FloatField(required=False)
    cpi = serializers.FloatField(required=False)

    class Meta:
        model = Records
        fields = '__all__'

    def create(self, validated_data):
        spend = validated_data.get('spend')
        installs = validated_data.get('installs')
        if spend and installs:
            validated_data['cpi'] = "{0:.2f}".format(validated_data['spend'] / validated_data['installs'])
        return Records.objects.create(**validated_data)
