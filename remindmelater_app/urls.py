from django.urls import path
from .views import ReminderListCreateAPIView

urlpatterns = [
    path(
        "create_reminder/", ReminderListCreateAPIView.as_view(), name="create_reminder"
    ),
]
