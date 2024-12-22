from django.urls import path
from .views import JobListView  # Ensure this is a valid import

urlpatterns = [
    path('', JobListView.as_view(), name='job-list'),  # Matches /api/jobs/
]
