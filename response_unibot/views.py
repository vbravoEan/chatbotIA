from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from django.conf import settings
import openai
import os
from response_unibot.utilities import format_fact_sheet
# Create your views here.
class ResponseChat(APIView):
    def post(self, request, *args, **kwargs):
        datosRecibidos = request.data
        datos = json.dumps(datosRecibidos, indent=4, ensure_ascii=False)
        respuesta = self.get_completion(datos)
        return Response({'respuesta': respuesta.__json__()}, status=status.HTTP_200_OK)

    def get_completion(self, data, model="gpt-3.5-turbo"):
        openai.api_key = os.getenv('OPENAI_API_KEY')

        prompt = """Eres un chatbot avanzado, 'Ean Asistente', programado para ofrecer apoyo emocional personalizado y guía a los servicios del programa 'Ean Contigo' a los estudiantes de la Universidad EAN. 
        Debes responder a las preguntas y preocupaciones de los estudiantes de manera empática, informativa y útil, asegurándote de mantener la confidencialidad y la seguridad de las conversaciones."""

        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": data}
            ]
        )
        chat_response = ChatResponse(response.choices[0].message["content"])
        print(chat_response)
        return chat_response

class ChatResponse:
    def __init__(self, content):
        self.content = content

    def __json__(self):
        return {'content': self.content}