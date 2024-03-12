from rest_framework import serializers
from .models import Reminder
from django.utils import timezone


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = [
            "date",
            "time",
            "message",
            "remind_via",
        ]

    def validate_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("The date cannot be in the past.")
        return value

    def validate_time(self, value):
        return value
