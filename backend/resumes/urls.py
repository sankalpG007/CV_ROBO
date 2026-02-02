# backend/resumes/urls.py
from django.urls import path
from .views import ResumeView, EducationView
from .views import ResumeView, EducationView, ExperienceView, SkillView

urlpatterns = [
    path('', ResumeView.as_view(), name='resume'),
    path('education/', EducationView.as_view(), name='education'),
    path('experience/', ExperienceView.as_view(), name='experience'),
    path('skill/', SkillView.as_view(), name='skill'),
]
