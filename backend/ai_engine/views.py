from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from resumes.models import Resume
from .gemini_client import generate_text
from .prompts import resume_summary_prompt


class GenerateSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        resume = Resume.objects.get(user=request.user)

        resume_data = {
            "educations": list(resume.educations.values()),
            "experiences": list(resume.experiences.values()),
            "skills": list(resume.skills.values()),
        }

        prompt = resume_summary_prompt(resume_data)
        summary = generate_text(prompt)

        resume.summary = summary
        resume.save()

        return Response(
            {"summary": summary},
            status=status.HTTP_200_OK
        )
