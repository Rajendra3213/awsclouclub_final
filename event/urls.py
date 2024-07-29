from django.urls import path
from .views import EventDetail,EventList,GrandEvent
app_name='event'
urlpatterns = [
    path('',EventList.as_view(),name="EventList"),
    path('view/<int:id>',EventDetail.as_view(),name="EventDetail"),
    path('grand/<int:id>',GrandEvent.as_view(),name="GrandEvent")
]
