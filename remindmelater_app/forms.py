from django import forms
from .models import Reminder
from django.core.exceptions import ValidationError
from django.utils import timezone


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = "__all__"

    def clean_date(self):
        date = self.cleaned_data["date"]
        if date < timezone.now().date():
            raise ValidationError("The date cannot be in the past.")
        return date

    def clean_time(self):
        time = self.cleaned_data["time"]
        return time
