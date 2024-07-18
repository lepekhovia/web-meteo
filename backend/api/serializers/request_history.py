from rest_framework import serializers

from core.models.request_history import RequestHistory


class RequestHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestHistory
        fields = ['town']
