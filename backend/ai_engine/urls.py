from django.urls import path
from .views import GenerateSummaryView

urlpatterns = [
    path('summary/', GenerateSummaryView.as_view(), name='ai-summary'),
]
