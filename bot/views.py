from rest_framework.views import APIView
from rest_framework.response import Response
from google import genai
from decouple import config
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class OrderBotView(APIView):
    def post(self, request):
        logger.info("Iniciado procesamiento de solicitud POST en OrderBotView")
        KEY = config("API_KEY_GEMINIAI")
        client = genai.Client(api_key=KEY)
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents="explica como funciona la inteligencia artificial en pocas palabras")
        return Response({"output": f'{response.text}'})
