from django.urls import path
from .views import NotificationListView, MarkAllReadView

urlpatterns = [
    path("notifications/", NotificationListView.as_view(), name="notifications"),
    path("notifications/mark-all-read/", MarkAllReadView.as_view(), name="notifications-mark-all-read"),
]