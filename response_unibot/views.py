from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from django.conf import settings
import openai
import os
from response_unibot.utilities import format_fact_sheet, update_chat,get_initial_message


class ResponseChat(APIView):
    messages =[
                {"role": "system", "content": """Eres un chatbot avanzado, 'UniBot', programado para ofrecer apoyo emocional personalizado y guía a los servicios del programa 'Ean Contigo' a los estudiantes de la Universidad EAN. Siempre debes preguntar su nombre y llamarlo como te indique. 
        Debes responder a las preguntas y preocupaciones de los estudiantes de manera empática, informativa y útil, asegurándote de mantener la confidencialidad y la seguridad de las conversaciones Algunos de los servicios de Ean Contigo son: Programa de Mentores,Apoyo Académico,Apoyo Personal,Apoyo Psicopedagógico,Apoyo Financiero,Apoyo Institucional. Ten encuenta esta la descripción de Ean contigo: Tu desarrollo personal y profesional nos importa, por eso te ofrecemos apoyo en áreas personales y familiares, así como orientación en temas financieros. Además, te garantizamos un proceso académico adecuado con la ayuda de nuestros Mentores y las diferentes instancias de la Universidad."""}]
    
    def post(self, request, *args, **kwargs):
        datosRecibidos = request.data
        datos = json.dumps(datosRecibidos, indent=4, ensure_ascii=False)
        mensajes= update_chat(self.messages, "user", datos)
        print(mensajes)
        respuesta = self.get_completion(mensajes)
        mensajes = update_chat(mensajes, "assistant", respuesta)
        print('Esta es la respuesta ',respuesta)
        return Response({'respuesta': respuesta}, status=status.HTTP_200_OK)

    def get_completion(self, messages, model="gpt-3.5-turbo"):
        openai.api_key = os.getenv('OPENAI_API_KEY')

        response = openai.ChatCompletion.create(
            model=model,
            messages= messages
        )
        
        return response.choices[0]['message']["content"]

class ChatResponse:
    def __init__(self, content):
        self.content = content

    def __json__(self):
        return {'content': self.content}