from django.urls import path
from .views import SummaryViewSet

urlpatterns=[
    path("summary/", SummaryViewSet.as_view({"get":"summary_details"})),
    path("summary2/", SummaryViewSet.as_view({"get":"summary"})),
]