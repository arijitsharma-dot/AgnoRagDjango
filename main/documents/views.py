from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Document

class UploadPDFView(APIView):
    def post(self, request):
        pdf = request.FILES.get("file")

        if not pdf:
            return Response(
                {"error": "No PDF provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        doc = Document.objects.create(file=pdf)
        return Response(
            {"message": "PDF uploaded successfully", "doc_id": doc.id},
            status=status.HTTP_201_CREATED,
        )
