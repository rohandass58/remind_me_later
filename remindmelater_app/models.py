from django.db import models


class Reminder(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    remind_via = models.CharField(
        max_length=10,
        choices=[
            ("SMS", "SMS"),
            ("Email", "Email"),
        ],
    )

    def __str__(self) -> str:
        return self.message
