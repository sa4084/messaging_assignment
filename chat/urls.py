
from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name = "home"),
   path('count', views.count, name = "count"),
   path('inbox/<user_id>', views.inbox, name = "inbox-event"),
   path('sent/<user_id>', views.sent, name = "sent-event"),
   path('compose', views.compose, name = "compose"),
   path('delete_event/<event_id>', views.delete_event, name = "delete-event")
]

