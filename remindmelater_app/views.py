from rest_framework.generics import ListCreateAPIView
from .models import Reminder
from .serializers import ReminderSerializer
from .forms import ReminderForm
from rest_framework.response import Response
from rest_framework import status


class ReminderListCreateAPIView(ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    def get(self, request, *args, **kwargs):
        reminders = self.get_queryset()
        serializer = self.get_serializer(reminders, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        form = ReminderForm(request.data)
        if form.is_valid():
            form.save()
            return Response(
                {"status": "Reminder created successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
