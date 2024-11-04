from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .main import answer_question
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QARequestSerializer, QAResponseSerializer

# Existing API view
class QAPIView(APIView):
    def post(self, request):
        serializer = QARequestSerializer(data=request.data)
        if serializer.is_valid():
            context = serializer.validated_data['context']
            question = serializer.validated_data['question']
            answer = answer_question(context, question)
            response_serializer = QAResponseSerializer(data={'answer': answer})
            if response_serializer.is_valid():
                return Response(response_serializer.data)
            else:
                return Response(response_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Existing test view
def test_view(request):
    context = "Hugging Face is creating amazing tools for the AI community."
    question = "What does Hugging Face do?"
    answer = answer_question(context, question)
    return JsonResponse({'answer': answer})

# New chat view to render the chat interface
def chat_view(request):
    return render(request, 'myapp/chat.html')
