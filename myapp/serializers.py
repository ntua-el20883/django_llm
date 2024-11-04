# myapp/serializers.py
from rest_framework import serializers

class QARequestSerializer(serializers.Serializer):
    context = serializers.CharField()
    question = serializers.CharField()

class QAResponseSerializer(serializers.Serializer):
    answer = serializers.CharField()
