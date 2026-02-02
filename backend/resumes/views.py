# backend/resumes/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Resume
from .serializers import ResumeSerializer, EducationSerializer
from .serializers import ExperienceSerializer, SkillSerializer
from .models import Experience, Skill


class ExperienceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        resume = Resume.objects.get(user=request.user)
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(resume=resume)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        resume = Resume.objects.get(user=request.user)
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(resume=resume)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResumeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        resume, _ = Resume.objects.get_or_create(user=request.user)
        serializer = ResumeSerializer(resume)
        return Response(serializer.data)

    def post(self, request):
        resume, _ = Resume.objects.get_or_create(user=request.user)
        serializer = ResumeSerializer(resume, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EducationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        resume = Resume.objects.get(user=request.user)
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(resume=resume)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
